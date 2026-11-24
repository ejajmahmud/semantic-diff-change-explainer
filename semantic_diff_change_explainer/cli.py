"""CLI for Semantic Diff Explainer."""
import argparse
from .core import SemanticDiffExplainer

def main():
    parser = argparse.ArgumentParser(description="Semantic Diff Change Explainer CLI")
    parser.add_argument("--demo", action="store_true", help="Run diff explainer demo")
    args = parser.parse_args()

    sample_diff = """diff --git a/core.py b/core.py
--- a/core.py
+++ b/core.py
@@ -10,1 +10,4 @@
+def new_feature_helper():
+    return True
"""
    summary = SemanticDiffExplainer.explain_diff(sample_diff)
    print("Semantic Diff Analysis:")
    print("  Modified files:", summary.modified_files)
    print("  Added functions:", summary.added_functions)
    print("  Breaking change:", summary.is_breaking)

if __name__ == "__main__":
    main()
