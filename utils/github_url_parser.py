import re

def get_pr_metadata(pr: str):         
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