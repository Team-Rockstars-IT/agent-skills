"""Behavior checks for filtering, evidence scope and generated-document integrity."""
import copy
import json
import subprocess
import sys
import unittest

import skill_catalog as catalog


class SkillCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = catalog.load()

    def test_dutch_goal_search_and_combined_filters(self):
        rows = catalog.search(self.data, "TERUGBLIK", category="development",
                              language="ts", source="matt", evidence="source-reviewed")
        self.assertEqual([r["id"] for r in rows], ["matt-retro"])
        self.assertEqual(catalog.search(self.data, "terugblik", category="security-privacy"), [])

    def test_language_matches_cross_language_and_exact_but_not_other_stacks(self):
        neutral = copy.deepcopy(self.data[0])
        python = {**neutral, "id": "python-only", "programming_languages": ["python"]}
        typescript = {**neutral, "id": "typescript-only", "programming_languages": ["typescript"]}
        rows = catalog.search([neutral, python, typescript], language="py")
        self.assertEqual([r["id"] for r in rows], ["python-only", neutral["id"]])
        self.assertEqual(catalog.search([python], language="typescript"), [])

    def test_default_language_badge_is_hidden_but_explicit_restrictions_remain(self):
        neutral = self.data[0]
        self.assertNotIn("language:any", catalog.table([neutral], "recipes/minimal-agent-workflow.md"))
        self.assertEqual(neutral["programming_languages"], ["any"])
        restricted = {**neutral, "programming_languages": ["python"]}
        self.assertIn("language:python", catalog.table([restricted], "recipes/minimal-agent-workflow.md"))

    def test_core_recipes_disclose_specialist_choices_only_on_demand(self):
        generated = catalog.documents(self.data)
        for recipe in catalog.CORE_RECIPES - {"recipes/choose-your-setup.md"}:
            text = generated[recipe]
            self.assertIn("<summary>Optional specialist workflows</summary>", text)
            self.assertLess(text.index("## Steps"), text.index(catalog.START))
        self.assertNotIn("<summary>Optional specialist workflows</summary>",
                         generated["recipes/spec-driven-development.md"])

    def test_instruction_language_cannot_be_used_as_programming_language(self):
        result = subprocess.run([sys.executable, str(catalog.ROOT / "scripts/skill_catalog.py"),
                                 "search", "--language", "nl"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid choice", result.stderr)

    def test_specification_tools_are_alternatives_to_a_skill(self):
        tools = catalog.search(self.data, goal="specification", kind="tool")
        skills = catalog.search(self.data, goal="specification", kind="skill")
        self.assertEqual({r["id"] for r in tools}, {"openspec", "spec-kit"})
        self.assertEqual([r["id"] for r in skills], ["addy-spec-driven-development"])
        for row in tools:
            rendered = catalog.table([row], "recipes/spec-driven-development.md")
            self.assertIn("(tool)", rendered)
            self.assertNotIn("/" + row["name"] + "]", rendered)

    def test_tdd_evaluation_does_not_leak_to_collection_or_new_revision(self):
        tested = catalog.search(self.data, source="Matt", evidence="locally-tested")
        self.assertEqual([r["id"] for r in tested], ["matt-tdd"])
        self.assertIn("a496f5513d4a4cf889bc48e189e579f4b0bdf6aa", tested[0]["upstream"])
        self.assertIn("synthetic", tested[0]["evidence_scope"])
        spec = catalog.search(self.data, goal="specification", kind="skill")[0]
        self.assertIn("phase only", spec["evidence_scope"])

    def test_marked_updates_preserve_surrounding_user_content_and_are_idempotent(self):
        block = catalog.START + "\nnew table\n" + catalog.END
        old = "intro\n" + catalog.START + "\nold table\n" + catalog.END + "\nuser notes\n"
        expected = "intro\n" + block + "\nuser notes\n"
        self.assertEqual(catalog.replace_block(old, block), expected)
        self.assertEqual(catalog.replace_block(expected, block), expected)
        with self.assertRaises(ValueError):
            catalog.replace_block("intro\n" + catalog.START, block)

    def test_metadata_rejects_unpinned_sources_duplicates_and_invalid_language_tags(self):
        data = copy.deepcopy(self.data)
        data[0]["upstream"] = data[0]["upstream"].replace("a496f5513d4a4cf889bc48e189e579f4b0bdf6aa", "main")
        data[1]["id"] = data[0]["id"]
        data[2]["programming_languages"] = ["any", "python"]
        errors = catalog.validate(data)
        self.assertTrue(any("exact Markdown source revision" in e for e in errors))
        self.assertTrue(any("duplicate" in e for e in errors))
        self.assertTrue(any("invalid programming languages" in e for e in errors))

    def test_cli_json_from_another_directory_and_no_results(self):
        command = [sys.executable, str(catalog.ROOT / "scripts/skill_catalog.py"), "search"]
        result = subprocess.run(command + ["specificatie", "--kind", "tool", "--language", "c#", "--json"],
                                cwd=catalog.ROOT.parent, capture_output=True, text=True, check=True)
        self.assertEqual({r["id"] for r in json.loads(result.stdout)}, {"openspec", "spec-kit"})
        empty = subprocess.run(command + ["not-a-known-outcome", "--json"],
                               capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(empty.stdout), [])

    def test_generated_views_match_and_cover_each_recipe_choice(self):
        self.assertEqual(catalog.check_generated(), [])
        for row in self.data:
            for recipe in row["recipes"]:
                text = (catalog.ROOT / recipe).read_text(encoding="utf-8")
                self.assertIn(row["upstream"], text)
                self.assertIn(row["evidence_scope"], text)

    def test_removing_a_choice_also_removes_obsolete_recipe_tables(self):
        remaining = [row for row in self.data if row["id"] != "matt-retro"]
        generated = catalog.documents(remaining)
        retro = generated["recipes/session-retrospective.md"]
        self.assertNotIn(catalog.START, retro)
        self.assertNotIn("## Upstream choices", retro)
        self.assertIn("## Steps", retro)
        self.assertIn("## Ask an agent", retro)


if __name__ == "__main__":
    unittest.main()
