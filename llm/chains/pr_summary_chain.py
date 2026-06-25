from llm.llm_factory import LLMFactory
from prompts.pr_summary_prompt import prompt

from langchain_core.output_parsers import PydanticOutputParser

from schemas.overview_schema import PRSummary

parser = PydanticOutputParser(pydantic_object=PRSummary)

llm = LLMFactory.get_llm()

prompt = prompt.partial(format_instructions=parser.get_format_instructions())

pr_summary_chain = prompt | llm | parser
