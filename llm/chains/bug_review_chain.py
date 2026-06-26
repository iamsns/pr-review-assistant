from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.output_parsers import OutputFixingParser

from prompts.bug_review_prompt import prompt
from schemas.review_schema import BugReviewResponse
from llm.llm_factory import LLMFactory


llm = LLMFactory.get_llm()

# Base parser
base_parser = PydanticOutputParser(
    pydantic_object=BugReviewResponse
)

# Auto-fixing parser
parser = OutputFixingParser.from_llm(
    parser=base_parser,
    llm=llm
)

prompt = prompt.partial(format_instructions=base_parser.get_format_instructions())

chain = prompt | llm | parser
