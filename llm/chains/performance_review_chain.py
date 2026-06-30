from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.output_parsers import OutputFixingParser

from schemas.review_schema import PerformanceReviewResponse
from prompts.performance_review_prompt import prompt
from llm.llm_factory import LLMFactory

llm = LLMFactory.get_llm()

base_parser = PydanticOutputParser(pydantic_object=PerformanceReviewResponse)

parser = OutputFixingParser.from_llm(parser=base_parser, llm=llm)

final_prompt = prompt.partial(format_instructions=base_parser.get_format_instructions())

chain = final_prompt | llm | parser

chain.get_graph().print_ascii()