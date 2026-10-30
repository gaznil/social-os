import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    out = subprocess.run([sys.executable, "-m", "tools.sos.cli", *args],
                         cwd=ROOT, capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


class Cli(unittest.TestCase):
    def setUp(self):
        posts = [
            {"id": "a", "platform": "linkedin", "format": "text", "caption": "Hi",
             "status": "approved", "approvedAt": "2026-11-01T10:00:00+05:30",
             "plannedAt": "2026-11-02T09:00:00+05:30", "mediaUrls": []},
            {"id": "b", "platform": "instagram", "format": "image", "caption": "Hi",
             "status": "approved", "approvedAt": "2026-11-01T10:00:00+05:30",
             "plannedAt": "2026-11-03T09:00:00+05:30", "mediaUrls": []},
        ]
        self.tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump(posts, self.tmp)
        self.tmp.close()

    def tearDown(self):
        Path(self.tmp.name).unlink()

    def test_due(self):
        res = run("due", self.tmp.name, "--now", "2026-11-02T10:00:00+05:30")
        self.assertEqual([p["id"] for p in res], ["a"])

    def test_check(self):
        res = run("check", self.tmp.name)
        self.assertEqual(res["a"], [])
        self.assertIn("Instagram needs at least one image or video.", res["b"])


if __name__ == "__main__":
    unittest.main()
