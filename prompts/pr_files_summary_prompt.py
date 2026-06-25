from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from schemas.overview_schema import PRFileSummary

parser = PydanticOutputParser(pydantic_object=PRFileSummary)

template = """
You are a senior software engineer.

Analyze the following pull request changes and provide file level summary.

{format_instructions}

Return JSON.

PR Diff:

{diff}
"""

prompt = PromptTemplate(template=template, input_variables=["diff"], partial_variables={"format_instructions":parser.get_format_instructions()})