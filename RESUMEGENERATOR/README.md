# AI NEXUS 360

Generative AI, Prompt Engineering & AI Application Development — Module 2
Integrated Assignment.

## Problem Statement

Freshers applying to technical roles need three things during a job search
that are usually handled by separate, disconnected tools: a tailored,
ATS-scoring resume; realistic interview practice with real feedback; and
platform-native content for personal branding. AI NEXUS 360 builds all
three as one small GenAI ecosystem sharing a single prompt library and a
single AI service layer.

## Objectives

- Demonstrate all 9 required prompting techniques (Zero-Shot, One-Shot,
  Few-Shot, Role, Structured, Meta, Chain-of-Thought, Tree-of-Thought,
  Prompt Chaining) in real, working code — not just in theory answers.
- Build three working Streamlit applications: Resume Generator, Interview
  Assistant, Content Generator.
- Implement one complete Prompt-Chaining workflow (Resume Optimization
  Chain) where each stage's output is provably the next stage's input.
- Ship a reusable 100-prompt library covering the required categories.

## Technologies Used

- **Python 3.10+**
- **Streamlit** — UI layer, multipage app via `pages/`
- **Anthropic API** (`anthropic` SDK) — the AI/LLM service
- **python-docx** — DOCX resume export
- **python-dotenv** — environment variable loading

## Application Architecture

```
User Interface (Streamlit pages/)
        |
Application Logic (services/*.py)
        |
Prompt Layer (prompts/*.py)
        |
AI/LLM Service (services/llm_service.py -> Anthropic API)
        |
Response Processing (JSON parsing / Markdown section splitting)
        |
Final Output (resume, interview report, content, chained results)
```

Every Streamlit page only imports from `services/`. Every service only
imports prompt builders from `prompts/` and the shared `llm_service`.
No page calls the Anthropic API directly — this is what "Prompt Layer"
and "AI/LLM Service" mean as separate architectural layers, not just a
diagram.

## Project Structure

```
ai-nexus-360/
├── app.py                        # Home page
├── requirements.txt
├── .env.example
├── build_prompt_library.py       # generates prompt_library.md
├── prompt_library.md             # 100 prompts (generated)
├── pages/
│   ├── 1_Resume_Generator.py
│   ├── 2_Interview_Assistant.py
│   ├── 3_Content_Generator.py
│   └── 4_Prompt_Chaining_Demo.py
├── services/
│   ├── llm_service.py            # AI/LLM Service layer
│   ├── resume_service.py
│   ├── interview_service.py
│   ├── content_service.py
│   └── ats_service.py
├── prompts/
│   ├── resume_prompts.py         # Zero/Few-Shot, Role, Structured
│   ├── interview_prompts.py
│   ├── content_prompts.py
│   └── chaining_prompts.py       # CoT, ToT, Meta, Prompt Chaining
└── utils/
    ├── validators.py
    └── export_utils.py
```

## Installation Steps

```bash
git clone <your-repo-url>
cd ai-nexus-360
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Environment Setup

```bash
cp .env.example .env
# then edit .env and set:
# ANTHROPIC_API_KEY=your_key_here
```

Get a key from https://console.anthropic.com/

## How to Run

```bash
streamlit run app.py
```

Regenerate the prompt library if you edit `build_prompt_library.py`:

```bash
python build_prompt_library.py
```

## Features

- **Resume Generator:** structured resume generation, few-shot summary,
  ATS keyword extraction + scoring, improvement suggestions, TXT/DOCX export.
- **Interview Assistant:** role-based adaptive question generation
  (Easy → Medium → Medium → Hard → Hard), 5-parameter scored evaluation,
  strengths/weaknesses feedback, final performance report.
- **Content Generator:** single-platform generation across 7 content
  types and 7 tones, multi-output mode (LinkedIn + Instagram + YouTube +
  hashtags + headlines + CTA in one call), improve/shorten/expand/change
  tone/generate-headline/hashtags/CTA actions.
- **Prompt Chaining Demo:** the full 4-stage Resume Optimization Chain
  with every intermediate output shown.

## Prompt Techniques Used

See `prompt_library.md` for all 100 catalogued prompts. In the running
apps specifically:

| Technique | Where it's used |
|---|---|
| Zero-Shot | ATS keyword extraction |
| Few-Shot | Resume summary generation |
| Role Prompting | Resume writer persona, interviewer persona |
| Structured Prompting | Full resume, interview evaluation JSON, content JSON |
| Meta Prompting | `chaining_prompts.build_meta_prompt()` |
| Chain-of-Thought | `chaining_prompts.build_cot_prompt()` (project consistency check) |
| Tree-of-Thought | `chaining_prompts.build_tot_prompt()` (bullet-point branching) |
| Prompt Chaining | Resume Optimization Chain (4 stages) |

## Sample Input

```
Full Name: Devanshi
Target Role: Embedded Systems Engineer
Technical Skills: C, Embedded C, STM32, RTOS, Python
Job Description: "Looking for an embedded engineer with STM32, RTOS, and
low-power design experience..."
```

## Sample Output

```
ATS Score: 78%
Matched Keywords: ✓ STM32 ✓ RTOS ✓ C
Missing Keywords: ✗ Low-power design ✗ CAN bus
```

(exact figures vary per run since output is LLM-generated)

## Limitations

- ATS keyword matching is substring-based, not semantic (see Q15 in the
  theory answers for why this is a deliberate simplification, not an oversight).
- No persistent database — session state resets when the Streamlit app restarts.
- Requires a live Anthropic API key; there is no offline/mock mode.
- Interview question generation does not currently prevent topic repeats
  across a session.

## Future Enhancements

- Add semantic ATS matching using embeddings instead of substring match.
- Persist resumes/interview history to a database per user.
- Add a PDF export path alongside TXT/DOCX.
- Add a settings page to swap models or adjust temperature per module.

## Screenshots

Screenshots of the running application (UI, resume generation, ATS score,
interview flow, content generation, prompt chaining) should be added here
after running `streamlit run app.py` locally, as required by the submission
checklist.
