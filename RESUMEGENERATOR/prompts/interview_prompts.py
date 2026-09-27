"""
prompts/interview_prompts.py
------------------------------
Prompt Layer for Project 2 (AI Interview Assistant).
"""

INTERVIEWER_ROLE_PROMPT = (
    "You are a senior technical interviewer at a product-based company. "
    "You ask precise, role-relevant questions and evaluate answers strictly "
    "but fairly, the way a real panel would."
)


def build_question_generation_prompt(config: dict, question_number: int,
                                      difficulty: str, category: str) -> str:
    """STRUCTURED PROMPT: fixed fields drive deterministic difficulty/category."""
    return f"""
ROLE: {INTERVIEWER_ROLE_PROMPT}

TASK:
Generate ONE interview question for this candidate profile.

CANDIDATE PROFILE:
Target Role: {config.get('target_role')}
Experience Level: {config.get('experience_level')}
Domain: {config.get('domain')}
Interview Type: {config.get('interview_type')}

QUESTION SPEC:
Question Number: {question_number}
Category: {category}
Difficulty: {difficulty}

OUTPUT FORMAT (strict JSON):
{{"question": "...", "category": "{category}", "difficulty": "{difficulty}"}}
"""


def build_evaluation_prompt(question: str, candidate_answer: str, category: str) -> str:
    """
    STRUCTURED PROMPT producing scored, structured evaluation --
    Requirement 5 (Answer Evaluation) needs numeric sub-scores, not prose.
    """
    return f"""
ROLE: {INTERVIEWER_ROLE_PROMPT}

TASK:
Evaluate the candidate's answer to the interview question below.

QUESTION ({category}): {question}
CANDIDATE ANSWER: {candidate_answer}

Score each parameter from 0-10:
- technical_accuracy
- relevance
- completeness
- clarity
- communication

Also list strengths (max 3), weaknesses (max 3), and one suggested_improvement.

OUTPUT FORMAT (strict JSON):
{{
  "technical_accuracy": 0,
  "relevance": 0,
  "completeness": 0,
  "clarity": 0,
  "communication": 0,
  "overall_score": 0.0,
  "strengths": ["..."],
  "weaknesses": ["..."],
  "suggested_improvement": "..."
}}
"""


def build_interview_summary_prompt(evaluations: list[dict], config: dict) -> str:
    """FEW-SHOT-flavored structured prompt: shows the exact target shape inline."""
    return f"""
ROLE: {INTERVIEWER_ROLE_PROMPT}

TASK:
Summarize this candidate's full interview performance for a {config.get('target_role')}
({config.get('experience_level')}) role.

PER-QUESTION EVALUATIONS (JSON):
{evaluations}

OUTPUT FORMAT (strict JSON), matching this shape exactly:
{{
  "questions_attempted": 0,
  "average_score": 0.0,
  "strong_areas": ["..."],
  "weak_areas": ["..."],
  "overall_recommendation": "One or two sentences of actionable advice."
}}
"""
