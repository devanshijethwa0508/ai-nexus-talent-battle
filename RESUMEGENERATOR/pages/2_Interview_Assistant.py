"""
pages/2_Interview_Assistant.py
---------------------------------
UI layer for Project 2. Flow:

    Candidate Configuration -> Generate Question -> Candidate Answers
        -> AI Evaluation -> Score -> Feedback -> Next Question
        -> ... -> Interview Summary
"""

import streamlit as st
from utils.validators import validate_interview_config
from utils.export_utils import interview_report_to_txt
from services.interview_service import generate_question, evaluate_answer, build_summary
from services.llm_service import LLMServiceError

st.set_page_config(page_title="Interview Assistant", page_icon="🎤", layout="wide")
st.title("🎤 AI Interview Assistant")

TOTAL_QUESTIONS = 5

for key, default in [
    ("interview_config", None), ("current_question", None),
    ("question_number", 1), ("evaluations", []), ("summary", None),
]:
    if key not in st.session_state:
        st.session_state[key] = default

# ---------------------------------------------------------------- Candidate Configuration
st.header("1. Candidate Configuration")
c1, c2 = st.columns(2)
target_role = c1.text_input("Target Role", placeholder="Python Developer")
experience_level = c2.selectbox("Experience Level", ["Fresher", "1-3 years", "3-5 years", "5+ years"])
c3, c4 = st.columns(2)
domain = c3.text_input("Technology / Domain", placeholder="Python + DSA")
interview_type = c4.selectbox("Interview Type", ["Technical", "HR", "Managerial"])

if st.button("Start Interview", type="primary"):
    config = {
        "target_role": target_role, "experience_level": experience_level,
        "domain": domain, "interview_type": interview_type,
    }
    errors = validate_interview_config(config)
    if errors:
        for e in errors:
            st.error(e)
    else:
        st.session_state.interview_config = config
        st.session_state.question_number = 1
        st.session_state.evaluations = []
        st.session_state.summary = None
        st.session_state.current_question = None

# ---------------------------------------------------------------- Interview Simulation
if st.session_state.interview_config and st.session_state.question_number <= TOTAL_QUESTIONS:
    st.header(f"2. Question {st.session_state.question_number} of {TOTAL_QUESTIONS}")

    if st.session_state.current_question is None:
        with st.spinner("Generating question..."):
            try:
                st.session_state.current_question = generate_question(
                    st.session_state.interview_config, st.session_state.question_number
                )
            except LLMServiceError as exc:
                st.error(str(exc))

    q = st.session_state.current_question
    if q:
        st.markdown(f"**[{q.get('difficulty')} | {q.get('category')}]** {q.get('question')}")
        answer = st.text_area("Your Answer", key=f"answer_{st.session_state.question_number}")

        if st.button("Submit Answer"):
            with st.spinner("Evaluating..."):
                try:
                    result = evaluate_answer(q["question"], answer, q["category"])
                    result["question"] = q["question"]
                    result["category"] = q["category"]
                    st.session_state.evaluations.append(result)

                    st.subheader("Score")
                    st.write(
                        {k: result[k] for k in
                         ["technical_accuracy", "relevance", "completeness",
                          "clarity", "communication", "overall_score"]}
                    )

                    st.subheader("Feedback")
                    st.markdown("**Strengths**")
                    for s in result.get("strengths", []):
                        st.markdown(f"✓ {s}")
                    st.markdown("**Weaknesses**")
                    for w in result.get("weaknesses", []):
                        st.markdown(f"✗ {w}")
                    st.markdown(f"**Suggested Improvement:** {result.get('suggested_improvement')}")

                    st.session_state.question_number += 1
                    st.session_state.current_question = None
                    if st.button("Next Question ➡️"):
                        st.rerun()
                except LLMServiceError as exc:
                    st.error(str(exc))

# ---------------------------------------------------------------- Interview Summary
if (st.session_state.interview_config
        and st.session_state.question_number > TOTAL_QUESTIONS
        and st.session_state.evaluations):
    st.header("3. Interview Performance Report")

    if st.session_state.summary is None:
        with st.spinner("Building summary..."):
            try:
                st.session_state.summary = build_summary(
                    st.session_state.evaluations, st.session_state.interview_config
                )
            except LLMServiceError as exc:
                st.error(str(exc))

    if st.session_state.summary:
        s = st.session_state.summary
        m1, m2 = st.columns(2)
        m1.metric("Questions Attempted", s.get("questions_attempted"))
        m2.metric("Average Score", f"{s.get('average_score')}/10")

        st.markdown("**Strong Areas:** " + ", ".join(s.get("strong_areas", [])))
        st.markdown("**Weak Areas:** " + ", ".join(s.get("weak_areas", [])))
        st.markdown(f"**Overall Recommendation:** {s.get('overall_recommendation')}")

        st.download_button(
            "⬇️ Download Report (TXT)",
            data=interview_report_to_txt(s),
            file_name="interview_report.txt",
            mime="text/plain",
        )
