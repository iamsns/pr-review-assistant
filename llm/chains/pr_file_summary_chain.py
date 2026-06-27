from langchain_core.output_parsers import PydanticOutputParser

from llm.llm_factory import LLMFactory
from prompts.pr_files_summary_prompt import prompt
from schemas.overview_schema import PRFileSummary

llm = LLMFactory.get_llm()

parser = PydanticOutputParser(pydantic_object=PRFileSummary)

prompt = prompt.partial(format_instructions=parser.get_format_instructions())

pr_files_summary_chain = prompt | llm | parser