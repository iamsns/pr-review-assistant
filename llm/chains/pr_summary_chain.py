from llm.llm_factory import LLMFactory
from prompts.pr_summary_prompt import prompt, parser

llm = LLMFactory.get_llm()


pr_summary_chain = prompt | llm | parser