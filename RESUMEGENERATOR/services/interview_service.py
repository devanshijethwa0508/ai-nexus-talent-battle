"""
services/interview_service.py
--------------------------------
Application Logic for Project 2. Implements:

    Generate Question -> Candidate Answers -> AI Evaluation -> Score
        -> Feedback -> Next Question

and the difficulty ramp (Easy -> Medium -> Medium -> Hard -> Hard).
"""

from services.llm_service import generate_json
from prompts.interview_prompts import (
    build_question_generation_prompt,
    build_evaluation_prompt,
    build_interview_summary_prompt,
)

CATEGORY_CYCLE = [
    "Programming", "DSA", "OOP", "Database/SQL", "Projects",
    "Technical Concepts", "Scenario-based",
]
DIFFICULTY_RAMP = ["Easy", "Medium", "Medium", "Hard", "Hard"]


def generate_question(config: dict, question_number: int) -> dict:
    difficulty = DIFFICULTY_RAMP[(question_number - 1) % len(DIFFICULTY_RAMP)]
    category = CATEGORY_CYCLE[(question_number - 1) % len(CATEGORY_CYCLE)]

    return generate_json(
        build_question_generation_prompt(config, question_number, difficulty, category)
    )


def evaluate_answer(question: str, candidate_answer: str, category: str) -> dict:
    result = generate_json(build_evaluation_prompt(question, candidate_answer, category))

    sub_scores = [
        result.get("technical_accuracy", 0),
        result.get("relevance", 0),
        result.get("completeness", 0),
        result.get("clarity", 0),
        result.get("communication", 0),
    ]
    result["overall_score"] = round(sum(sub_scores) / len(sub_scores), 1)
    return result


def build_summary(evaluations: list[dict], config: dict) -> dict:
    return generate_json(build_interview_summary_prompt(evaluations, config))
