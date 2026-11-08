import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class PluginManifestTest(unittest.TestCase):
    def test_every_sos_skill_is_in_the_plugin(self):
        manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        listed = {Path(p).name for p in manifest["skills"]}
        on_disk = {p.name for p in (ROOT / ".claude" / "skills").glob("sos-*") if (p / "SKILL.md").exists()}
        self.assertEqual(listed, on_disk)

    def test_listed_paths_exist(self):
        manifest = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        for p in manifest["skills"]:
            self.assertTrue((ROOT / p / "SKILL.md").exists(), p)


if __name__ == "__main__":
    unittest.main()
