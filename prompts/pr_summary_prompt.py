from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from schemas.overview_schema import PRSummary

parser = PydanticOutputParser(pydantic_object=PRSummary)

raw_template = """
You are a senior software engineer.

Analyze the following pull request changes.

Provide:

1. Overall Summary
2. Key Changes

{format_instructions}

Return JSON.

PR Diff:

{diff}
"""

prompt = PromptTemplate(template=raw_template, input_variables=["diff"], partial_variables={'format_instructions':parser.get_format_instructions()})
