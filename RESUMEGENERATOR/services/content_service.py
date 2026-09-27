"""
services/content_service.py
------------------------------
Application Logic for Project 3.
"""

from services.llm_service import generate, generate_json
from prompts.content_prompts import (
    build_content_prompt,
    build_multi_output_prompt,
    build_transform_prompt,
)


def generate_content(request: dict) -> str:
    return generate(build_content_prompt(request), max_tokens=800)


def generate_multi_output(topic: str, audience: str, tone: str) -> dict:
    return generate_json(build_multi_output_prompt(topic, audience, tone), max_tokens=1200)


def transform_content(content: str, action: str, extra: str = "") -> str:
    return generate(build_transform_prompt(content, action, extra), max_tokens=600)
