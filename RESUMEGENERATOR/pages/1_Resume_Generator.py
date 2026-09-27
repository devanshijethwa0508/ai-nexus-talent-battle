"""
pages/1_Resume_Generator.py
------------------------------
UI layer for Project 1. Flow (Requirement 6):

    Candidate Information -> Professional Information -> Job Description
        -> Generate Resume -> Generated Resume -> ATS Analysis
        -> Improvement Suggestions -> Download
"""

import streamlit as st
from utils.validators import validate_candidate_info
from utils.export_utils import resume_to_txt, resume_to_docx
from services.resume_service import generate_resume, analyze_and_improve
from services.llm_service import LLMServiceError

st.set_page_config(page_title="Resume Generator", page_icon="📄", layout="wide")
st.title("📄 AI Resume Generator")

if "resume_sections" not in st.session_state:
    st.session_state.resume_sections = None
if "ats_result" not in st.session_state:
    st.session_state.ats_result = None

# ---------------------------------------------------------------- Candidate Information
st.header("1. Candidate Information")
c1, c2, c3 = st.columns(3)
full_name = c1.text_input("Full Name")
email = c2.text_input("Email")
phone = c3.text_input("Phone")
c4, c5, c6 = st.columns(3)
location = c4.text_input("Location")
linkedin = c5.text_input("LinkedIn URL")
github = c6.text_input("GitHub URL")

# ---------------------------------------------------------------- Professional Information
st.header("2. Professional Information")
target_role = st.text_input("Target Role", placeholder="e.g. Embedded Systems Engineer")
technical_skills = st.text_area("Technical Skills (comma-separated)")
education = st.text_area("Education")
experience = st.text_area("Experience (optional)")
projects = st.text_area("Projects")
certifications = st.text_area("Certifications (optional)")

# ---------------------------------------------------------------- Job Description
st.header("3. Job Description")
job_description = st.text_area("Paste the target Job Description", height=150)

candidate = {
    "full_name": full_name, "email": email, "phone": phone, "location": location,
    "linkedin": linkedin, "github": github, "target_role": target_role,
    "technical_skills": technical_skills, "education": education,
    "experience": experience, "projects": projects,
    "certifications": certifications, "job_description": job_description,
}

# ---------------------------------------------------------------- Generate Resume
st.header("4. Generate Resume")
if st.button("🚀 Generate Resume", type="primary"):
    errors = validate_candidate_info(candidate)
    if errors:
        for e in errors:
            st.error(e)
    else:
        with st.spinner("Generating resume..."):
            try:
                st.session_state.resume_sections = generate_resume(candidate, job_description)
                st.session_state.ats_result = None
            except LLMServiceError as exc:
                st.error(str(exc))

# ---------------------------------------------------------------- Generated Resume
if st.session_state.resume_sections:
    st.header("5. Generated Resume")
    for heading, body in st.session_state.resume_sections.items():
        with st.expander(heading, expanded=True):
            st.markdown(body)

    # ------------------------------------------------------------ ATS Analysis
    st.header("6. ATS Analysis")
    if st.button("🔍 Run ATS Analysis"):
        with st.spinner("Analyzing against job description..."):
            try:
                st.session_state.ats_result = analyze_and_improve(
                    st.session_state.resume_sections, job_description
                )
            except LLMServiceError as exc:
                st.error(str(exc))

    if st.session_state.ats_result:
        ats = st.session_state.ats_result["ats"]
        st.metric("ATS Score", f"{ats['ats_score']}%")

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("**Matched Keywords**")
            for kw in ats["matched"]:
                st.markdown(f"✓ {kw}")
        with col_b:
            st.markdown("**Missing Keywords**")
            for kw in ats["missing"]:
                st.markdown(f"✗ {kw}")

        # -------------------------------------------------------- Improvement Suggestions
        st.header("7. Improvement Suggestions")
        st.markdown(st.session_state.ats_result["improvements"])

    # ------------------------------------------------------------ Download
    st.header("8. Download")
    d1, d2 = st.columns(2)
    d1.download_button(
        "⬇️ Download as TXT",
        data=resume_to_txt(st.session_state.resume_sections),
        file_name=f"{full_name or 'resume'}.txt",
        mime="text/plain",
    )
    d2.download_button(
        "⬇️ Download as DOCX",
        data=resume_to_docx(st.session_state.resume_sections, full_name),
        file_name=f"{full_name or 'resume'}.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
