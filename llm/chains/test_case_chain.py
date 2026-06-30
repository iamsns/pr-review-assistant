from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.output_parsers import OutputFixingParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

from llm.llm_factory import LLMFactory
from schemas.review_schema import TestCaseResponse
from prompts.test_case_prompt import prompt
from llm.chains.pr_summary_chain import pr_summary_chain

llm = LLMFactory.get_llm()


base_parser = PydanticOutputParser(pydantic_object=TestCaseResponse)

parser = OutputFixingParser.from_llm(llm=llm, parser=base_parser)


final_prompt = prompt.partial(format_instructions=base_parser.get_format_instructions())


para_chain = RunnableParallel({
    "summary": pr_summary_chain,
    "diff": RunnablePassthrough()
})

test_case_chain = final_prompt | llm | parser

chain = para_chain | test_case_chain