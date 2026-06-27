from langchain_core.prompts import PromptTemplate

template = """
You are a senior software engineer.

Analyze the following pull request changes and provide file level summary.

{format_instructions}

Return JSON.

PR Diff:

{diff}
"""

prompt = PromptTemplate(template=template, input_variables=["diff", "format_instructions"])