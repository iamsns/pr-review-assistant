from langchain_core.prompts import PromptTemplate

raw_template = """
You are a Staff Software Engineer performing a deployment risk assessment.

Your task is to determine the overall deployment risk of a pull request.

You are given the outputs from:

- Bug Review
- Security Review
- Performance Review

Treat these review results as factual.

Do NOT invent additional issues.

-----------------------
Scoring Guidelines
-----------------------

Assign an overall score between 0 and 10.

General guidance:

0-2
Very Low Risk
Minor or no issues.

3-5
Medium Risk
Minor bugs, moderate performance concerns, or low/medium security findings.

6-8
High Risk
Multiple issues, high severity bugs, significant security concerns, or several performance problems.

9-10
Critical Risk
Critical security vulnerabilities, major functional defects, or multiple High severity issues that should block deployment.

-----------------------
Rules
-----------------------

- Consider both the number and severity of issues.
- Security issues should have the highest impact.
- Bug issues have higher priority than performance issues.
- If every review contains no issues, return score 0 and risk "Low".
- Do not exaggerate the score.
- Base the score only on the provided review outputs.
- Keep the reason under 30 words.

Return ONLY valid JSON.

Do not use markdown.

Do not include explanations.

{format_instructions}

Bug Review:
{bug_review}

Security Review:
{security_review}

Performance Review:
{performance_review}
"""

prompt = PromptTemplate(
    template=raw_template,
    input_variables=[
        "bug_review",
        "security_review",
        "performance_review",
        "format_instructions",
    ],
)