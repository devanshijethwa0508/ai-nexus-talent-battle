"""
utils/validators.py
--------------------
Input Validation layer. Kept separate from Application Logic so every
Streamlit page can reuse the same rules and error messages.
"""

import re

EMAIL_RE = re.compile(r"^[\w\.\+\-]+@[\w\-]+\.[a-zA-Z]{2,}$")
PHONE_RE = re.compile(r"^[\d\+\-\s\(\)]{7,15}$")


def validate_candidate_info(data: dict) -> list[str]:
    """Returns a list of human-readable error messages (empty list = valid)."""
    errors = []

    if not data.get("full_name", "").strip():
        errors.append("Full Name is required.")

    email = data.get("email", "").strip()
    if not email:
        errors.append("Email is required.")
    elif not EMAIL_RE.match(email):
        errors.append("Email format looks invalid.")

    phone = data.get("phone", "").strip()
    if phone and not PHONE_RE.match(phone):
        errors.append("Phone number format looks invalid.")

    if not data.get("target_role", "").strip():
        errors.append("Target Role is required.")

    if not data.get("technical_skills", "").strip():
        errors.append("At least one Technical Skill is required.")

    if not data.get("job_description", "").strip():
        errors.append("Job Description is required for ATS matching.")

    return errors


def validate_interview_config(data: dict) -> list[str]:
    errors = []
    for field in ("target_role", "experience_level", "domain", "interview_type"):
        if not data.get(field, "").strip():
            errors.append(f"{field.replace('_', ' ').title()} is required.")
    return errors


def validate_content_request(data: dict) -> list[str]:
    errors = []
    if not data.get("topic", "").strip():
        errors.append("Topic is required.")
    if not data.get("content_type", "").strip():
        errors.append("Content Type is required.")
    if not data.get("tone", "").strip():
        errors.append("Tone is required.")
    return errors
