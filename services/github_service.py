import re
from typing import List

import requests

from schemas.overview_schema import FileChange, PROverviewData


class GithubService:

    def _fetch_pr_files(self, url: str) -> list[dict]:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    
    def get_pr_files_overview(self, pr_data: dict) -> PROverviewData:
        try:
            print("pr_data", pr_data)
            gh_pr_endpoint = f"https://api.github.com/repos/{pr_data["owner"]}/{pr_data["repo"]}/pulls/{pr_data["pr_number"]}/files"
            files_data = self._fetch_pr_files(gh_pr_endpoint)
            print("files_data", files_data)
            files = [
                FileChange(
                    file_name=file["filename"],
                    change_type=file["status"],
                    additions=file["additions"],
                    deletions=file["deletions"],
                    changes=file["changes"]
                )
                for file in files_data
            ]

            return PROverviewData(
                files_changed=len(files),
                files=files,
                total_additions=sum(file["additions"] for file in files_data),
                total_deletions=sum(file["deletions"] for file in files_data),
            )

        except requests.RequestException as e:
            raise Exception(f"Failed to fetch PR details: {str(e)}")
        
    def get_pr_metadata(self, pr: str):         
        pattern = r"github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)/pull/(?P<pr_number>\d+)/?$"

        match = re.search(pattern, pr)

        if match:
            # Extract data as a clean dictionary
            data = match.groupdict()
            print("Extracted Data:", data)
            
            # Access individual components directly
            print(f"Owner:   {data['owner']}")
            print(f"Repo:    {data['repo']}")
            print(f"PR Num:  {data['pr_number']}")
            data['pr_number'] = int(data['pr_number'])
            return data
        else:
            print("The URL does not match a standard GitHub Pull Request format.")
            return None