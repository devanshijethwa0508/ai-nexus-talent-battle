"""
build_prompt_library.py
--------------------------
Generates prompt_library.md: 100 prompts, 10 per required category,
covering the domains AI NEXUS 360 actually uses (resumes, interviews,
content, and general engineering/technical prompts) so the library is
reusable rather than filler.

Run: python build_prompt_library.py
"""

PROMPTS = []
_id = 0


def add(category, technique, domain, objective, prompt, expected_output,
        example_input="", example_output=""):
    global _id
    _id += 1
    PROMPTS.append({
        "id": f"P{_id:03d}", "category": category, "technique": technique,
        "domain": domain, "objective": objective, "prompt": prompt.strip(),
        "expected_output": expected_output, "example_input": example_input,
        "example_output": example_output,
    })


# ============================================================ ZERO-SHOT (10)
add("Prompt Engineering", "Zero-Shot", "Resume Writing",
    "Extract ATS keywords from a job description.",
    "Extract the top 15 technical keywords an ATS would scan for in this job description. Return a comma-separated list only.\n\nJob Description: {job_description}",
    "A comma-separated keyword list, no extra text.")
add("Prompt Engineering", "Zero-Shot", "Interview Prep",
    "Generate a technical interview question.",
    "Generate one medium-difficulty technical interview question for a {role} candidate on the topic of {topic}.",
    "A single, clearly worded interview question.")
add("Prompt Engineering", "Zero-Shot", "Content Creation",
    "Write a LinkedIn post from a topic.",
    "Write a 150-word LinkedIn post about {topic} for an audience of {audience}. Professional tone.",
    "A ready-to-post LinkedIn caption.")
add("Prompt Engineering", "Zero-Shot", "Career Guidance",
    "Summarize a job description into requirements.",
    "Summarize this job description into 5 bullet points covering the core responsibilities.\n\n{job_description}",
    "5 bullet points.")
add("Prompt Engineering", "Zero-Shot", "Embedded Systems",
    "Explain a hardware concept plainly.",
    "Explain what a watchdog timer does in an embedded system, in 3 sentences, for a fresher audience.",
    "3-sentence plain-language explanation.")
add("Prompt Engineering", "Zero-Shot", "Data Science",
    "Explain a metric.",
    "Explain the difference between precision and recall in 100 words, with one real-world analogy.",
    "100-word explanation with an analogy.")
add("Prompt Engineering", "Zero-Shot", "Telecom",
    "Summarize a protocol.",
    "Summarize how the SIP protocol establishes a VoIP call, in 5 steps.",
    "A 5-step numbered summary.")
add("Prompt Engineering", "Zero-Shot", "Email Writing",
    "Draft a follow-up email.",
    "Write a polite follow-up email to a recruiter one week after submitting an application for {role}, keeping it under 100 words.",
    "A complete, ready-to-send email under 100 words.")
add("Prompt Engineering", "Zero-Shot", "Code Review",
    "Identify an issue in a code snippet.",
    "Review this Python function and list any bugs or edge cases it misses:\n\n{code}",
    "A bullet list of issues found.")
add("Prompt Engineering", "Zero-Shot", "Content Creation",
    "Generate hashtags.",
    "Generate 5 relevant hashtags for a post about {topic} aimed at {audience}.",
    "5 hashtags.")

# ============================================================ ONE-SHOT (10)
add("Prompt Engineering", "One-Shot", "Resume Writing",
    "Rewrite a bullet point to be achievement-focused.",
    "Rewrite resume bullets to be achievement-focused.\n\nExample:\nBefore: \"Worked on a billing system.\"\nAfter: \"Built a billing module handling 500+ daily transactions, reducing manual entry errors.\"\n\nNow rewrite: \"Before: {raw_bullet}\"",
    "One rewritten, achievement-focused bullet.",
    "Before: Made a website for college fest.",
    "After: Built and deployed the college fest website, used by 2,000+ visitors over the event weekend.")
add("Prompt Engineering", "One-Shot", "Interview Prep",
    "Generate a follow-up probing question.",
    "Given an interview answer, generate one probing follow-up question.\n\nExample:\nAnswer: \"I used a hashmap to solve it in O(n).\"\nFollow-up: \"What would you do if the input didn't fit in memory?\"\n\nNow generate a follow-up for: \"{answer}\"",
    "One follow-up question.",
    "Answer: I optimized the query using an index.",
    "Follow-up: What tradeoff did adding that index introduce on writes?")
add("Prompt Engineering", "One-Shot", "Content Creation",
    "Write a tweet in a target style.",
    "Write a tweet under 280 characters in this style.\n\nExample:\nTopic: Debugging\nTweet: \"90% of debugging is admitting the bug is in the line you skipped reading.\"\n\nNow write one for: \"{topic}\"",
    "One tweet under 280 characters.")
add("Prompt Engineering", "One-Shot", "Email Writing",
    "Write a thank-you-after-interview email.",
    "Write a thank-you email after an interview.\n\nExample:\nRole: Data Analyst\nEmail: \"Thank you for the conversation today about the Data Analyst role...\"\n\nNow write one for: Role: {role}, Interviewer: {interviewer_name}",
    "A complete thank-you email.")
add("Prompt Engineering", "One-Shot", "Embedded Systems",
    "Explain an error code in context.",
    "Explain an embedded error code like the example.\n\nExample:\nCode: HAL_TIMEOUT\nExplanation: \"The peripheral did not respond within the configured wait time, often due to a clock misconfiguration.\"\n\nNow explain: {error_code}",
    "One explanation matching the example's style.")
add("Prompt Engineering", "One-Shot", "Data Science",
    "Explain a model choice.",
    "Justify a model choice.\n\nExample:\nProblem: Predicting churn with imbalanced classes.\nJustification: \"Random Forest is chosen for its robustness to class imbalance when combined with class weighting.\"\n\nNow justify a model for: {problem}",
    "One justification.")
add("Prompt Engineering", "One-Shot", "Telecom",
    "Summarize an incident report.",
    "Summarize a network incident in one sentence.\n\nExample:\nDetails: \"Cell site X lost backhaul for 40 minutes due to a fiber cut.\"\nSummary: \"40-minute outage at Site X caused by fiber cut.\"\n\nNow summarize: {incident_details}",
    "One-sentence summary.")
add("Prompt Engineering", "One-Shot", "Career Guidance",
    "Reframe a gap year positively.",
    "Reframe a resume gap.\n\nExample:\nGap: \"1 year unemployed after graduation.\"\nReframe: \"Spent 2025 building independent ML projects and completing two certifications while job hunting.\"\n\nNow reframe: {gap_description}",
    "One reframed sentence, no fabricated employer.")
add("Prompt Engineering", "One-Shot", "Code Review",
    "Suggest a more Pythonic version of a line.",
    "Suggest a Pythonic rewrite.\n\nExample:\nBefore: \"for i in range(len(lst)): print(lst[i])\"\nAfter: \"for item in lst: print(item)\"\n\nNow rewrite: \"{code_line}\"",
    "One rewritten line.")
add("Prompt Engineering", "One-Shot", "Content Creation",
    "Write an Instagram caption in a target voice.",
    "Write an Instagram caption.\n\nExample:\nTopic: Internship offer\nCaption: \"Said yes before they finished the sentence. Onward. 🚀\"\n\nNow write one for: {topic}",
    "One caption with emoji.")

# ============================================================ FEW-SHOT (10)
add("Prompt Engineering", "Few-Shot", "Resume Writing",
    "Generate a Professional Summary from candidate facts.",
    "Write a resume summary, following these examples' tone.\n\nExample 1: Input: Fresher, CSE, Django/Postgres, billing dashboard. Output: \"CS graduate experienced in full-stack billing dashboards using Django and PostgreSQL, focused on shippable, testable code.\"\nExample 2: Input: Fresher, ECE, STM32/RTOS, sensor fusion. Output: \"Electronics graduate specializing in embedded firmware, from register-level drivers to real-time scheduling.\"\n\nNow write for: {candidate_facts}",
    "One 2-3 sentence summary matching the examples' register.")
add("Prompt Engineering", "Few-Shot", "Interview Prep",
    "Score an interview answer 1-10.",
    "Score interview answers 1-10 for technical accuracy.\n\nExample 1: Answer: \"Uses O(n log n) sort then binary search.\" Score: 9\nExample 2: Answer: \"I'd just try stuff until it works.\" Score: 2\nExample 3: Answer: \"Two-pointer approach after sorting, O(n log n) overall.\" Score: 8\n\nNow score: \"{answer}\"",
    "A single integer 1-10 with one-line justification.")
add("Prompt Engineering", "Few-Shot", "Content Creation",
    "Generate a headline in a proven style.",
    "Write a headline.\n\nExample 1: Topic: AI in healthcare -> \"The Algorithm Will See You Now\"\nExample 2: Topic: remote work -> \"Home Is Where The Standup Is\"\nExample 3: Topic: cybersecurity -> \"Trust No Click\"\n\nNow write one for: {topic}",
    "One punchy headline, same style/length.")
add("Prompt Engineering", "Few-Shot", "Data Science",
    "Classify a bug report's severity.",
    "Classify severity as Low/Medium/High.\n\nExample 1: \"Typo in footer.\" -> Low\nExample 2: \"Login fails for 10% of users.\" -> High\nExample 3: \"Chart colors slightly off-brand.\" -> Low\nExample 4: \"Checkout crashes for Safari users.\" -> High\n\nNow classify: \"{bug_report}\"",
    "One severity label with reasoning.")
add("Prompt Engineering", "Few-Shot", "Telecom",
    "Categorize a network fault.",
    "Categorize the fault type.\n\nExample 1: \"BTS unreachable, power alarm active\" -> Power Fault\nExample 2: \"High packet loss on backhaul link\" -> Transmission Fault\nExample 3: \"Cell showing degraded RSSI\" -> RF Fault\n\nNow categorize: \"{fault_description}\"",
    "One category label.")
add("Prompt Engineering", "Few-Shot", "Email Writing",
    "Write a negotiation email in a firm-but-polite tone.",
    "Write a salary negotiation email.\n\nExample 1: Offer: 6 LPA, target 7.2 LPA -> polite, cites market data, no ultimatums.\nExample 2: Offer: 8 LPA, target 8.5 LPA -> polite, cites a competing offer.\n\nNow write for: Offer {offer}, target {target}",
    "One complete email in the same tone.")
add("Prompt Engineering", "Few-Shot", "Embedded Systems",
    "Diagnose a likely cause from symptoms.",
    "Diagnose the likely cause.\n\nExample 1: \"MCU resets randomly under load\" -> brown-out from insufficient decoupling.\nExample 2: \"UART receives garbage bytes\" -> baud rate mismatch.\n\nNow diagnose: \"{symptom}\"",
    "One likely cause with brief reasoning.")
add("Prompt Engineering", "Few-Shot", "Career Guidance",
    "Match a project to a job requirement.",
    "Match a project to a JD requirement, in one sentence.\n\nExample 1: Requirement: \"Experience with REST APIs\" + Project: \"Built a Flask API for a todo app\" -> \"Directly demonstrates REST API design and implementation.\"\n\nNow match: Requirement: {requirement}, Project: {project}",
    "One matching sentence.")
add("Prompt Engineering", "Few-Shot", "Code Review",
    "Flag a security issue in code.",
    "Flag security issues.\n\nExample 1: \"query = f'SELECT * WHERE id={user_input}'\" -> SQL injection risk, use parameterized queries.\nExample 2: \"password stored in plaintext\" -> hash with bcrypt/argon2.\n\nNow review: \"{code_snippet}\"",
    "Issue name + one-line fix.")
add("Prompt Engineering", "Few-Shot", "Content Creation",
    "Write a CTA matching examples.",
    "Write a call-to-action.\n\nExample 1: Topic: new blog post -> \"Read the full breakdown →\"\nExample 2: Topic: webinar -> \"Save your seat before it fills up.\"\n\nNow write one for: {topic}",
    "One short CTA line.")

# ============================================================ ROLE PROMPTING (10)
add("Prompt Engineering", "Role Prompting", "Resume Writing",
    "Act as a recruiter to critique a resume.",
    "You are a senior technical recruiter who has screened 5,000+ resumes. Critique this resume for a {role} position, focusing on what would get it rejected in a 10-second scan.\n\n{resume_text}",
    "A blunt, recruiter-style critique.")
add("Prompt Engineering", "Role Prompting", "Interview Prep",
    "Act as a strict panel interviewer.",
    "You are a strict, no-nonsense panel interviewer at a top product company. Ask one hard follow-up question that exposes shallow understanding, based on this answer: \"{answer}\"",
    "One incisive follow-up question.")
add("Prompt Engineering", "Role Prompting", "Content Creation",
    "Act as a copywriter for a specific brand voice.",
    "You are a witty, Gen-Z-savvy social media copywriter. Write an Instagram caption about {topic} in that voice.",
    "One caption in the specified voice.")
add("Prompt Engineering", "Role Prompting", "Data Science",
    "Act as a skeptical peer reviewer.",
    "You are a skeptical ML peer reviewer. Point out three ways this experiment's results could be misleading: {experiment_summary}",
    "3 skeptical points.")
add("Prompt Engineering", "Role Prompting", "Telecom",
    "Act as a network operations engineer.",
    "You are a telecom NOC engineer during an active outage. Given this alarm log, state the single most likely root cause and the first diagnostic step you'd take.\n\n{alarm_log}",
    "One root-cause hypothesis + one next step.")
add("Prompt Engineering", "Role Prompting", "Embedded Systems",
    "Act as a hardware bring-up engineer.",
    "You are a hardware bring-up engineer debugging a new board. Given this symptom, list the first three things you'd check on the board.\n\nSymptom: {symptom}",
    "3 concrete checks, hardware-first.")
add("Prompt Engineering", "Role Prompting", "Career Guidance",
    "Act as a career coach for freshers.",
    "You are a career coach specializing in placing fresh engineering graduates. Given this profile, name the single biggest gap holding back their applications.\n\n{profile_summary}",
    "One specific, honest gap.")
add("Prompt Engineering", "Role Prompting", "Code Review",
    "Act as a strict senior engineer doing code review.",
    "You are a strict senior engineer reviewing a junior's pull request. List every issue you'd block the PR on, in order of severity.\n\n{code_diff}",
    "A severity-ordered issue list.")
add("Prompt Engineering", "Role Prompting", "Email Writing",
    "Act as an HR professional drafting a rejection.",
    "You are an HR professional. Write a respectful, encouraging rejection email for a candidate who interviewed well but was not selected for {role}.",
    "One complete, respectful email.")
add("Prompt Engineering", "Role Prompting", "Content Creation",
    "Act as a technical educator explaining to beginners.",
    "You are a patient technical educator. Explain {concept} to someone with zero background, using one everyday analogy.",
    "A beginner-friendly explanation with an analogy.")

# ============================================================ STRUCTURED PROMPTING (10)
add("Prompt Engineering", "Structured Prompting", "Resume Writing",
    "Generate a full resume with fixed sections.",
    "ROLE: Expert resume writer.\nCONTEXT: {candidate_context}\nTASK: Write Professional Summary, Technical Skills, Experience, Projects, Education sections.\nCONSTRAINTS: Do not invent facts.\nOUTPUT FORMAT: Markdown headings (##), nothing else.",
    "A resume in the exact 5-section Markdown structure.")
add("Prompt Engineering", "Structured Prompting", "Interview Prep",
    "Generate a scored evaluation as JSON.",
    "ROLE: Technical interviewer.\nTASK: Score this answer.\nINPUT: Question: {question}, Answer: {answer}\nOUTPUT FORMAT (strict JSON): {{\"technical_accuracy\":0,\"clarity\":0,\"overall_score\":0.0}}",
    "Valid JSON matching the exact schema, no extra text.")
add("Prompt Engineering", "Structured Prompting", "Content Creation",
    "Generate multi-platform content as JSON.",
    "ROLE: Content strategist.\nTASK: Generate LinkedIn post, tweet, and 3 hashtags for {topic}.\nOUTPUT FORMAT (strict JSON): {{\"linkedin\":\"\",\"tweet\":\"\",\"hashtags\":[]}}",
    "Valid JSON with exactly those three keys.")
add("Prompt Engineering", "Structured Prompting", "Data Science",
    "Generate a model comparison table.",
    "ROLE: ML consultant.\nTASK: Compare {model_a} vs {model_b} for {use_case}.\nOUTPUT FORMAT: A Markdown table with columns: Criterion | {model_a} | {model_b}.",
    "A well-formed Markdown table.")
add("Prompt Engineering", "Structured Prompting", "Telecom",
    "Generate an incident report in a fixed template.",
    "TASK: Fill this incident template from the raw notes.\nTEMPLATE: Incident ID / Start Time / End Time / Root Cause / Impact / Resolution\nRAW NOTES: {raw_notes}\nOUTPUT FORMAT: Field: Value, one per line, in that exact order.",
    "6 lines, one field per line, in order.")
add("Prompt Engineering", "Structured Prompting", "Embedded Systems",
    "Generate a register configuration checklist.",
    "TASK: List the register configuration steps to enable {peripheral} on {mcu}.\nOUTPUT FORMAT: Numbered list, one register/bit per step, no prose paragraphs.",
    "A numbered, register-level checklist.")
add("Prompt Engineering", "Structured Prompting", "Career Guidance",
    "Generate a 30-60-90 day plan.",
    "TASK: Create a 30-60-90 day plan for a fresher starting as {role}.\nOUTPUT FORMAT (strict JSON): {{\"30_days\":[],\"60_days\":[],\"90_days\":[]}}",
    "Valid JSON with three array fields.")
add("Prompt Engineering", "Structured Prompting", "Code Review",
    "Generate a review report with fixed fields.",
    "TASK: Review this code: {code}\nOUTPUT FORMAT: Bugs: <list>\\nStyle Issues: <list>\\nSecurity Issues: <list>\\nVerdict: Approve/Request Changes",
    "Exactly those four labeled sections.")
add("Prompt Engineering", "Structured Prompting", "Email Writing",
    "Generate a structured cold outreach email.",
    "TASK: Write a cold outreach email to {recipient_role} about {ask}.\nOUTPUT FORMAT: Subject: <one line>\\nBody: <email body>",
    "Exactly a Subject line and a Body.")
add("Prompt Engineering", "Structured Prompting", "Content Creation",
    "Generate a content calendar as JSON.",
    "TASK: Create a 5-day content calendar on {theme}.\nOUTPUT FORMAT (strict JSON): [{{\"day\":1,\"platform\":\"\",\"topic\":\"\"}}, ...]",
    "A JSON array of 5 objects with those three keys.")

# ============================================================ META PROMPTING (10)
add("Prompt Engineering", "Meta Prompting", "Resume Writing",
    "Design a prompt for resume bullet rewriting.",
    "Design an effective prompt for the task: 'rewrite a weak resume bullet into an achievement-focused one, without inventing metrics.' Include role, constraints, and output format.",
    "A ready-to-use prompt, not the rewritten bullet itself.")
add("Prompt Engineering", "Meta Prompting", "Interview Prep",
    "Design a prompt for adaptive question difficulty.",
    "Design a prompt that generates the NEXT interview question, harder or easier depending on how well the previous answer scored. Include the scoring input format.",
    "A ready-to-use adaptive-difficulty prompt template.")
add("Prompt Engineering", "Meta Prompting", "Content Creation",
    "Design a prompt for platform-adapted content.",
    "Design a prompt that takes one topic and produces genuinely different copy per platform (LinkedIn vs Instagram vs Twitter), not the same text reused.",
    "A ready-to-use multi-platform prompt template.")
add("Prompt Engineering", "Meta Prompting", "Data Science",
    "Improve a vague data-analysis prompt.",
    "Here is a weak prompt: \"analyze this data.\" Rewrite it into a strong, structured prompt that specifies the analysis goal, expected output format, and constraints.",
    "One improved prompt, not an analysis.")
add("Prompt Engineering", "Meta Prompting", "Telecom",
    "Design a prompt for root-cause analysis from logs.",
    "Design a prompt for extracting a single root cause from noisy telecom alarm logs, specifying what counts as 'root cause' vs 'symptom' in the instructions.",
    "One ready-to-use RCA prompt.")
add("Prompt Engineering", "Meta Prompting", "Embedded Systems",
    "Design a prompt for datasheet-grounded answers.",
    "Design a prompt that forces an LLM to answer embedded hardware questions ONLY using facts from a provided datasheet excerpt, refusing to guess otherwise.",
    "One ready-to-use grounded-QA prompt.")
add("Prompt Engineering", "Meta Prompting", "Career Guidance",
    "Design a prompt for honest gap analysis.",
    "Design a prompt that compares a candidate's resume to a job description and honestly flags gaps, avoiding generic flattery. Specify tone constraints explicitly.",
    "One ready-to-use gap-analysis prompt.")
add("Prompt Engineering", "Meta Prompting", "Code Review",
    "Design a prompt for severity-ranked code review.",
    "Design a prompt that reviews code and ranks every issue by severity (blocking / major / minor / nitpick), with a fixed output format.",
    "One ready-to-use code-review prompt.")
add("Prompt Engineering", "Meta Prompting", "Email Writing",
    "Design a prompt for tone-matched email replies.",
    "Design a prompt that drafts an email reply matching the formality level of the email it's replying to, inferred automatically rather than asked for.",
    "One ready-to-use tone-matching prompt.")
add("Prompt Engineering", "Meta Prompting", "Content Creation",
    "Improve a prompt for hashtag generation.",
    "Here is a weak prompt: \"give me hashtags.\" Rewrite it to specify count, relevance criteria, and platform norms explicitly.",
    "One improved prompt.")

# ============================================================ CHAIN-OF-THOUGHT (10)
add("Prompting Techniques", "Chain-of-Thought", "Resume Writing",
    "Reason through whether a claim is consistent.",
    "A candidate claims: \"{claim}\". Think step by step about what skills/time this would require, then decide if it's plausible for a fresher. Show your reasoning, then give a final verdict.",
    "Step-by-step reasoning followed by a verdict.")
add("Prompting Techniques", "Chain-of-Thought", "Interview Prep",
    "Solve a DSA problem with visible reasoning.",
    "Solve this problem step by step, explaining your reasoning at each step before writing final code: {problem_statement}",
    "Numbered reasoning steps, then final code.")
add("Prompting Techniques", "Chain-of-Thought", "Data Science",
    "Diagnose why a model underperforms.",
    "This model's accuracy dropped after deployment: {context}. Think step by step through possible causes (data drift, leakage, label shift, etc.) before concluding the most likely cause.",
    "Step-by-step elimination, then a conclusion.")
add("Prompting Techniques", "Chain-of-Thought", "Telecom",
    "Trace a call-drop root cause.",
    "Given these KPIs and alarms: {data}, reason step by step through the call chain (RF -> Transport -> Core) to isolate where the drop most likely occurred.",
    "A layer-by-layer trace ending in one conclusion.")
add("Prompting Techniques", "Chain-of-Thought", "Embedded Systems",
    "Debug a timing issue methodically.",
    "An interrupt handler sometimes misses events: {symptom_details}. Reason step by step through timing, priority, and race-condition possibilities before concluding.",
    "Step-by-step debugging reasoning, then a conclusion.")
add("Prompting Techniques", "Chain-of-Thought", "Career Guidance",
    "Decide between two job offers.",
    "Compare these two offers step by step across growth, compensation, and learning curve before recommending one: Offer A: {offer_a}, Offer B: {offer_b}",
    "Step-by-step comparison, then a recommendation.")
add("Prompting Techniques", "Chain-of-Thought", "Code Review",
    "Trace through code to find a logic bug.",
    "Trace through this function step by step with the input {sample_input} to find where the output diverges from expectations.\n\n{code}",
    "A step-by-step trace, then the located bug.")
add("Prompting Techniques", "Chain-of-Thought", "Content Creation",
    "Plan a content angle before writing.",
    "Before writing the post, think step by step: who is the audience, what do they already believe about {topic}, and what's the one new idea worth their time? Then write the post.",
    "Visible reasoning, then the final post.")
add("Prompting Techniques", "Chain-of-Thought", "Email Writing",
    "Decide the right tone before drafting.",
    "Before drafting, reason step by step about the relationship and stakes implied by this context: {context}. Then write the email in the tone you concluded.",
    "Brief reasoning, then the email.")
add("Prompting Techniques", "Chain-of-Thought", "Data Science",
    "Choose an evaluation metric methodically.",
    "For this problem: {problem_description}, reason step by step about class balance and business cost of false positives/negatives before recommending one evaluation metric.",
    "Step-by-step reasoning, then one recommended metric.")

# ============================================================ TREE-OF-THOUGHT (10)
add("Prompting Techniques", "Tree-of-Thought", "Resume Writing",
    "Explore three bullet-point framings.",
    "For this raw achievement: \"{achievement}\", generate three different bullet framings (technical depth / business impact / leadership), rate each 1-10, then recommend one.",
    "3 rated branches + a final recommendation.")
add("Prompting Techniques", "Tree-of-Thought", "Interview Prep",
    "Explore multiple solution approaches to a problem.",
    "For this problem: {problem}, explore three different algorithmic approaches, note the time/space complexity of each, then recommend the best for an interview setting.",
    "3 approaches with complexity, then a recommendation.")
add("Prompting Techniques", "Tree-of-Thought", "Data Science",
    "Explore multiple feature-engineering strategies.",
    "For predicting {target}, branch into three feature-engineering strategies, evaluate each for likely predictive value and cost to build, then pick one.",
    "3 branches evaluated, then a final pick.")
add("Prompting Techniques", "Tree-of-Thought", "Telecom",
    "Explore multiple root-cause hypotheses.",
    "Given this fault: {fault_description}, branch into three plausible root-cause hypotheses (RF / Transport / Core), evaluate the evidence for each, then pick the most likely.",
    "3 hypotheses evaluated, then a conclusion.")
add("Prompting Techniques", "Tree-of-Thought", "Embedded Systems",
    "Explore multiple low-power design strategies.",
    "For a battery-powered sensor node with {constraints}, branch into three low-power strategies (duty cycling / sleep modes / event-driven wake), evaluate trade-offs, then recommend one.",
    "3 branches with trade-offs, then a recommendation.")
add("Prompting Techniques", "Tree-of-Thought", "Career Guidance",
    "Explore multiple career-path branches.",
    "Given this background: {background}, branch into three plausible next-role paths, evaluate pros/cons of each for a 2-year horizon, then recommend one.",
    "3 paths evaluated, then a recommendation.")
add("Prompting Techniques", "Tree-of-Thought", "Code Review",
    "Explore multiple refactor strategies.",
    "For this code: {code}, branch into three refactor strategies (performance-focused / readability-focused / minimal-diff), evaluate each, then recommend one.",
    "3 strategies evaluated, then a recommendation.")
add("Prompting Techniques", "Tree-of-Thought", "Content Creation",
    "Explore multiple headline angles.",
    "For the topic {topic}, branch into three headline angles (curiosity / benefit / controversy), write one headline per angle, rate each for click potential, then recommend one.",
    "3 rated headlines, then a recommendation.")
add("Prompting Techniques", "Tree-of-Thought", "Email Writing",
    "Explore multiple negotiation framings.",
    "For negotiating {ask}, branch into three framings (data-driven / relationship-based / urgency-based), draft one line for each, then recommend which fits {context} best.",
    "3 framings, then a recommendation.")
add("Prompting Techniques", "Tree-of-Thought", "Resume Writing",
    "Explore multiple summary openings.",
    "For a candidate targeting {role}, branch into three different opening lines for a resume summary, each leading with a different strength, then recommend one.",
    "3 opening lines, then a recommendation.")

# ============================================================ PROMPT CHAINING (10)
add("Prompting Techniques", "Prompt Chaining", "Resume Writing",
    "Chain: extract skills -> gap -> recommendations -> optimized resume.",
    "STAGE 1 of 4: Extract required skills from this job description as a comma-separated list.\n\n{job_description}",
    "Output feeds Stage 2 (skill-gap analysis).")
add("Prompting Techniques", "Prompt Chaining", "Resume Writing",
    "Chain stage 2: analyze skill gap.",
    "STAGE 2 of 4: Required skills: {output_1}. Candidate skills: {candidate_skills}. List the missing skills.",
    "Output feeds Stage 3 (recommendations).")
add("Prompting Techniques", "Prompt Chaining", "Resume Writing",
    "Chain stage 3: generate recommendations.",
    "STAGE 3 of 4: Missing skills: {output_2}. Generate 4-5 honest ways to address this gap on a resume without fabricating experience.",
    "Output feeds Stage 4 (final resume).")
add("Prompting Techniques", "Prompt Chaining", "Resume Writing",
    "Chain stage 4: optimize final resume.",
    "STAGE 4 of 4: Draft resume: {draft_resume}. Recommendations: {output_3}. Apply them and return the optimized resume.",
    "Final resume output.")
add("Prompting Techniques", "Prompt Chaining", "Interview Prep",
    "Chain: question -> answer -> eval -> next question difficulty.",
    "STAGE 1: Generate an Easy question for {domain}.\nSTAGE 2 (after answer): Evaluate the answer and output a score 0-10.\nSTAGE 3: If score >= 7, generate a Medium question next; else generate another Easy question.",
    "A 3-stage adaptive chain description with explicit branching rule.")
add("Prompting Techniques", "Prompt Chaining", "Content Creation",
    "Chain: outline -> draft -> platform adaptation.",
    "STAGE 1: Outline 3 key points about {topic}.\nSTAGE 2: Expand the outline into a full blog draft.\nSTAGE 3: Adapt the blog draft into a LinkedIn post using only its core idea, not its full text.",
    "3 chained outputs, each built from the previous.")
add("Prompting Techniques", "Prompt Chaining", "Data Science",
    "Chain: EDA summary -> hypothesis -> test plan.",
    "STAGE 1: Summarize key patterns in this dataset description: {dataset_summary}.\nSTAGE 2: From the patterns, propose one testable hypothesis.\nSTAGE 3: Design a statistical test to check that hypothesis.",
    "3 chained outputs.")
add("Prompting Techniques", "Prompt Chaining", "Telecom",
    "Chain: raw logs -> anomalies -> root cause -> action.",
    "STAGE 1: Extract anomalies from this raw log: {raw_log}.\nSTAGE 2: Given the anomalies, identify the most likely root cause.\nSTAGE 3: Given the root cause, recommend one corrective action.",
    "3 chained outputs, each depending on the last.")
add("Prompting Techniques", "Prompt Chaining", "Career Guidance",
    "Chain: profile -> gaps -> 90-day plan.",
    "STAGE 1: List this candidate's current strengths from {profile}.\nSTAGE 2: Compare strengths to {target_role} requirements and list gaps.\nSTAGE 3: Turn the gaps into a 90-day upskilling plan.",
    "3 chained outputs.")
add("Prompting Techniques", "Prompt Chaining", "Code Review",
    "Chain: find bugs -> prioritize -> write fixes.",
    "STAGE 1: List all bugs found in {code}.\nSTAGE 2: Rank the bugs by severity.\nSTAGE 3: Write the fix for only the top-ranked bug.",
    "3 chained outputs, each narrowing on the previous.")

# ============================================================ DOMAIN-SPECIFIC (10)
add("Domain-specific AI Prompts", "Structured Prompting", "Embedded Systems",
    "Generate a peripheral init checklist for a target MCU.",
    "List the initialization steps for enabling {peripheral} (e.g. UART, SPI, ADC) on {mcu_family}, in the order a bring-up engineer would perform them.",
    "A numbered, hardware-accurate checklist.")
add("Domain-specific AI Prompts", "Few-Shot", "Telecom Core Networks",
    "Classify a core-network alarm by 3GPP domain.",
    "Classify this alarm by domain (RAN / Transport / Core / IMS).\n\nExample 1: \"MME path failure\" -> Core\nExample 2: \"eNB cell down\" -> RAN\n\nNow classify: \"{alarm_text}\"",
    "One domain label with justification.")
add("Domain-specific AI Prompts", "Chain-of-Thought", "Data Science / ML",
    "Reason about overfitting in a specific model.",
    "Given train accuracy {train_acc}% and validation accuracy {val_acc}%, reason step by step about whether this indicates overfitting and what to try next.",
    "Step-by-step reasoning, then a recommendation.")
add("Domain-specific AI Prompts", "Role Prompting", "Instrumentation",
    "Act as a calibration engineer.",
    "You are an instrumentation calibration engineer. Given this sensor drift data: {drift_data}, state whether recalibration is due and why.",
    "One clear yes/no with justification.")
add("Domain-specific AI Prompts", "Structured Prompting", "Placements / Job Search",
    "Generate a weekly job-search tracker entry.",
    "TASK: Turn this raw update into a tracker row.\nRAW UPDATE: {raw_update}\nOUTPUT FORMAT: Company | Role | Stage | Next Action | Date",
    "One pipe-delimited row.")
add("Domain-specific AI Prompts", "Zero-Shot", "IEEE / Research Writing",
    "Tighten an abstract to a word limit.",
    "Rewrite this abstract to fit within {word_limit} words while keeping the core contribution and results intact.\n\n{abstract_text}",
    "A rewritten abstract at or under the word limit.")
add("Domain-specific AI Prompts", "Meta Prompting", "LinkedIn Branding",
    "Design a prompt for a consistent personal-brand voice.",
    "Design a prompt that generates LinkedIn posts consistent with a stated personal brand (e.g. 'grounded, technical, no hype'), enforcing that voice as an explicit constraint.",
    "One ready-to-use branded-voice prompt.")
add("Domain-specific AI Prompts", "Tree-of-Thought", "Embedded Systems",
    "Explore communication protocol choices for a sensor network.",
    "For a low-power multi-sensor network with {constraints}, branch into three protocol choices (I2C / SPI / UART-based), evaluate trade-offs, then recommend one.",
    "3 evaluated branches, then a recommendation.")
add("Domain-specific AI Prompts", "One-Shot", "Data Science / ML",
    "Explain a confusion matrix cell in context.",
    "Explain what a specific confusion matrix cell means for the business.\n\nExample: False Negatives in fraud detection -> \"Fraudulent transactions that went undetected, directly causing financial loss.\"\n\nNow explain: {cell_type} in {context}",
    "One business-framed explanation.")
add("Domain-specific AI Prompts", "Prompt Chaining", "Telecom Core Networks",
    "Chain: KPI drop -> correlated alarms -> root cause -> RCA report.",
    "STAGE 1: List KPIs that dropped given {kpi_data}.\nSTAGE 2: Correlate the drop with alarms in {alarm_log}.\nSTAGE 3: State the most likely root cause.\nSTAGE 4: Write a one-paragraph RCA report summarizing stages 1-3.",
    "4 chained outputs ending in a short RCA report.")

assert len(PROMPTS) == 100, f"Expected 100 prompts, got {len(PROMPTS)}"

CATEGORY_ORDER = [
    "Zero-Shot", "One-Shot", "Few-Shot", "Role Prompting", "Structured Prompting",
    "Meta Prompting", "Chain-of-Thought", "Tree-of-Thought", "Prompt Chaining",
]

lines = ["# AI NEXUS 360 — Prompt Library", "",
         "100 reusable prompts across the 10 required categories, drawn from the",
         "domains this ecosystem actually uses: resumes, interviews, content,",
         "and Devanshi's core technical areas (embedded systems, telecom, data science).",
         "", "## Distribution", "",
         "| Category | Count |", "|---|---|"]

from collections import Counter
counts = Counter(p["technique"] for p in PROMPTS)
for tech in CATEGORY_ORDER:
    lines.append(f"| {tech} | {counts.get(tech, 0)} |")
domain_specific_count = sum(1 for p in PROMPTS if p["category"] == "Domain-specific AI Prompts")
lines.append(f"| Domain-specific AI Prompts | {domain_specific_count} |")
lines.append(f"| **Total** | **{len(PROMPTS)}** |")
lines.append("")
lines.append("---")
lines.append("")

for p in PROMPTS:
    lines.append(f"### {p['id']}")
    lines.append(f"- **Category:** {p['category']}")
    lines.append(f"- **Technique:** {p['technique']}")
    lines.append(f"- **Domain:** {p['domain']}")
    lines.append(f"- **Objective:** {p['objective']}")
    lines.append(f"- **Prompt:**")
    lines.append("  ```")
    for line in p["prompt"].split("\n"):
        lines.append(f"  {line}")
    lines.append("  ```")
    lines.append(f"- **Expected Output:** {p['expected_output']}")
    if p["example_input"]:
        lines.append(f"- **Example Input:** {p['example_input']}")
    if p["example_output"]:
        lines.append(f"- **Example Output:** {p['example_output']}")
    lines.append("")

with open("prompt_library.md", "w") as f:
    f.write("\n".join(lines))

print(f"Wrote prompt_library.md with {len(PROMPTS)} prompts.")
