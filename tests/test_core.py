"""Tests for SemanticDiffExplainer."""
import unittest
from semantic_diff_change_explainer.core import SemanticDiffExplainer

class TestSemanticDiffExplainer(unittest.TestCase):
    def test_diff_parsing(self):
        diff = """diff --git a/api.py b/api.py
-def legacy_endpoint():
+def modern_endpoint():
"""
        res = SemanticDiffExplainer.explain_diff(diff)
        self.assertTrue(res.is_breaking)
        self.assertIn("modern_endpoint", res.added_functions)
        self.assertIn("api.py", res.modified_files)
