import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.sos import deepdive


def make_video(path, seconds=3):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"testsrc=size=640x360:rate=25:d={seconds}",
                    "-f", "lavfi", "-i", f"sine=frequency=440:duration={seconds}",
                    "-shortest", str(path)], check=True)


class DeepDive(unittest.TestCase):
    def setUp(self):
        self.dir = Path(tempfile.mkdtemp())
        self.video = self.dir / "v.mp4"
        make_video(self.video)

    def test_local_path_is_used_as_is(self):
        self.assertEqual(deepdive.fetch(str(self.video), self.dir), self.video)

    def test_contact_sheet_is_3_by_2_grid(self):
        sheet = deepdive.contact_sheet(self.video, self.dir / "frames.jpg")
        out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries",
                              "stream=width,height", "-of", "csv=p=0", str(sheet)],
                             capture_output=True, text=True, check=True)
        w, h = map(int, out.stdout.strip().split(","))
        self.assertEqual((w, h), (360 * 3, 202 * 2))

    def test_card_lists_timestamps_and_blank_formula(self):
        t = {"language": "en", "segments": [{"start": 0.0, "end": 1.2, "text": "Stop scrolling"}]}
        text = deepdive.card(t, "https://example.com/p/1")
        self.assertIn("- [0.0s] Stop scrolling", text)
        self.assertIn("## Formula (with blanks)", text)
        self.assertIn("Source: https://example.com/p/1", text)

    def test_elevenlabs_words_become_sentence_lines(self):
        words = [{"text": "Stop", "start": 0.0, "end": 0.3, "type": "word"},
                 {"text": " ", "start": 0.3, "end": 0.35, "type": "spacing"},
                 {"text": "scrolling.", "start": 0.35, "end": 0.9, "type": "word"},
                 {"text": " ", "start": 0.9, "end": 1.0, "type": "spacing"},
                 {"text": "Three", "start": 1.0, "end": 1.3, "type": "word"},
                 {"text": " ", "start": 1.3, "end": 1.35, "type": "spacing"},
                 {"text": "tools", "start": 1.35, "end": 1.8, "type": "word"}]
        self.assertEqual(deepdive.lines(words), [
            {"start": 0.0, "end": 0.9, "text": "Stop scrolling."},
            {"start": 1.0, "end": 1.8, "text": "Three tools"}])

    def test_card_without_speech(self):
        self.assertIn("(no speech)", deepdive.card({"language": "en", "segments": []}))


if __name__ == "__main__":
    unittest.main()
