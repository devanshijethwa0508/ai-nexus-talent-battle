"""
prompts/chaining_prompts.py
-----------------------------
Demonstrates the Integrated Prompt-Chaining Task and the remaining
required techniques that don't live naturally inside one project:
CHAIN-OF-THOUGHT, TREE-OF-THOUGHT, and META PROMPTING.

RESUME OPTIMIZATION CHAIN
--------------------------
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

Each stage's prompt is built using ONLY the previous stage's output --
never the raw job description re-sent from scratch -- so the chain is a
genuine pipeline, not one large prompt split into four calls.
"""

from services.llm_service import generate


# --- Stage 1 -----------------------------------------------------------
def prompt_1_extract_required_skills(job_description: str) -> str:
    return f"""
Extract the required technical skills from this job description as a
comma-separated list, ordered by how central each skill is to the role.

Job Description:
{job_description}
"""


# --- Stage 2 -------------------------------------------------------------
def prompt_2_analyze_skill_gap(required_skills: str, candidate_skills: str) -> str:
    return f"""
Required skills for the role: {required_skills}
Candidate's current skills: {candidate_skills}

Compare the two lists and return only the skills present in "Required" but
missing (or weak) in "Candidate", as a comma-separated list. If none are
missing, return "None".
"""


# --- Stage 3 ---------------------------------------------------------------
def prompt_3_generate_recommendations(skill_gap: str) -> str:
    return f"""
A candidate is missing these skills relative to a target job: {skill_gap}

Generate 4-5 short, practical recommendations for how the candidate should
address this gap in their resume RIGHT NOW using only truthful reframing
(e.g. highlighting adjacent experience) -- do not suggest lying about skills
they don't have. Return as a plain bullet list.
"""


# --- Stage 4 -----------------------------------------------------------------
def prompt_4_optimize_resume(draft_resume: str, recommendations: str) -> str:
    return f"""
Here is a draft resume:
{draft_resume}

Apply these recommendations to improve it, without inventing any new facts,
employers, or metrics:
{recommendations}

Return the full optimized resume in the same section structure as the draft.
"""


def run_resume_optimization_chain(job_description: str, candidate_skills: str,
                                   draft_resume: str) -> dict:
    """Runs all four stages in sequence, feeding each output into the next prompt."""
    output_1_required_skills = generate(prompt_1_extract_required_skills(job_description))
    output_2_skill_gap = generate(
        prompt_2_analyze_skill_gap(output_1_required_skills, candidate_skills)
    )
    output_3_recommendations = generate(
        prompt_3_generate_recommendations(output_2_skill_gap)
    )
    final_resume = generate(
        prompt_4_optimize_resume(draft_resume, output_3_recommendations)
    )

    return {
        "output_1_required_skills": output_1_required_skills,
        "output_2_skill_gap": output_2_skill_gap,
        "output_3_recommendations": output_3_recommendations,
        "final_resume": final_resume,
    }


# ---------------------------------------------------------------------------
# CHAIN-OF-THOUGHT PROMPTING
# Asks the model to reason step by step before answering -- used here to
# judge whether a candidate's project claim is technically consistent.
# ---------------------------------------------------------------------------
def build_cot_prompt(project_description: str) -> str:
    return f"""
A candidate describes a project as follows:
"{project_description}"

Think step by step:
1. What technologies does this project imply are required?
2. Does the described scope match the complexity of those technologies?
3. Are there any red flags (buzzwords with no supporting detail)?
Then give a final verdict: "Consistent" or "Needs more detail", with one
sentence of justification.
"""


# ---------------------------------------------------------------------------
# TREE-OF-THOUGHT PROMPTING
# Explores multiple candidate framings in parallel before picking the best,
# instead of committing to the first line of reasoning (as CoT does).
# ---------------------------------------------------------------------------
def build_tot_prompt(achievement_raw: str) -> str:
    return f"""
A candidate has this raw achievement note: "{achievement_raw}"

Generate THREE different ways to phrase this as a resume bullet point,
each taking a different angle:
  Branch A: Emphasize technical depth.
  Branch B: Emphasize measurable business/user impact.
  Branch C: Emphasize collaboration/leadership.

For each branch, write the bullet, then rate it 1-10 for "resume strength".
Finally, state which branch you'd recommend and why.
"""


# ---------------------------------------------------------------------------
# META PROMPTING
# A prompt whose job is to generate or improve another prompt.
# ---------------------------------------------------------------------------
def build_meta_prompt(task_description: str) -> str:
    return f"""
You are a prompt engineering expert. Design an effective LLM prompt for the
following task. Your output must be a ready-to-use prompt (not the task
performed) that includes: a role, clear task instructions, constraints,
and an explicit output format.

Task the new prompt must accomplish:
{task_description}

Return only the new prompt text.
"""
