"""Core Semantic Diff Explainer implementation."""
import re
from typing import Dict, List, Any

class DiffSummary:
    def __init__(self, added_files: List[str], modified_files: List[str], added_functions: List[str], is_breaking: bool):
        self.added_files = added_files
        self.modified_files = modified_files
        self.added_functions = added_functions
        self.is_breaking = is_breaking

class SemanticDiffExplainer:
    @classmethod
    def explain_diff(cls, diff_text: str) -> DiffSummary:
        added_files = []
        modified_files = []
        added_functions = []
        is_breaking = False

        lines = diff_text.splitlines()
        current_file = ""

        for line in lines:
            if line.startswith("diff --git"):
                parts = line.split()
                if len(parts) >= 4:
                    current_file = parts[3].replace("b/", "")
                    modified_files.append(current_file)
            elif line.startswith("new file"):
                if current_file:
                    added_files.append(current_file)
                    if current_file in modified_files:
                        modified_files.remove(current_file)
            elif line.startswith("+def ") or line.startswith("+    def "):
                fn_name = re.findall(r"def\s+([a-zA-Z0-9_]+)", line)
                if fn_name:
                    added_functions.append(fn_name[0])
            elif line.startswith("-def ") or line.startswith("-    def "):
                # Deleting a function is potentially breaking
                is_breaking = True

        return DiffSummary(list(set(added_files)), list(set(modified_files)), added_functions, is_breaking)
