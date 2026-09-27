"""
services/llm_service.py
------------------------
Single choke point for every call to the AI/LLM service.

This is the "AI/LLM Service" layer in the architecture:

    User Interface -> Application Logic -> Prompt Layer -> AI/LLM Service
        -> Response Processing -> Final Output

Every other module builds a prompt (Prompt Layer) and hands it to
`generate()` or `generate_json()` here. This keeps API-key handling,
model selection, retries and error handling in exactly one place.
"""

import os
import json
import time
from dotenv import load_dotenv
from anthropic import Anthropic, APIError, APIConnectionError

load_dotenv()

MODEL_NAME = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")
MAX_RETRIES = 2


class LLMServiceError(Exception):
    """Raised when the AI service cannot produce a usable response."""


def _get_client() -> Anthropic:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise LLMServiceError(
            "ANTHROPIC_API_KEY is not set. Copy .env.example to .env and add your key."
        )
    return Anthropic(api_key=api_key)


def generate(prompt: str, system: str = "", max_tokens: int = 1500,
             temperature: float = 0.4) -> str:
    """
    Send a single prompt to the LLM and return plain text.
    Used for: zero-shot / one-shot / few-shot / role / meta prompts
    that just need free-text output (e.g. a resume section, feedback text).
    """
    client = _get_client()
    last_error = None

    for attempt in range(MAX_RETRIES + 1):
        try:
            response = client.messages.create(
                model=MODEL_NAME,
                max_tokens=max_tokens,
                temperature=temperature,
                system=system or "You are a precise, helpful assistant.",
                messages=[{"role": "user", "content": prompt}],
            )
            return "".join(
                block.text for block in response.content if block.type == "text"
            ).strip()
        except (APIError, APIConnectionError) as exc:
            last_error = exc
            time.sleep(1.5 * (attempt + 1))

    raise LLMServiceError(f"AI service call failed after retries: {last_error}")


def generate_json(prompt: str, system: str = "", max_tokens: int = 2000,
                   temperature: float = 0.2) -> dict:
    """
    Send a Structured Prompt and parse a strict-JSON response.
    Used for: ATS scoring, interview evaluation, multi-field content output —
    anywhere Response Processing needs a predictable schema, not prose.
    """
    structured_system = (
        (system or "You are a precise assistant.")
        + " Respond with ONLY valid JSON. No markdown fences, no preamble, "
          "no explanation outside the JSON object."
    )
    raw = generate(prompt, system=structured_system, max_tokens=max_tokens,
                    temperature=temperature)

    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        cleaned = cleaned.replace("json\n", "", 1) if cleaned.startswith("json\n") else cleaned

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise LLMServiceError(
            f"AI service returned non-JSON output: {exc}\nRaw output: {raw[:300]}"
        )
