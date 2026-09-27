"""
services/resume_service.py
-----------------------------
Application Logic for Project 1. Orchestrates prompt building, LLM calls,
ATS analysis and improvement suggestions -- the Streamlit page (UI layer)
never talks to prompts/ or llm_service directly.
"""

from services.llm_service import generate
from services.ats_service import run_ats_analysis
from prompts.resume_prompts import (
    ROLE_SYSTEM_PROMPT,
    build_resume_prompt,
    build_summary_fewshot_prompt,
    build_improvement_prompt,
)


def generate_resume(candidate: dict, job_description: str) -> dict:
    """
    Runs the Structured Prompt for the full resume, and separately the
    Few-Shot prompt for just the summary line (kept for the assignment's
    "demonstrate at least 4 techniques" requirement, and because a
    few-shot summary is often punchier than one baked into a long prompt).
    """
    full_resume_md = generate(
        build_resume_prompt(candidate, job_description),
        system=ROLE_SYSTEM_PROMPT,
        max_tokens=1800,
    )
    fewshot_summary = generate(
        build_summary_fewshot_prompt(candidate),
        system=ROLE_SYSTEM_PROMPT,
        max_tokens=200,
    )

    sections = _split_markdown_sections(full_resume_md)
    if fewshot_summary.strip():
        sections["Professional Summary"] = fewshot_summary.strip()

    return sections


def _split_markdown_sections(markdown_text: str) -> dict:
    """Parses '## Heading' blocks into an ordered dict for export/rendering."""
    sections = {}
    current_heading = None
    buffer = []

    for line in markdown_text.splitlines():
        if line.strip().startswith("## "):
            if current_heading:
                sections[current_heading] = "\n".join(buffer).strip()
            current_heading = line.strip("# ").strip()
            buffer = []
        else:
            buffer.append(line)

    if current_heading:
        sections[current_heading] = "\n".join(buffer).strip()

    return sections or {"Resume": markdown_text}


def analyze_and_improve(sections: dict, job_description: str) -> dict:
    """Runs Requirement 3 (ATS) then Requirement 4 (Improvement) in sequence."""
    resume_text = "\n\n".join(sections.values())
    skills_text = sections.get("Technical Skills", resume_text)

    ats_result = run_ats_analysis(job_description, skills_text)

    improvements = generate(
        build_improvement_prompt(resume_text, ats_result["missing"], job_description),
        max_tokens=500,
    )

    return {"ats": ats_result, "improvements": improvements}
