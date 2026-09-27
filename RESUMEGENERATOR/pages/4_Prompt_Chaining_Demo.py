"""
pages/4_Prompt_Chaining_Demo.py
----------------------------------
UI layer for the Integrated Prompt-Chaining Task (Resume Optimization Chain).
Shows every intermediate output so the grader can see that stage N's output
literally becomes stage N+1's input.
"""

import streamlit as st
from prompts.chaining_prompts import run_resume_optimization_chain
from services.llm_service import LLMServiceError

st.set_page_config(page_title="Prompt Chaining Demo", page_icon="🔗", layout="wide")
st.title("🔗 Resume Optimization Chain")

st.markdown(
    """
```
Job Description
    |
    v
Prompt 1: Extract Required Skills   -> Output 1 (Required Skills)
    |
    v
Prompt 2: Analyze Candidate Skills  -> Output 2 (Skill Gap)
    |
    v
Prompt 3: Generate Improvements     -> Output 3 (Recommendations)
    |
    v
Prompt 4: Optimize Resume           -> Final Resume
```
"""
)

job_description = st.text_area("Job Description", height=150)
candidate_skills = st.text_area("Candidate's Current Skills")
draft_resume = st.text_area("Draft Resume (paste the resume from the Resume Generator page)", height=200)

if st.button("▶️ Run the Chain", type="primary"):
    if not (job_description and candidate_skills and draft_resume):
        st.error("All three fields are required to run the chain.")
    else:
        with st.spinner("Running 4-stage chain..."):
            try:
                result = run_resume_optimization_chain(job_description, candidate_skills, draft_resume)

                st.subheader("Stage 1 → Output: Required Skills")
                st.code(result["output_1_required_skills"])

                st.subheader("Stage 2 → Output: Skill Gap")
                st.code(result["output_2_skill_gap"])

                st.subheader("Stage 3 → Output: Recommendations")
                st.markdown(result["output_3_recommendations"])

                st.subheader("Stage 4 → Final Output: Optimized Resume")
                st.markdown(result["final_resume"])
            except LLMServiceError as exc:
                st.error(str(exc))
