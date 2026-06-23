import re


class PROverviewService:

    def generate_overview(self, pr_diff: str):
        files = self._parse_files(pr_diff)

        return {
            "files_changed": len(files),
            "total_additions": sum(f["additions"] for f in files),
            "total_deletions": sum(f["deletions"] for f in files),
            "files": files,
        }

    def _parse_files(self, pr_diff: str):
        sections = re.split(r"(?=diff --git)", pr_diff)

        files = []

        for section in sections:
            if not section.strip():
                continue

            file_info = self._parse_file_section(section)

            if file_info:
                files.append(file_info)

        return files

    def _parse_file_section(self, section: str):

        match = re.search(
            r"diff --git a/(.*?) b/(.*?)\n",
            section
        )

        if not match:
            return None

        old_file = match.group(1)
        new_file = match.group(2)

        change_type = "modified"

        if "new file mode" in section:
            change_type = "added"

        elif "deleted file mode" in section:
            change_type = "deleted"

        elif "rename from" in section:
            change_type = "renamed"

        additions = 0
        deletions = 0

        for line in section.splitlines():

            if line.startswith("+++"):
                continue

            if line.startswith("---"):
                continue

            if line.startswith("+"):
                additions += 1

            elif line.startswith("-"):
                deletions += 1

        result = {
            "file_name": new_file,
            "change_type": change_type,
            "additions": additions,
            "deletions": deletions,
        }

        if change_type == "renamed":

            rename_from = re.search(
                r"rename from (.*)",
                section
            )

            rename_to = re.search(
                r"rename to (.*)",
                section
            )

            result["old_name"] = rename_from.group(1)
            result["new_name"] = rename_to.group(1)

        return result