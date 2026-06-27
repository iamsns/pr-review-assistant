from langchain_core.prompts import PromptTemplate

template = """
You are a senior application security reviewer.

Review ONLY the changed code in this pull request.

Identify security issues including:

- SQL Injection
- XSS
- Secrets
- Authentication
- Authorization
- SSRF
- Command Injection
- Path Traversal
- Unsafe Deserialization
- Weak Cryptography

Only report real issues.

If none exist, return

{{
  "security_issues": []
}}

{format_instructions}

PR Diff:

{diff}

Do NOT wrap it in markdown.

Do NOT write explanations.

Do NOT write "This answer satisfies..."

Do NOT use ```json or ```python.
"""


prompt = PromptTemplate(template=template, input_variables=["diff", "format_instructions"])