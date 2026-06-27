from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.output_parsers import OutputFixingParser
from langchain_core.runnables import RunnableParallel

from llm.llm_factory import LLMFactory
from llm.chains.pr_summary_chain import pr_summary_chain
from llm.chains.bug_review_chain import chain as bug_review_chain
from prompts.bug_review_comment_prompt import prompt
from schemas.review_schema import  ReviewCommentsResponse

llm = LLMFactory.get_llm()

# Base parser
base_parser = PydanticOutputParser(
    pydantic_object=ReviewCommentsResponse
)

# Auto-fixing parser
parser = OutputFixingParser.from_llm(
    parser=base_parser,
    llm=llm
)

prompt = prompt.partial(
    format_instructions=base_parser.get_format_instructions()
)

review_comment_chain = prompt | llm | parser

para_chain = RunnableParallel({
    "pr_summary": pr_summary_chain,
    "issues":bug_review_chain
})

chain = para_chain | review_comment_chain

chain.get_graph().print_ascii()