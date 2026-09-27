# AI NEXUS 360 — Prompt Library

100 reusable prompts across the 10 required categories, drawn from the
domains this ecosystem actually uses: resumes, interviews, content,
and Devanshi's core technical areas (embedded systems, telecom, data science).

## Distribution

| Category | Count |
|---|---|
| Zero-Shot | 11 |
| One-Shot | 11 |
| Few-Shot | 11 |
| Role Prompting | 11 |
| Structured Prompting | 12 |
| Meta Prompting | 11 |
| Chain-of-Thought | 11 |
| Tree-of-Thought | 11 |
| Prompt Chaining | 11 |
| Domain-specific AI Prompts | 10 |
| **Total** | **100** |

---

### P001
- **Category:** Prompt Engineering
- **Technique:** Zero-Shot
- **Domain:** Resume Writing
- **Objective:** Extract ATS keywords from a job description.
- **Prompt:**
  ```
  Extract the top 15 technical keywords an ATS would scan for in this job description. Return a comma-separated list only.
  
  Job Description: {job_description}
  ```
- **Expected Output:** A comma-separated keyword list, no extra text.

### P002
- **Category:** Prompt Engineering
- **Technique:** Zero-Shot
- **Domain:** Interview Prep
- **Objective:** Generate a technical interview question.
- **Prompt:**
  ```
  Generate one medium-difficulty technical interview question for a {role} candidate on the topic of {topic}.
  ```
- **Expected Output:** A single, clearly worded interview question.

### P003
- **Category:** Prompt Engineering
- **Technique:** Zero-Shot
- **Domain:** Content Creation
- **Objective:** Write a LinkedIn post from a topic.
- **Prompt:**
  ```
  Write a 150-word LinkedIn post about {topic} for an audience of {audience}. Professional tone.
  ```
- **Expected Output:** A ready-to-post LinkedIn caption.

### P004
- **Category:** Prompt Engineering
- **Technique:** Zero-Shot
- **Domain:** Career Guidance
- **Objective:** Summarize a job description into requirements.
- **Prompt:**
  ```
  Summarize this job description into 5 bullet points covering the core responsibilities.
  
  {job_description}
  ```
- **Expected Output:** 5 bullet points.

### P005
- **Category:** Prompt Engineering
- **Technique:** Zero-Shot
- **Domain:** Embedded Systems
- **Objective:** Explain a hardware concept plainly.
- **Prompt:**
  ```
  Explain what a watchdog timer does in an embedded system, in 3 sentences, for a fresher audience.
  ```
- **Expected Output:** 3-sentence plain-language explanation.

### P006
- **Category:** Prompt Engineering
- **Technique:** Zero-Shot
- **Domain:** Data Science
- **Objective:** Explain a metric.
- **Prompt:**
  ```
  Explain the difference between precision and recall in 100 words, with one real-world analogy.
  ```
- **Expected Output:** 100-word explanation with an analogy.

### P007
- **Category:** Prompt Engineering
- **Technique:** Zero-Shot
- **Domain:** Telecom
- **Objective:** Summarize a protocol.
- **Prompt:**
  ```
  Summarize how the SIP protocol establishes a VoIP call, in 5 steps.
  ```
- **Expected Output:** A 5-step numbered summary.

### P008
- **Category:** Prompt Engineering
- **Technique:** Zero-Shot
- **Domain:** Email Writing
- **Objective:** Draft a follow-up email.
- **Prompt:**
  ```
  Write a polite follow-up email to a recruiter one week after submitting an application for {role}, keeping it under 100 words.
  ```
- **Expected Output:** A complete, ready-to-send email under 100 words.

### P009
- **Category:** Prompt Engineering
- **Technique:** Zero-Shot
- **Domain:** Code Review
- **Objective:** Identify an issue in a code snippet.
- **Prompt:**
  ```
  Review this Python function and list any bugs or edge cases it misses:
  
  {code}
  ```
- **Expected Output:** A bullet list of issues found.

### P010
- **Category:** Prompt Engineering
- **Technique:** Zero-Shot
- **Domain:** Content Creation
- **Objective:** Generate hashtags.
- **Prompt:**
  ```
  Generate 5 relevant hashtags for a post about {topic} aimed at {audience}.
  ```
- **Expected Output:** 5 hashtags.

### P011
- **Category:** Prompt Engineering
- **Technique:** One-Shot
- **Domain:** Resume Writing
- **Objective:** Rewrite a bullet point to be achievement-focused.
- **Prompt:**
  ```
  Rewrite resume bullets to be achievement-focused.
  
  Example:
  Before: "Worked on a billing system."
  After: "Built a billing module handling 500+ daily transactions, reducing manual entry errors."
  
  Now rewrite: "Before: {raw_bullet}"
  ```
- **Expected Output:** One rewritten, achievement-focused bullet.
- **Example Input:** Before: Made a website for college fest.
- **Example Output:** After: Built and deployed the college fest website, used by 2,000+ visitors over the event weekend.

### P012
- **Category:** Prompt Engineering
- **Technique:** One-Shot
- **Domain:** Interview Prep
- **Objective:** Generate a follow-up probing question.
- **Prompt:**
  ```
  Given an interview answer, generate one probing follow-up question.
  
  Example:
  Answer: "I used a hashmap to solve it in O(n)."
  Follow-up: "What would you do if the input didn't fit in memory?"
  
  Now generate a follow-up for: "{answer}"
  ```
- **Expected Output:** One follow-up question.
- **Example Input:** Answer: I optimized the query using an index.
- **Example Output:** Follow-up: What tradeoff did adding that index introduce on writes?

### P013
- **Category:** Prompt Engineering
- **Technique:** One-Shot
- **Domain:** Content Creation
- **Objective:** Write a tweet in a target style.
- **Prompt:**
  ```
  Write a tweet under 280 characters in this style.
  
  Example:
  Topic: Debugging
  Tweet: "90% of debugging is admitting the bug is in the line you skipped reading."
  
  Now write one for: "{topic}"
  ```
- **Expected Output:** One tweet under 280 characters.

### P014
- **Category:** Prompt Engineering
- **Technique:** One-Shot
- **Domain:** Email Writing
- **Objective:** Write a thank-you-after-interview email.
- **Prompt:**
  ```
  Write a thank-you email after an interview.
  
  Example:
  Role: Data Analyst
  Email: "Thank you for the conversation today about the Data Analyst role..."
  
  Now write one for: Role: {role}, Interviewer: {interviewer_name}
  ```
- **Expected Output:** A complete thank-you email.

### P015
- **Category:** Prompt Engineering
- **Technique:** One-Shot
- **Domain:** Embedded Systems
- **Objective:** Explain an error code in context.
- **Prompt:**
  ```
  Explain an embedded error code like the example.
  
  Example:
  Code: HAL_TIMEOUT
  Explanation: "The peripheral did not respond within the configured wait time, often due to a clock misconfiguration."
  
  Now explain: {error_code}
  ```
- **Expected Output:** One explanation matching the example's style.

### P016
- **Category:** Prompt Engineering
- **Technique:** One-Shot
- **Domain:** Data Science
- **Objective:** Explain a model choice.
- **Prompt:**
  ```
  Justify a model choice.
  
  Example:
  Problem: Predicting churn with imbalanced classes.
  Justification: "Random Forest is chosen for its robustness to class imbalance when combined with class weighting."
  
  Now justify a model for: {problem}
  ```
- **Expected Output:** One justification.

### P017
- **Category:** Prompt Engineering
- **Technique:** One-Shot
- **Domain:** Telecom
- **Objective:** Summarize an incident report.
- **Prompt:**
  ```
  Summarize a network incident in one sentence.
  
  Example:
  Details: "Cell site X lost backhaul for 40 minutes due to a fiber cut."
  Summary: "40-minute outage at Site X caused by fiber cut."
  
  Now summarize: {incident_details}
  ```
- **Expected Output:** One-sentence summary.

### P018
- **Category:** Prompt Engineering
- **Technique:** One-Shot
- **Domain:** Career Guidance
- **Objective:** Reframe a gap year positively.
- **Prompt:**
  ```
  Reframe a resume gap.
  
  Example:
  Gap: "1 year unemployed after graduation."
  Reframe: "Spent 2025 building independent ML projects and completing two certifications while job hunting."
  
  Now reframe: {gap_description}
  ```
- **Expected Output:** One reframed sentence, no fabricated employer.

### P019
- **Category:** Prompt Engineering
- **Technique:** One-Shot
- **Domain:** Code Review
- **Objective:** Suggest a more Pythonic version of a line.
- **Prompt:**
  ```
  Suggest a Pythonic rewrite.
  
  Example:
  Before: "for i in range(len(lst)): print(lst[i])"
  After: "for item in lst: print(item)"
  
  Now rewrite: "{code_line}"
  ```
- **Expected Output:** One rewritten line.

### P020
- **Category:** Prompt Engineering
- **Technique:** One-Shot
- **Domain:** Content Creation
- **Objective:** Write an Instagram caption in a target voice.
- **Prompt:**
  ```
  Write an Instagram caption.
  
  Example:
  Topic: Internship offer
  Caption: "Said yes before they finished the sentence. Onward. 🚀"
  
  Now write one for: {topic}
  ```
- **Expected Output:** One caption with emoji.

### P021
- **Category:** Prompt Engineering
- **Technique:** Few-Shot
- **Domain:** Resume Writing
- **Objective:** Generate a Professional Summary from candidate facts.
- **Prompt:**
  ```
  Write a resume summary, following these examples' tone.
  
  Example 1: Input: Fresher, CSE, Django/Postgres, billing dashboard. Output: "CS graduate experienced in full-stack billing dashboards using Django and PostgreSQL, focused on shippable, testable code."
  Example 2: Input: Fresher, ECE, STM32/RTOS, sensor fusion. Output: "Electronics graduate specializing in embedded firmware, from register-level drivers to real-time scheduling."
  
  Now write for: {candidate_facts}
  ```
- **Expected Output:** One 2-3 sentence summary matching the examples' register.

### P022
- **Category:** Prompt Engineering
- **Technique:** Few-Shot
- **Domain:** Interview Prep
- **Objective:** Score an interview answer 1-10.
- **Prompt:**
  ```
  Score interview answers 1-10 for technical accuracy.
  
  Example 1: Answer: "Uses O(n log n) sort then binary search." Score: 9
  Example 2: Answer: "I'd just try stuff until it works." Score: 2
  Example 3: Answer: "Two-pointer approach after sorting, O(n log n) overall." Score: 8
  
  Now score: "{answer}"
  ```
- **Expected Output:** A single integer 1-10 with one-line justification.

### P023
- **Category:** Prompt Engineering
- **Technique:** Few-Shot
- **Domain:** Content Creation
- **Objective:** Generate a headline in a proven style.
- **Prompt:**
  ```
  Write a headline.
  
  Example 1: Topic: AI in healthcare -> "The Algorithm Will See You Now"
  Example 2: Topic: remote work -> "Home Is Where The Standup Is"
  Example 3: Topic: cybersecurity -> "Trust No Click"
  
  Now write one for: {topic}
  ```
- **Expected Output:** One punchy headline, same style/length.

### P024
- **Category:** Prompt Engineering
- **Technique:** Few-Shot
- **Domain:** Data Science
- **Objective:** Classify a bug report's severity.
- **Prompt:**
  ```
  Classify severity as Low/Medium/High.
  
  Example 1: "Typo in footer." -> Low
  Example 2: "Login fails for 10% of users." -> High
  Example 3: "Chart colors slightly off-brand." -> Low
  Example 4: "Checkout crashes for Safari users." -> High
  
  Now classify: "{bug_report}"
  ```
- **Expected Output:** One severity label with reasoning.

### P025
- **Category:** Prompt Engineering
- **Technique:** Few-Shot
- **Domain:** Telecom
- **Objective:** Categorize a network fault.
- **Prompt:**
  ```
  Categorize the fault type.
  
  Example 1: "BTS unreachable, power alarm active" -> Power Fault
  Example 2: "High packet loss on backhaul link" -> Transmission Fault
  Example 3: "Cell showing degraded RSSI" -> RF Fault
  
  Now categorize: "{fault_description}"
  ```
- **Expected Output:** One category label.

### P026
- **Category:** Prompt Engineering
- **Technique:** Few-Shot
- **Domain:** Email Writing
- **Objective:** Write a negotiation email in a firm-but-polite tone.
- **Prompt:**
  ```
  Write a salary negotiation email.
  
  Example 1: Offer: 6 LPA, target 7.2 LPA -> polite, cites market data, no ultimatums.
  Example 2: Offer: 8 LPA, target 8.5 LPA -> polite, cites a competing offer.
  
  Now write for: Offer {offer}, target {target}
  ```
- **Expected Output:** One complete email in the same tone.

### P027
- **Category:** Prompt Engineering
- **Technique:** Few-Shot
- **Domain:** Embedded Systems
- **Objective:** Diagnose a likely cause from symptoms.
- **Prompt:**
  ```
  Diagnose the likely cause.
  
  Example 1: "MCU resets randomly under load" -> brown-out from insufficient decoupling.
  Example 2: "UART receives garbage bytes" -> baud rate mismatch.
  
  Now diagnose: "{symptom}"
  ```
- **Expected Output:** One likely cause with brief reasoning.

### P028
- **Category:** Prompt Engineering
- **Technique:** Few-Shot
- **Domain:** Career Guidance
- **Objective:** Match a project to a job requirement.
- **Prompt:**
  ```
  Match a project to a JD requirement, in one sentence.
  
  Example 1: Requirement: "Experience with REST APIs" + Project: "Built a Flask API for a todo app" -> "Directly demonstrates REST API design and implementation."
  
  Now match: Requirement: {requirement}, Project: {project}
  ```
- **Expected Output:** One matching sentence.

### P029
- **Category:** Prompt Engineering
- **Technique:** Few-Shot
- **Domain:** Code Review
- **Objective:** Flag a security issue in code.
- **Prompt:**
  ```
  Flag security issues.
  
  Example 1: "query = f'SELECT * WHERE id={user_input}'" -> SQL injection risk, use parameterized queries.
  Example 2: "password stored in plaintext" -> hash with bcrypt/argon2.
  
  Now review: "{code_snippet}"
  ```
- **Expected Output:** Issue name + one-line fix.

### P030
- **Category:** Prompt Engineering
- **Technique:** Few-Shot
- **Domain:** Content Creation
- **Objective:** Write a CTA matching examples.
- **Prompt:**
  ```
  Write a call-to-action.
  
  Example 1: Topic: new blog post -> "Read the full breakdown →"
  Example 2: Topic: webinar -> "Save your seat before it fills up."
  
  Now write one for: {topic}
  ```
- **Expected Output:** One short CTA line.

### P031
- **Category:** Prompt Engineering
- **Technique:** Role Prompting
- **Domain:** Resume Writing
- **Objective:** Act as a recruiter to critique a resume.
- **Prompt:**
  ```
  You are a senior technical recruiter who has screened 5,000+ resumes. Critique this resume for a {role} position, focusing on what would get it rejected in a 10-second scan.
  
  {resume_text}
  ```
- **Expected Output:** A blunt, recruiter-style critique.

### P032
- **Category:** Prompt Engineering
- **Technique:** Role Prompting
- **Domain:** Interview Prep
- **Objective:** Act as a strict panel interviewer.
- **Prompt:**
  ```
  You are a strict, no-nonsense panel interviewer at a top product company. Ask one hard follow-up question that exposes shallow understanding, based on this answer: "{answer}"
  ```
- **Expected Output:** One incisive follow-up question.

### P033
- **Category:** Prompt Engineering
- **Technique:** Role Prompting
- **Domain:** Content Creation
- **Objective:** Act as a copywriter for a specific brand voice.
- **Prompt:**
  ```
  You are a witty, Gen-Z-savvy social media copywriter. Write an Instagram caption about {topic} in that voice.
  ```
- **Expected Output:** One caption in the specified voice.

### P034
- **Category:** Prompt Engineering
- **Technique:** Role Prompting
- **Domain:** Data Science
- **Objective:** Act as a skeptical peer reviewer.
- **Prompt:**
  ```
  You are a skeptical ML peer reviewer. Point out three ways this experiment's results could be misleading: {experiment_summary}
  ```
- **Expected Output:** 3 skeptical points.

### P035
- **Category:** Prompt Engineering
- **Technique:** Role Prompting
- **Domain:** Telecom
- **Objective:** Act as a network operations engineer.
- **Prompt:**
  ```
  You are a telecom NOC engineer during an active outage. Given this alarm log, state the single most likely root cause and the first diagnostic step you'd take.
  
  {alarm_log}
  ```
- **Expected Output:** One root-cause hypothesis + one next step.

### P036
- **Category:** Prompt Engineering
- **Technique:** Role Prompting
- **Domain:** Embedded Systems
- **Objective:** Act as a hardware bring-up engineer.
- **Prompt:**
  ```
  You are a hardware bring-up engineer debugging a new board. Given this symptom, list the first three things you'd check on the board.
  
  Symptom: {symptom}
  ```
- **Expected Output:** 3 concrete checks, hardware-first.

### P037
- **Category:** Prompt Engineering
- **Technique:** Role Prompting
- **Domain:** Career Guidance
- **Objective:** Act as a career coach for freshers.
- **Prompt:**
  ```
  You are a career coach specializing in placing fresh engineering graduates. Given this profile, name the single biggest gap holding back their applications.
  
  {profile_summary}
  ```
- **Expected Output:** One specific, honest gap.

### P038
- **Category:** Prompt Engineering
- **Technique:** Role Prompting
- **Domain:** Code Review
- **Objective:** Act as a strict senior engineer doing code review.
- **Prompt:**
  ```
  You are a strict senior engineer reviewing a junior's pull request. List every issue you'd block the PR on, in order of severity.
  
  {code_diff}
  ```
- **Expected Output:** A severity-ordered issue list.

### P039
- **Category:** Prompt Engineering
- **Technique:** Role Prompting
- **Domain:** Email Writing
- **Objective:** Act as an HR professional drafting a rejection.
- **Prompt:**
  ```
  You are an HR professional. Write a respectful, encouraging rejection email for a candidate who interviewed well but was not selected for {role}.
  ```
- **Expected Output:** One complete, respectful email.

### P040
- **Category:** Prompt Engineering
- **Technique:** Role Prompting
- **Domain:** Content Creation
- **Objective:** Act as a technical educator explaining to beginners.
- **Prompt:**
  ```
  You are a patient technical educator. Explain {concept} to someone with zero background, using one everyday analogy.
  ```
- **Expected Output:** A beginner-friendly explanation with an analogy.

### P041
- **Category:** Prompt Engineering
- **Technique:** Structured Prompting
- **Domain:** Resume Writing
- **Objective:** Generate a full resume with fixed sections.
- **Prompt:**
  ```
  ROLE: Expert resume writer.
  CONTEXT: {candidate_context}
  TASK: Write Professional Summary, Technical Skills, Experience, Projects, Education sections.
  CONSTRAINTS: Do not invent facts.
  OUTPUT FORMAT: Markdown headings (##), nothing else.
  ```
- **Expected Output:** A resume in the exact 5-section Markdown structure.

### P042
- **Category:** Prompt Engineering
- **Technique:** Structured Prompting
- **Domain:** Interview Prep
- **Objective:** Generate a scored evaluation as JSON.
- **Prompt:**
  ```
  ROLE: Technical interviewer.
  TASK: Score this answer.
  INPUT: Question: {question}, Answer: {answer}
  OUTPUT FORMAT (strict JSON): {{"technical_accuracy":0,"clarity":0,"overall_score":0.0}}
  ```
- **Expected Output:** Valid JSON matching the exact schema, no extra text.

### P043
- **Category:** Prompt Engineering
- **Technique:** Structured Prompting
- **Domain:** Content Creation
- **Objective:** Generate multi-platform content as JSON.
- **Prompt:**
  ```
  ROLE: Content strategist.
  TASK: Generate LinkedIn post, tweet, and 3 hashtags for {topic}.
  OUTPUT FORMAT (strict JSON): {{"linkedin":"","tweet":"","hashtags":[]}}
  ```
- **Expected Output:** Valid JSON with exactly those three keys.

### P044
- **Category:** Prompt Engineering
- **Technique:** Structured Prompting
- **Domain:** Data Science
- **Objective:** Generate a model comparison table.
- **Prompt:**
  ```
  ROLE: ML consultant.
  TASK: Compare {model_a} vs {model_b} for {use_case}.
  OUTPUT FORMAT: A Markdown table with columns: Criterion | {model_a} | {model_b}.
  ```
- **Expected Output:** A well-formed Markdown table.

### P045
- **Category:** Prompt Engineering
- **Technique:** Structured Prompting
- **Domain:** Telecom
- **Objective:** Generate an incident report in a fixed template.
- **Prompt:**
  ```
  TASK: Fill this incident template from the raw notes.
  TEMPLATE: Incident ID / Start Time / End Time / Root Cause / Impact / Resolution
  RAW NOTES: {raw_notes}
  OUTPUT FORMAT: Field: Value, one per line, in that exact order.
  ```
- **Expected Output:** 6 lines, one field per line, in order.

### P046
- **Category:** Prompt Engineering
- **Technique:** Structured Prompting
- **Domain:** Embedded Systems
- **Objective:** Generate a register configuration checklist.
- **Prompt:**
  ```
  TASK: List the register configuration steps to enable {peripheral} on {mcu}.
  OUTPUT FORMAT: Numbered list, one register/bit per step, no prose paragraphs.
  ```
- **Expected Output:** A numbered, register-level checklist.

### P047
- **Category:** Prompt Engineering
- **Technique:** Structured Prompting
- **Domain:** Career Guidance
- **Objective:** Generate a 30-60-90 day plan.
- **Prompt:**
  ```
  TASK: Create a 30-60-90 day plan for a fresher starting as {role}.
  OUTPUT FORMAT (strict JSON): {{"30_days":[],"60_days":[],"90_days":[]}}
  ```
- **Expected Output:** Valid JSON with three array fields.

### P048
- **Category:** Prompt Engineering
- **Technique:** Structured Prompting
- **Domain:** Code Review
- **Objective:** Generate a review report with fixed fields.
- **Prompt:**
  ```
  TASK: Review this code: {code}
  OUTPUT FORMAT: Bugs: <list>\nStyle Issues: <list>\nSecurity Issues: <list>\nVerdict: Approve/Request Changes
  ```
- **Expected Output:** Exactly those four labeled sections.

### P049
- **Category:** Prompt Engineering
- **Technique:** Structured Prompting
- **Domain:** Email Writing
- **Objective:** Generate a structured cold outreach email.
- **Prompt:**
  ```
  TASK: Write a cold outreach email to {recipient_role} about {ask}.
  OUTPUT FORMAT: Subject: <one line>\nBody: <email body>
  ```
- **Expected Output:** Exactly a Subject line and a Body.

### P050
- **Category:** Prompt Engineering
- **Technique:** Structured Prompting
- **Domain:** Content Creation
- **Objective:** Generate a content calendar as JSON.
- **Prompt:**
  ```
  TASK: Create a 5-day content calendar on {theme}.
  OUTPUT FORMAT (strict JSON): [{{"day":1,"platform":"","topic":""}}, ...]
  ```
- **Expected Output:** A JSON array of 5 objects with those three keys.

### P051
- **Category:** Prompt Engineering
- **Technique:** Meta Prompting
- **Domain:** Resume Writing
- **Objective:** Design a prompt for resume bullet rewriting.
- **Prompt:**
  ```
  Design an effective prompt for the task: 'rewrite a weak resume bullet into an achievement-focused one, without inventing metrics.' Include role, constraints, and output format.
  ```
- **Expected Output:** A ready-to-use prompt, not the rewritten bullet itself.

### P052
- **Category:** Prompt Engineering
- **Technique:** Meta Prompting
- **Domain:** Interview Prep
- **Objective:** Design a prompt for adaptive question difficulty.
- **Prompt:**
  ```
  Design a prompt that generates the NEXT interview question, harder or easier depending on how well the previous answer scored. Include the scoring input format.
  ```
- **Expected Output:** A ready-to-use adaptive-difficulty prompt template.

### P053
- **Category:** Prompt Engineering
- **Technique:** Meta Prompting
- **Domain:** Content Creation
- **Objective:** Design a prompt for platform-adapted content.
- **Prompt:**
  ```
  Design a prompt that takes one topic and produces genuinely different copy per platform (LinkedIn vs Instagram vs Twitter), not the same text reused.
  ```
- **Expected Output:** A ready-to-use multi-platform prompt template.

### P054
- **Category:** Prompt Engineering
- **Technique:** Meta Prompting
- **Domain:** Data Science
- **Objective:** Improve a vague data-analysis prompt.
- **Prompt:**
  ```
  Here is a weak prompt: "analyze this data." Rewrite it into a strong, structured prompt that specifies the analysis goal, expected output format, and constraints.
  ```
- **Expected Output:** One improved prompt, not an analysis.

### P055
- **Category:** Prompt Engineering
- **Technique:** Meta Prompting
- **Domain:** Telecom
- **Objective:** Design a prompt for root-cause analysis from logs.
- **Prompt:**
  ```
  Design a prompt for extracting a single root cause from noisy telecom alarm logs, specifying what counts as 'root cause' vs 'symptom' in the instructions.
  ```
- **Expected Output:** One ready-to-use RCA prompt.

### P056
- **Category:** Prompt Engineering
- **Technique:** Meta Prompting
- **Domain:** Embedded Systems
- **Objective:** Design a prompt for datasheet-grounded answers.
- **Prompt:**
  ```
  Design a prompt that forces an LLM to answer embedded hardware questions ONLY using facts from a provided datasheet excerpt, refusing to guess otherwise.
  ```
- **Expected Output:** One ready-to-use grounded-QA prompt.

### P057
- **Category:** Prompt Engineering
- **Technique:** Meta Prompting
- **Domain:** Career Guidance
- **Objective:** Design a prompt for honest gap analysis.
- **Prompt:**
  ```
  Design a prompt that compares a candidate's resume to a job description and honestly flags gaps, avoiding generic flattery. Specify tone constraints explicitly.
  ```
- **Expected Output:** One ready-to-use gap-analysis prompt.

### P058
- **Category:** Prompt Engineering
- **Technique:** Meta Prompting
- **Domain:** Code Review
- **Objective:** Design a prompt for severity-ranked code review.
- **Prompt:**
  ```
  Design a prompt that reviews code and ranks every issue by severity (blocking / major / minor / nitpick), with a fixed output format.
  ```
- **Expected Output:** One ready-to-use code-review prompt.

### P059
- **Category:** Prompt Engineering
- **Technique:** Meta Prompting
- **Domain:** Email Writing
- **Objective:** Design a prompt for tone-matched email replies.
- **Prompt:**
  ```
  Design a prompt that drafts an email reply matching the formality level of the email it's replying to, inferred automatically rather than asked for.
  ```
- **Expected Output:** One ready-to-use tone-matching prompt.

### P060
- **Category:** Prompt Engineering
- **Technique:** Meta Prompting
- **Domain:** Content Creation
- **Objective:** Improve a prompt for hashtag generation.
- **Prompt:**
  ```
  Here is a weak prompt: "give me hashtags." Rewrite it to specify count, relevance criteria, and platform norms explicitly.
  ```
- **Expected Output:** One improved prompt.

### P061
- **Category:** Prompting Techniques
- **Technique:** Chain-of-Thought
- **Domain:** Resume Writing
- **Objective:** Reason through whether a claim is consistent.
- **Prompt:**
  ```
  A candidate claims: "{claim}". Think step by step about what skills/time this would require, then decide if it's plausible for a fresher. Show your reasoning, then give a final verdict.
  ```
- **Expected Output:** Step-by-step reasoning followed by a verdict.

### P062
- **Category:** Prompting Techniques
- **Technique:** Chain-of-Thought
- **Domain:** Interview Prep
- **Objective:** Solve a DSA problem with visible reasoning.
- **Prompt:**
  ```
  Solve this problem step by step, explaining your reasoning at each step before writing final code: {problem_statement}
  ```
- **Expected Output:** Numbered reasoning steps, then final code.

### P063
- **Category:** Prompting Techniques
- **Technique:** Chain-of-Thought
- **Domain:** Data Science
- **Objective:** Diagnose why a model underperforms.
- **Prompt:**
  ```
  This model's accuracy dropped after deployment: {context}. Think step by step through possible causes (data drift, leakage, label shift, etc.) before concluding the most likely cause.
  ```
- **Expected Output:** Step-by-step elimination, then a conclusion.

### P064
- **Category:** Prompting Techniques
- **Technique:** Chain-of-Thought
- **Domain:** Telecom
- **Objective:** Trace a call-drop root cause.
- **Prompt:**
  ```
  Given these KPIs and alarms: {data}, reason step by step through the call chain (RF -> Transport -> Core) to isolate where the drop most likely occurred.
  ```
- **Expected Output:** A layer-by-layer trace ending in one conclusion.

### P065
- **Category:** Prompting Techniques
- **Technique:** Chain-of-Thought
- **Domain:** Embedded Systems
- **Objective:** Debug a timing issue methodically.
- **Prompt:**
  ```
  An interrupt handler sometimes misses events: {symptom_details}. Reason step by step through timing, priority, and race-condition possibilities before concluding.
  ```
- **Expected Output:** Step-by-step debugging reasoning, then a conclusion.

### P066
- **Category:** Prompting Techniques
- **Technique:** Chain-of-Thought
- **Domain:** Career Guidance
- **Objective:** Decide between two job offers.
- **Prompt:**
  ```
  Compare these two offers step by step across growth, compensation, and learning curve before recommending one: Offer A: {offer_a}, Offer B: {offer_b}
  ```
- **Expected Output:** Step-by-step comparison, then a recommendation.

### P067
- **Category:** Prompting Techniques
- **Technique:** Chain-of-Thought
- **Domain:** Code Review
- **Objective:** Trace through code to find a logic bug.
- **Prompt:**
  ```
  Trace through this function step by step with the input {sample_input} to find where the output diverges from expectations.
  
  {code}
  ```
- **Expected Output:** A step-by-step trace, then the located bug.

### P068
- **Category:** Prompting Techniques
- **Technique:** Chain-of-Thought
- **Domain:** Content Creation
- **Objective:** Plan a content angle before writing.
- **Prompt:**
  ```
  Before writing the post, think step by step: who is the audience, what do they already believe about {topic}, and what's the one new idea worth their time? Then write the post.
  ```
- **Expected Output:** Visible reasoning, then the final post.

### P069
- **Category:** Prompting Techniques
- **Technique:** Chain-of-Thought
- **Domain:** Email Writing
- **Objective:** Decide the right tone before drafting.
- **Prompt:**
  ```
  Before drafting, reason step by step about the relationship and stakes implied by this context: {context}. Then write the email in the tone you concluded.
  ```
- **Expected Output:** Brief reasoning, then the email.

### P070
- **Category:** Prompting Techniques
- **Technique:** Chain-of-Thought
- **Domain:** Data Science
- **Objective:** Choose an evaluation metric methodically.
- **Prompt:**
  ```
  For this problem: {problem_description}, reason step by step about class balance and business cost of false positives/negatives before recommending one evaluation metric.
  ```
- **Expected Output:** Step-by-step reasoning, then one recommended metric.

### P071
- **Category:** Prompting Techniques
- **Technique:** Tree-of-Thought
- **Domain:** Resume Writing
- **Objective:** Explore three bullet-point framings.
- **Prompt:**
  ```
  For this raw achievement: "{achievement}", generate three different bullet framings (technical depth / business impact / leadership), rate each 1-10, then recommend one.
  ```
- **Expected Output:** 3 rated branches + a final recommendation.

### P072
- **Category:** Prompting Techniques
- **Technique:** Tree-of-Thought
- **Domain:** Interview Prep
- **Objective:** Explore multiple solution approaches to a problem.
- **Prompt:**
  ```
  For this problem: {problem}, explore three different algorithmic approaches, note the time/space complexity of each, then recommend the best for an interview setting.
  ```
- **Expected Output:** 3 approaches with complexity, then a recommendation.

### P073
- **Category:** Prompting Techniques
- **Technique:** Tree-of-Thought
- **Domain:** Data Science
- **Objective:** Explore multiple feature-engineering strategies.
- **Prompt:**
  ```
  For predicting {target}, branch into three feature-engineering strategies, evaluate each for likely predictive value and cost to build, then pick one.
  ```
- **Expected Output:** 3 branches evaluated, then a final pick.

### P074
- **Category:** Prompting Techniques
- **Technique:** Tree-of-Thought
- **Domain:** Telecom
- **Objective:** Explore multiple root-cause hypotheses.
- **Prompt:**
  ```
  Given this fault: {fault_description}, branch into three plausible root-cause hypotheses (RF / Transport / Core), evaluate the evidence for each, then pick the most likely.
  ```
- **Expected Output:** 3 hypotheses evaluated, then a conclusion.

### P075
- **Category:** Prompting Techniques
- **Technique:** Tree-of-Thought
- **Domain:** Embedded Systems
- **Objective:** Explore multiple low-power design strategies.
- **Prompt:**
  ```
  For a battery-powered sensor node with {constraints}, branch into three low-power strategies (duty cycling / sleep modes / event-driven wake), evaluate trade-offs, then recommend one.
  ```
- **Expected Output:** 3 branches with trade-offs, then a recommendation.

### P076
- **Category:** Prompting Techniques
- **Technique:** Tree-of-Thought
- **Domain:** Career Guidance
- **Objective:** Explore multiple career-path branches.
- **Prompt:**
  ```
  Given this background: {background}, branch into three plausible next-role paths, evaluate pros/cons of each for a 2-year horizon, then recommend one.
  ```
- **Expected Output:** 3 paths evaluated, then a recommendation.

### P077
- **Category:** Prompting Techniques
- **Technique:** Tree-of-Thought
- **Domain:** Code Review
- **Objective:** Explore multiple refactor strategies.
- **Prompt:**
  ```
  For this code: {code}, branch into three refactor strategies (performance-focused / readability-focused / minimal-diff), evaluate each, then recommend one.
  ```
- **Expected Output:** 3 strategies evaluated, then a recommendation.

### P078
- **Category:** Prompting Techniques
- **Technique:** Tree-of-Thought
- **Domain:** Content Creation
- **Objective:** Explore multiple headline angles.
- **Prompt:**
  ```
  For the topic {topic}, branch into three headline angles (curiosity / benefit / controversy), write one headline per angle, rate each for click potential, then recommend one.
  ```
- **Expected Output:** 3 rated headlines, then a recommendation.

### P079
- **Category:** Prompting Techniques
- **Technique:** Tree-of-Thought
- **Domain:** Email Writing
- **Objective:** Explore multiple negotiation framings.
- **Prompt:**
  ```
  For negotiating {ask}, branch into three framings (data-driven / relationship-based / urgency-based), draft one line for each, then recommend which fits {context} best.
  ```
- **Expected Output:** 3 framings, then a recommendation.

### P080
- **Category:** Prompting Techniques
- **Technique:** Tree-of-Thought
- **Domain:** Resume Writing
- **Objective:** Explore multiple summary openings.
- **Prompt:**
  ```
  For a candidate targeting {role}, branch into three different opening lines for a resume summary, each leading with a different strength, then recommend one.
  ```
- **Expected Output:** 3 opening lines, then a recommendation.

### P081
- **Category:** Prompting Techniques
- **Technique:** Prompt Chaining
- **Domain:** Resume Writing
- **Objective:** Chain: extract skills -> gap -> recommendations -> optimized resume.
- **Prompt:**
  ```
  STAGE 1 of 4: Extract required skills from this job description as a comma-separated list.
  
  {job_description}
  ```
- **Expected Output:** Output feeds Stage 2 (skill-gap analysis).

### P082
- **Category:** Prompting Techniques
- **Technique:** Prompt Chaining
- **Domain:** Resume Writing
- **Objective:** Chain stage 2: analyze skill gap.
- **Prompt:**
  ```
  STAGE 2 of 4: Required skills: {output_1}. Candidate skills: {candidate_skills}. List the missing skills.
  ```
- **Expected Output:** Output feeds Stage 3 (recommendations).

### P083
- **Category:** Prompting Techniques
- **Technique:** Prompt Chaining
- **Domain:** Resume Writing
- **Objective:** Chain stage 3: generate recommendations.
- **Prompt:**
  ```
  STAGE 3 of 4: Missing skills: {output_2}. Generate 4-5 honest ways to address this gap on a resume without fabricating experience.
  ```
- **Expected Output:** Output feeds Stage 4 (final resume).

### P084
- **Category:** Prompting Techniques
- **Technique:** Prompt Chaining
- **Domain:** Resume Writing
- **Objective:** Chain stage 4: optimize final resume.
- **Prompt:**
  ```
  STAGE 4 of 4: Draft resume: {draft_resume}. Recommendations: {output_3}. Apply them and return the optimized resume.
  ```
- **Expected Output:** Final resume output.

### P085
- **Category:** Prompting Techniques
- **Technique:** Prompt Chaining
- **Domain:** Interview Prep
- **Objective:** Chain: question -> answer -> eval -> next question difficulty.
- **Prompt:**
  ```
  STAGE 1: Generate an Easy question for {domain}.
  STAGE 2 (after answer): Evaluate the answer and output a score 0-10.
  STAGE 3: If score >= 7, generate a Medium question next; else generate another Easy question.
  ```
- **Expected Output:** A 3-stage adaptive chain description with explicit branching rule.

### P086
- **Category:** Prompting Techniques
- **Technique:** Prompt Chaining
- **Domain:** Content Creation
- **Objective:** Chain: outline -> draft -> platform adaptation.
- **Prompt:**
  ```
  STAGE 1: Outline 3 key points about {topic}.
  STAGE 2: Expand the outline into a full blog draft.
  STAGE 3: Adapt the blog draft into a LinkedIn post using only its core idea, not its full text.
  ```
- **Expected Output:** 3 chained outputs, each built from the previous.

### P087
- **Category:** Prompting Techniques
- **Technique:** Prompt Chaining
- **Domain:** Data Science
- **Objective:** Chain: EDA summary -> hypothesis -> test plan.
- **Prompt:**
  ```
  STAGE 1: Summarize key patterns in this dataset description: {dataset_summary}.
  STAGE 2: From the patterns, propose one testable hypothesis.
  STAGE 3: Design a statistical test to check that hypothesis.
  ```
- **Expected Output:** 3 chained outputs.

### P088
- **Category:** Prompting Techniques
- **Technique:** Prompt Chaining
- **Domain:** Telecom
- **Objective:** Chain: raw logs -> anomalies -> root cause -> action.
- **Prompt:**
  ```
  STAGE 1: Extract anomalies from this raw log: {raw_log}.
  STAGE 2: Given the anomalies, identify the most likely root cause.
  STAGE 3: Given the root cause, recommend one corrective action.
  ```
- **Expected Output:** 3 chained outputs, each depending on the last.

### P089
- **Category:** Prompting Techniques
- **Technique:** Prompt Chaining
- **Domain:** Career Guidance
- **Objective:** Chain: profile -> gaps -> 90-day plan.
- **Prompt:**
  ```
  STAGE 1: List this candidate's current strengths from {profile}.
  STAGE 2: Compare strengths to {target_role} requirements and list gaps.
  STAGE 3: Turn the gaps into a 90-day upskilling plan.
  ```
- **Expected Output:** 3 chained outputs.

### P090
- **Category:** Prompting Techniques
- **Technique:** Prompt Chaining
- **Domain:** Code Review
- **Objective:** Chain: find bugs -> prioritize -> write fixes.
- **Prompt:**
  ```
  STAGE 1: List all bugs found in {code}.
  STAGE 2: Rank the bugs by severity.
  STAGE 3: Write the fix for only the top-ranked bug.
  ```
- **Expected Output:** 3 chained outputs, each narrowing on the previous.

### P091
- **Category:** Domain-specific AI Prompts
- **Technique:** Structured Prompting
- **Domain:** Embedded Systems
- **Objective:** Generate a peripheral init checklist for a target MCU.
- **Prompt:**
  ```
  List the initialization steps for enabling {peripheral} (e.g. UART, SPI, ADC) on {mcu_family}, in the order a bring-up engineer would perform them.
  ```
- **Expected Output:** A numbered, hardware-accurate checklist.

### P092
- **Category:** Domain-specific AI Prompts
- **Technique:** Few-Shot
- **Domain:** Telecom Core Networks
- **Objective:** Classify a core-network alarm by 3GPP domain.
- **Prompt:**
  ```
  Classify this alarm by domain (RAN / Transport / Core / IMS).
  
  Example 1: "MME path failure" -> Core
  Example 2: "eNB cell down" -> RAN
  
  Now classify: "{alarm_text}"
  ```
- **Expected Output:** One domain label with justification.

### P093
- **Category:** Domain-specific AI Prompts
- **Technique:** Chain-of-Thought
- **Domain:** Data Science / ML
- **Objective:** Reason about overfitting in a specific model.
- **Prompt:**
  ```
  Given train accuracy {train_acc}% and validation accuracy {val_acc}%, reason step by step about whether this indicates overfitting and what to try next.
  ```
- **Expected Output:** Step-by-step reasoning, then a recommendation.

### P094
- **Category:** Domain-specific AI Prompts
- **Technique:** Role Prompting
- **Domain:** Instrumentation
- **Objective:** Act as a calibration engineer.
- **Prompt:**
  ```
  You are an instrumentation calibration engineer. Given this sensor drift data: {drift_data}, state whether recalibration is due and why.
  ```
- **Expected Output:** One clear yes/no with justification.

### P095
- **Category:** Domain-specific AI Prompts
- **Technique:** Structured Prompting
- **Domain:** Placements / Job Search
- **Objective:** Generate a weekly job-search tracker entry.
- **Prompt:**
  ```
  TASK: Turn this raw update into a tracker row.
  RAW UPDATE: {raw_update}
  OUTPUT FORMAT: Company | Role | Stage | Next Action | Date
  ```
- **Expected Output:** One pipe-delimited row.

### P096
- **Category:** Domain-specific AI Prompts
- **Technique:** Zero-Shot
- **Domain:** IEEE / Research Writing
- **Objective:** Tighten an abstract to a word limit.
- **Prompt:**
  ```
  Rewrite this abstract to fit within {word_limit} words while keeping the core contribution and results intact.
  
  {abstract_text}
  ```
- **Expected Output:** A rewritten abstract at or under the word limit.

### P097
- **Category:** Domain-specific AI Prompts
- **Technique:** Meta Prompting
- **Domain:** LinkedIn Branding
- **Objective:** Design a prompt for a consistent personal-brand voice.
- **Prompt:**
  ```
  Design a prompt that generates LinkedIn posts consistent with a stated personal brand (e.g. 'grounded, technical, no hype'), enforcing that voice as an explicit constraint.
  ```
- **Expected Output:** One ready-to-use branded-voice prompt.

### P098
- **Category:** Domain-specific AI Prompts
- **Technique:** Tree-of-Thought
- **Domain:** Embedded Systems
- **Objective:** Explore communication protocol choices for a sensor network.
- **Prompt:**
  ```
  For a low-power multi-sensor network with {constraints}, branch into three protocol choices (I2C / SPI / UART-based), evaluate trade-offs, then recommend one.
  ```
- **Expected Output:** 3 evaluated branches, then a recommendation.

### P099
- **Category:** Domain-specific AI Prompts
- **Technique:** One-Shot
- **Domain:** Data Science / ML
- **Objective:** Explain a confusion matrix cell in context.
- **Prompt:**
  ```
  Explain what a specific confusion matrix cell means for the business.
  
  Example: False Negatives in fraud detection -> "Fraudulent transactions that went undetected, directly causing financial loss."
  
  Now explain: {cell_type} in {context}
  ```
- **Expected Output:** One business-framed explanation.

### P100
- **Category:** Domain-specific AI Prompts
- **Technique:** Prompt Chaining
- **Domain:** Telecom Core Networks
- **Objective:** Chain: KPI drop -> correlated alarms -> root cause -> RCA report.
- **Prompt:**
  ```
  STAGE 1: List KPIs that dropped given {kpi_data}.
  STAGE 2: Correlate the drop with alarms in {alarm_log}.
  STAGE 3: State the most likely root cause.
  STAGE 4: Write a one-paragraph RCA report summarizing stages 1-3.
  ```
- **Expected Output:** 4 chained outputs ending in a short RCA report.
