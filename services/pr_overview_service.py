import re
from services.github_service import GithubService
from schemas.overview_schema import PROverviewRequest, PROverviewData

from utils.github_url_parser import get_pr_metadata
from llm.chains.pr_summary_chain import pr_summary_chain

class PROverviewService:
    def __init__(self):
        self.github_service = GithubService()

    def generate_overview(self, pr_data: PROverviewRequest):
        if pr_data.url:
            pr_metadata = get_pr_metadata(pr=pr_data.url)
            if pr_metadata is None:
                raise Exception("Invalid pr url")
            else:
                return self.github_service.get_pr_files_overview(pr_metadata)
        else:
            pr_metadata = pr_data.model_dump()
            return self.github_service.get_pr_files_overview(pr_metadata)
       
    def get_pr_summary(self, pr_overview: PROverviewData):
        print(pr_overview)
        return pr_summary_chain.invoke({"diff":pr_overview})