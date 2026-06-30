from services.github_service import GithubService
from services.pr_overview_service import PROverviewService
from schemas.overview_schema import PROverviewRequest
from llm.chains.bug_review_chain import chain as bug_review_chain
from llm.chains.review_comment_chain import chain as review_comment_chain
from llm.chains.security_review_chain import chain as security_review_chain
from llm.chains.performance_review_chain import chain as performance_review_chain
from llm.chains.test_case_chain import chain as test_case_chain

class ReviewService:
    
    def __init__(self):
        self.github_service = GithubService()
        self.overview_service = PROverviewService()

    def get_bug_review(self, pr_data: PROverviewRequest):
        overview = self.overview_service.generate_overview(pr_data)
        if overview:
            return bug_review_chain.invoke({"diff":overview})

        return "Invalid Data"
    
    def get_review_comments(self, pr_data:PROverviewRequest):
        overview = self.overview_service.generate_overview(pr_data)
        if overview:
            print("Overview:- ", overview)
            return review_comment_chain.invoke({"diff":overview})

        return "Invalid Data"
    
    def get_security_review(self, pr_data:PROverviewRequest):
        overview = self.overview_service.generate_overview(pr_data)
        if overview:
            print("Overview:- ", overview)
            return security_review_chain.invoke({"diff":overview})

        return "Invalid Data"
    
    def get_performance_review(self, pr_data:PROverviewRequest):
        overview = self.overview_service.generate_overview(pr_data)
        if overview:
            print("Overview:- ", overview)
            return performance_review_chain.invoke({"diff":overview})

        return "Invalid Data"
    
    
    def generate_test_case(self, pr_data:PROverviewRequest):
        overview = self.overview_service.generate_overview(pr_data)
        if overview:
            print("Overview:- ", overview)
            return test_case_chain.invoke({"diff":overview})

        return "Invalid Data"
    
    