"""
services/ats_service.py
--------------------------
Requirement 3 (ATS Analysis) pipeline:

    Job Description -> Keyword Extraction -> Candidate Skill Matching
        -> Matched Keywords -> Missing Keywords -> ATS Match Score
"""

import re
from services.llm_service import generate
from prompts.resume_prompts import build_ats_keyword_prompt


def extract_keywords(job_description: str) -> list[str]:
    """Zero-shot LLM call, then light normalization/cleanup."""
    raw = generate(build_ats_keyword_prompt(job_description), max_tokens=300)
    keywords = [kw.strip() for kw in raw.split(",") if kw.strip()]
    return keywords[:15]


def match_keywords(keywords: list[str], candidate_skills: str) -> dict:
    """
    Simple, transparent keyword-based matching (Q15 contrasts this with
    semantic matching in the theory answers). Case-insensitive substring
    match against the candidate's stated skills/resume text.
    """
    skills_lower = candidate_skills.lower()
    matched, missing = [], []

    for kw in keywords:
        kw_clean = re.sub(r"[^a-z0-9\+\#\. ]", "", kw.lower())
        if kw_clean and kw_clean in skills_lower:
            matched.append(kw)
        else:
            missing.append(kw)

    return {"matched": matched, "missing": missing}


def compute_ats_score(matched: list[str], total_keywords: list[str]) -> int:
    if not total_keywords:
        return 0
    return round(100 * len(matched) / len(total_keywords))


def run_ats_analysis(job_description: str, candidate_skills: str) -> dict:
    keywords = extract_keywords(job_description)
    match_result = match_keywords(keywords, candidate_skills)
    score = compute_ats_score(match_result["matched"], keywords)

    return {
        "keywords": keywords,
        "matched": match_result["matched"],
        "missing": match_result["missing"],
        "ats_score": score,
    }
