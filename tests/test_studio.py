import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.sos.studio import check_job, pack_plan

ROOT = Path(__file__).resolve().parents[1]

ACC = [
    {"id": "ig-a", "platform": "instagram", "status": "active"},
    {"id": "li-a", "platform": "linkedin", "status": "active"},
    {"id": "x-a", "platform": "x", "status": "setup"},
]


class StudioTest(unittest.TestCase):
    def test_ok_job(self):
        self.assertEqual(check_job({"accountId": "ig-a", "kind": "prompt", "brief": "a reel"}), [])

    def test_clip_only_is_ok(self):
        self.assertEqual(check_job({"accountId": "ig-a", "kind": "prompt", "clipUrl": "clip.mp4"}), [])

    def test_needs_brief_or_clip(self):
        self.assertTrue(check_job({"accountId": "ig-a", "kind": "prompt", "brief": "  "}))

    def test_bad_kind(self):
        self.assertTrue(check_job({"accountId": "ig-a", "kind": "run", "brief": "x"}))

    def test_needs_account(self):
        self.assertTrue(check_job({"kind": "pack", "brief": "x"}))

    def test_pack_plan(self):
        plan = pack_plan({"accountId": "ig-a", "kind": "pack", "brief": "x"}, ACC)
        self.assertEqual(plan, [
            {"accountId": "ig-a", "platform": "instagram", "format": "carousel"},
            {"accountId": "li-a", "platform": "linkedin", "format": "text"},
        ])

    def test_prompt_job_has_no_pack(self):
        self.assertEqual(pack_plan({"accountId": "ig-a", "kind": "prompt", "brief": "x"}, ACC), [])


class StudioCli(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.job = Path(self.dir.name, "job.json")
        self.acc = Path(self.dir.name, "accounts.json")
        self.job.write_text(json.dumps({"accountId": "ig-a", "kind": "pack", "brief": "x"}))
        self.acc.write_text(json.dumps(ACC))

    def tearDown(self):
        self.dir.cleanup()

    def run_cli(self, *args):
        out = subprocess.run([sys.executable, "-m", "tools.sos.cli", *args],
                             cwd=ROOT, capture_output=True, text=True, check=True)
        return json.loads(out.stdout)

    def test_studio_check(self):
        self.assertEqual(self.run_cli("studio-check", str(self.job)), [])

    def test_pack_plan(self):
        res = self.run_cli("pack-plan", str(self.job), str(self.acc))
        self.assertEqual([t["accountId"] for t in res], ["ig-a", "li-a"])


if __name__ == "__main__":
    unittest.main()
