"""
app.py
-------
AI NEXUS 360 — Home page.

    AI NEXUS 360
        |
        v
    Prompt Engineering
     /      |       \\
Resume  Interview  Content
 Gen     Assistant  Generator
  |         |          |
 ATS    Evaluation  Platform
Analysis & Feedback Optimization
     \\      |       /
      Prompt Chaining
            |
            v
     AI Application Workflow

This file is the User Interface entry point. Streamlit's multipage
mechanism picks up every file in pages/ automatically and lists them
in the sidebar.
"""

import streamlit as st

st.set_page_config(page_title="AI NEXUS 360", page_icon="🧭", layout="wide")

st.title("🧭 AI NEXUS 360")
st.subheader("Generative AI, Prompt Engineering & AI Application Development")

st.markdown(
    """
Welcome. This app is a mini GenAI ecosystem with three tools that all share
one Prompt Library and one AI service layer:

- **📄 Resume Generator** — ATS-oriented resume generation + ATS scoring + improvement suggestions
- **🎤 Interview Assistant** — role-based question generation, scored evaluation, performance report
- **✍️ Content Generator** — multi-platform content generation from a single topic
- **🔗 Prompt Chaining Demo** — the Resume Optimization Chain, stage by stage

Use the sidebar to navigate. Each page collects its own inputs — nothing
here is shared state you need to fill in twice.
"""
)

st.info(
    "First time running this? Copy `.env.example` to `.env` and add your "
    "`ANTHROPIC_API_KEY` before generating anything."
)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Apps", "3")
col2.metric("Prompt Techniques Demonstrated", "9")
col3.metric("Prompt Library", "100 prompts")
col4.metric("Chaining Stages", "4")
