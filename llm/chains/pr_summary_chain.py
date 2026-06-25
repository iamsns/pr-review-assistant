from llm.llm_factory import LLMFactory
from prompts.pr_summary_prompt import prompt as pr_summary_prompt, parser as pr_summary_parser
from prompts.pr_files_summary_prompt import prompt as file_summary_prompt, parser as file_summary_parser

llm = LLMFactory.get_llm()


pr_summary_chain = pr_summary_prompt | llm | pr_summary_parser

pr_files_summary_chain = file_summary_prompt | llm | file_summary_parser