"""
pages/3_Content_Generator.py
-------------------------------
UI layer for Project 3.
"""

import streamlit as st
from utils.validators import validate_content_request
from services.content_service import generate_content, generate_multi_output, transform_content
from services.llm_service import LLMServiceError

st.set_page_config(page_title="Content Generator", page_icon="✍️", layout="wide")
st.title("✍️ AI Content Generator")

if "generated_content" not in st.session_state:
    st.session_state.generated_content = None
if "multi_output" not in st.session_state:
    st.session_state.multi_output = None

tab_single, tab_multi = st.tabs(["Single Platform", "Multi-Output (all platforms at once)"])

# ------------------------------------------------------------------ Single Platform
with tab_single:
    st.header("1. Content Request")
    c1, c2 = st.columns(2)
    content_type = c1.selectbox(
        "Content Type",
        ["LinkedIn Post", "Instagram Caption", "YouTube Description", "Blog",
         "Technical Article", "Email", "Tweet/X Post"],
    )
    tone = c2.selectbox(
        "Tone",
        ["Professional", "Technical", "Educational", "Conversational",
         "Persuasive", "Formal", "Creative"],
    )
    topic = st.text_input("Topic")
    audience = st.text_input("Target Audience")
    keywords = st.text_input("Keywords (comma-separated)")
    length = st.selectbox("Content Length", ["Short", "Medium", "Long"])

    request = {
        "content_type": content_type, "tone": tone, "topic": topic,
        "audience": audience, "keywords": keywords, "length": length,
    }

    if st.button("✨ Generate Content", type="primary"):
        errors = validate_content_request(request)
        if errors:
            for e in errors:
                st.error(e)
        else:
            with st.spinner("Generating..."):
                try:
                    st.session_state.generated_content = generate_content(request)
                except LLMServiceError as exc:
                    st.error(str(exc))

    if st.session_state.generated_content:
        st.header("2. Generated Content")
        st.text_area("Output", st.session_state.generated_content, height=250, key="output_box")

        st.header("3. Improve / Transform")
        action_labels = {
            "improve": "Improve", "shorten": "Shorten", "expand": "Expand",
            "generate_headline": "Generate Headline",
            "generate_hashtags": "Generate Hashtags", "generate_cta": "Generate CTA",
        }
        cols = st.columns(len(action_labels))
        for col, (action, label) in zip(cols, action_labels.items()):
            if col.button(label):
                with st.spinner(f"{label}..."):
                    st.session_state.generated_content = transform_content(
                        st.session_state.generated_content, action
                    )
                    st.rerun()

        new_tone = st.selectbox("Change Tone To", list(
            ["Professional", "Technical", "Educational", "Conversational",
             "Persuasive", "Formal", "Creative"]), key="new_tone")
        if st.button("Change Tone"):
            with st.spinner("Changing tone..."):
                st.session_state.generated_content = transform_content(
                    st.session_state.generated_content, "change_tone", new_tone
                )
                st.rerun()

# ------------------------------------------------------------------ Multi-Output
with tab_multi:
    st.header("Generate Everything At Once")
    st.caption(
        "For a single topic: 1 LinkedIn Post, 1 Instagram Caption, "
        "1 YouTube Description, 5 Hashtags, 3 Headlines, 1 CTA."
    )
    m_topic = st.text_input("Topic", key="multi_topic")
    m_audience = st.text_input("Target Audience", key="multi_audience")
    m_tone = st.selectbox("Tone", ["Professional", "Educational", "Conversational"], key="multi_tone")

    if st.button("🚀 Generate All Formats"):
        if not m_topic.strip():
            st.error("Topic is required.")
        else:
            with st.spinner("Generating across platforms..."):
                try:
                    st.session_state.multi_output = generate_multi_output(m_topic, m_audience, m_tone)
                except LLMServiceError as exc:
                    st.error(str(exc))

    if st.session_state.multi_output:
        out = st.session_state.multi_output
        st.subheader("LinkedIn Post")
        st.write(out.get("linkedin_post"))
        st.subheader("Instagram Caption")
        st.write(out.get("instagram_caption"))
        st.subheader("YouTube Description")
        st.write(out.get("youtube_description"))
        st.subheader("Hashtags")
        st.write(" ".join(out.get("hashtags", [])))
        st.subheader("Headlines")
        for h in out.get("headlines", []):
            st.markdown(f"- {h}")
        st.subheader("CTA")
        st.write(out.get("cta"))
