"""
prompts/content_prompts.py
-----------------------------
Prompt Layer for Project 3 (AI Content Generator).
"""

PLATFORM_GUIDANCE = {
    "LinkedIn Post": "Professional network. 150-250 words, line breaks for "
                      "readability, end with a soft question or CTA, 3-5 hashtags.",
    "Instagram Caption": "Casual, visual-first. 1-3 short sentences, emojis "
                          "welcome, hashtags at the end (5-8).",
    "YouTube Description": "First 2 lines act as the search/preview hook. "
                            "Include a brief summary, then bullet timestamps placeholder.",
    "Blog": "Structured long-form with an intro, 2-4 subheadings, and a conclusion.",
    "Technical Article": "Precise and structured, code-comfortable audience, "
                          "may include a short code-style example described in prose.",
    "Email": "Subject line + short body, one clear call to action.",
    "Tweet/X Post": "Under 280 characters, punchy, at most 2 hashtags.",
}


def build_content_prompt(request: dict) -> str:
    """STRUCTURED PROMPT with platform-specific constraints injected."""
    content_type = request.get("content_type")
    guidance = PLATFORM_GUIDANCE.get(content_type, "Adapt naturally to the platform.")

    return f"""
ROLE:
You are a content strategist who writes platform-native copy -- never a
generic paragraph copy-pasted across platforms.

TASK:
Write a {content_type} on the topic below.

TOPIC: {request.get('topic')}
TARGET AUDIENCE: {request.get('audience')}
TONE: {request.get('tone')}
KEYWORDS TO INCLUDE: {request.get('keywords')}
DESIRED LENGTH: {request.get('length')}

PLATFORM RULES FOR {content_type}:
{guidance}

OUTPUT REQUIREMENTS:
Return only the finished {content_type} text, nothing else.
"""


def build_multi_output_prompt(topic: str, audience: str, tone: str) -> str:
    """
    STRUCTURED + FEW-SHOT hybrid: fixed JSON schema so the six outputs the
    assignment asks for (Requirement 6) come back as one machine-parseable
    call instead of six separate free-text calls.
    """
    return f"""
ROLE: You are a multi-platform content strategist.

TASK:
For the single topic below, generate all of the following, each adapted
to its platform's norms (do not reuse the same sentences across formats):

TOPIC: {topic}
AUDIENCE: {audience}
TONE: {tone}

OUTPUT FORMAT (strict JSON):
{{
  "linkedin_post": "...",
  "instagram_caption": "...",
  "youtube_description": "...",
  "hashtags": ["#tag1", "#tag2", "#tag3", "#tag4", "#tag5"],
  "headlines": ["headline1", "headline2", "headline3"],
  "cta": "..."
}}
"""


def build_transform_prompt(content: str, action: str, extra: str = "") -> str:
    """
    ZERO-SHOT PROMPT for Requirement 5 (Improve / Shorten / Expand / Change
    Tone / Generate Headline / Generate Hashtags / Generate CTA).
    `action` and `extra` are supplied by the UI's action buttons.
    """
    action_instructions = {
        "improve": "Improve the clarity, flow and persuasiveness of this content.",
        "shorten": "Shorten this content by roughly half while keeping the key message.",
        "expand": "Expand this content with more detail and examples.",
        "change_tone": f"Rewrite this content in a {extra} tone.",
        "generate_headline": "Generate 3 punchy headline options for this content.",
        "generate_hashtags": "Generate 5 relevant hashtags for this content.",
        "generate_cta": "Generate one strong call-to-action for this content.",
    }
    instruction = action_instructions.get(action, "Improve this content.")

    return f"""
{instruction}

CONTENT:
{content}

Return only the result, no preamble.
"""
