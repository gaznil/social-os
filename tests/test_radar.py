import unittest

from tools.sos import radar


class RadarUrlsTest(unittest.TestCase):
    def test_extracts_and_dedups_tracking_params(self):
        text = """Check these out:
        https://www.instagram.com/reel/ABC123/?igsh=xyz123
        https://www.instagram.com/reel/ABC123/
        https://youtu.be/dQw4w9WgXcQ?si=trackme
        https://x.com/user/status/999?s=20&t=abc"""
        got = radar.extract_urls(text)
        self.assertEqual(got, [
            {"url": "https://www.instagram.com/reel/ABC123", "platform": "instagram"},
            {"url": "https://youtu.be/dQw4w9WgXcQ", "platform": "youtube"},
            {"url": "https://x.com/user/status/999", "platform": "x"},
        ])


class RadarScoringTest(unittest.TestCase):
    def test_ranks_hot_outlier_above_weak_and_unprovable(self):
        items = [
            {"id": "weak", "url": "https://instagram.com/reel/1", "outlierMultiple": 1.1, "ageDays": 40, "hookScore": 35, "fitScore": 40, "effort": "high"},
            {"id": "hot", "url": "https://instagram.com/reel/2", "outlierMultiple": 12.5, "ageDays": 2, "hookScore": 88, "fitScore": 90, "effort": "low"},
            {"id": "fake", "url": "https://instagram.com/reel/3", "outlierMultiple": 15.0, "ageDays": 1, "hookScore": 90, "fitScore": 90, "provable": False, "effort": "low"},
        ]
        ranked = radar.rank_inspirations(items)
        self.assertEqual(ranked[0]["id"], "hot")
        self.assertEqual(ranked[0]["tier"], "P1")
        self.assertGreaterEqual(ranked[0]["score"], 85)
        fake = next(x for x in ranked if x["id"] == "fake")
        self.assertEqual(fake["tier"], "skip")
        weak = next(x for x in ranked if x["id"] == "weak")
        self.assertIn(weak["tier"], ("P3", "skip"))


if __name__ == "__main__":
    unittest.main()
