class ReviewService:

    def process_diff(self, pr_diff: str):

        if not pr_diff.strip():
            raise ValueError("PR diff cannot be empty")

        return {"success": True, "message": "PR diff received successfully"}
