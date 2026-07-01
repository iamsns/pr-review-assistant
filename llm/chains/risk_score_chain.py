from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.output_parsers import OutputFixingParser
from langchain_core.runnables import RunnableParallel

from schemas.risk_schema import RiskScoreResponse
from prompts.risk_score_prompt import prompt
from llm.llm_factory import LLMFactory
from llm.chains.bug_review_chain import chain as bug_review_chain
from llm.chains.security_review_chain import chain as security_review_chain
from llm.chains.performance_review_chain import chain as performance_review_chain

llm = LLMFactory.get_llm()

base_parser = PydanticOutputParser(pydantic_object=RiskScoreResponse)

parser = OutputFixingParser.from_llm(parser=base_parser, llm=llm)

final_prompt = prompt.partial(format_instructions=base_parser.get_format_instructions())

para_chain = RunnableParallel({
    "bug_review":bug_review_chain,
    "security_review":security_review_chain,
    "performance_review": performance_review_chain
})

chain = para_chain | final_prompt | llm | parser