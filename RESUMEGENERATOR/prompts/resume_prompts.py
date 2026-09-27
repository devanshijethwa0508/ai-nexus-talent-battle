"""
prompts/resume_prompts.py
--------------------------
Prompt Layer for Project 1 (AI Resume Generator).

Demonstrates the required techniques:
  - ROLE PROMPT        -> ROLE_SYSTEM_PROMPT
  - STRUCTURED PROMPT   -> build_resume_prompt() (fixed Role/Context/Task/
                           Constraints/Output-format sections)
  - FEW-SHOT PROMPT     -> build_summary_fewshot_prompt()
  - ZERO-SHOT PROMPT    -> build_ats_keyword_prompt()
"""

# ---------------------------------------------------------------------------
# ROLE PROMPTING
# Assigning the LLM a persona changes its output style/priorities.
# ---------------------------------------------------------------------------
ROLE_SYSTEM_PROMPT = (
    "You are a senior technical recruiter and certified resume writer with "
    "12 years of experience placing engineering candidates at product and "
    "core-engineering companies. You write ATS-friendly, achievement-focused "
    "resume content and never invent facts the candidate did not provide."
)


def build_resume_prompt(candidate: dict, job_description: str) -> str:
    """
    STRUCTURED PROMPT
    Fixed sections: Role / Context / Task / Candidate Info / Job Description /
    Constraints / Output Requirements. This is what production prompt
    layers look like -- predictable structure the app can rely on.
    """
    return f"""
ROLE:
You are an expert resume writer specializing in ATS-optimized resumes for
engineering and technical roles.

CONTEXT:
A fresh graduate is applying for the role below and needs a resume tailored
to it, built only from the facts they supplied.

TASK:
Write the following resume sections, in this exact order, using Markdown
headings (##): Professional Summary, Technical Skills, Experience, Projects,
Education, Certifications.

CANDIDATE INFORMATION:
Name: {candidate.get('full_name')}
Target Role: {candidate.get('target_role')}
Technical Skills: {candidate.get('technical_skills')}
Education: {candidate.get('education')}
Experience: {candidate.get('experience') or 'None provided'}
Projects: {candidate.get('projects')}
Certifications: {candidate.get('certifications') or 'None provided'}

JOB DESCRIPTION:
{job_description}

CONSTRAINTS:
- Do NOT invent employers, dates, tools, or metrics the candidate did not provide.
- Where the candidate gave a project but no numeric result, describe scope/impact
  qualitatively instead of fabricating a number.
- Mirror key terminology from the job description wherever it is truthfully
  supported by the candidate's background.
- Keep the Professional Summary to 3-4 sentences.

OUTPUT REQUIREMENTS:
Return only the six Markdown sections, nothing else (no preamble, no notes).
"""


def build_summary_fewshot_prompt(candidate: dict) -> str:
    """
    FEW-SHOT PROMPT
    Shows the model two worked examples before asking it to produce a third,
    so tone/length/structure are learned from examples rather than instructions.
    """
    return f"""
Write a Professional Summary for a resume. Follow the style of these examples.

Example 1
Input: Fresher, B.Tech CSE, skills: Python, Django, PostgreSQL, one internship
building a billing dashboard.
Output: "Computer Science graduate with hands-on experience building
full-stack billing dashboards using Python, Django and PostgreSQL. Focused on
writing clean, testable backend code and shipping features that hold up in
production."

Example 2
Input: Fresher, B.Tech ECE, skills: Embedded C, STM32, RTOS, built a
sensor-fusion firmware project.
Output: "Electronics graduate specializing in embedded firmware, with
project experience building sensor-fusion pipelines on STM32 using Embedded C
and RTOS. Comfortable working close to hardware, from register-level drivers
to real-time task scheduling."

Now write one for this candidate:
Input: Fresher, {candidate.get('target_role')}, skills: {candidate.get('technical_skills')},
projects: {candidate.get('projects')}
Output:
"""


def build_ats_keyword_prompt(job_description: str) -> str:
    """
    ZERO-SHOT PROMPT
    No examples given -- the instruction alone is expected to be enough
    for a well-understood extraction task.
    """
    return f"""
Extract the top 15 technical skills, tools, and keywords an ATS system would
scan for in this job description. Return a plain comma-separated list only,
no numbering, no extra text.

Job Description:
{job_description}
"""


def build_improvement_prompt(resume_text: str, missing_keywords: list[str],
                              job_description: str) -> str:
    """Structured prompt for Requirement 4 -- Resume Improvement suggestions."""
    return f"""
ROLE:
You are a resume coach who gives specific, actionable feedback.

TASK:
Given the resume draft and the missing ATS keywords below, list 5-7 concrete
improvement recommendations. Each must be one line, start with a verb, and
where relevant reference a specific missing keyword.

RESUME DRAFT:
{resume_text}

MISSING KEYWORDS:
{', '.join(missing_keywords) if missing_keywords else 'None'}

JOB DESCRIPTION:
{job_description}

OUTPUT FORMAT:
A plain bullet list, one recommendation per line, starting with "- ".
"""
