import unittest

from tools.sos import radar


class RadarUrlsTest(unittest.TestCase):
    def test_extracts_and_dedups_tracking_params_and_ig_variants(self):
        text = """Check these out:
        https://www.instagram.com/reel/ABC123/?igsh=xyz123
        https://instagram.com/p/ABC123/
        https://www.instagram.com/reels/ABC123/
        https://youtu.be/dQw4w9WgXcQ?si=trackme
        https://x.com/user/status/999?s=20&t=abc
        https://www.youtube.com/watch?v=keep123&search=ai&si=stripme&utm_source=ig"""
        got = radar.extract_urls(text)
        self.assertEqual(got, [
            {"url": "https://instagram.com/reel/ABC123", "platform": "instagram"},
            {"url": "https://youtu.be/dQw4w9WgXcQ", "platform": "youtube"},
            {"url": "https://x.com/user/status/999", "platform": "x"},
            {"url": "https://youtube.com/watch?v=keep123&search=ai", "platform": "youtube"},
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

    def test_live_trend_outranks_evergreen_and_expired_sinks(self):
        now = "2026-11-21T12:00:00Z"
        items = [
            {
                "id": "evergreen-p1",
                "url": "https://instagram.com/reel/ev1",
                "outlierMultiple": 8.0,
                "ageDays": 3,
                "hookScore": 85,
                "fitScore": 88,
                "effort": "low",
                "shelfLife": "evergreen",
            },
            {
                "id": "live-update",
                "url": "https://github.com/org/repo",
                "outlierMultiple": 7.5,
                "ageDays": 1,
                "hookScore": 84,
                "fitScore": 86,
                "firstMover": "untapped",
                "effort": "low",
                "shelfLife": "update",
                "expiresAt": "2026-11-22T06:00:00Z",
            },
            {
                "id": "expired-update",
                "url": "https://x.com/u/status/1",
                "outlierMultiple": 12.0,
                "ageDays": 6,
                "hookScore": 92,
                "fitScore": 90,
                "effort": "low",
                "shelfLife": "update",
                "expiresAt": "2026-11-18T12:00:00Z",
            },
        ]
        ranked = radar.rank_inspirations(items, now=now)
        self.assertEqual([x["id"] for x in ranked], ["live-update", "evergreen-p1", "expired-update"])
        self.assertEqual(ranked[0]["expiryState"], "expiring_today")
        self.assertEqual(ranked[2]["tier"], "expired")
        self.assertEqual(ranked[2]["expiryState"], "expired")


if __name__ == "__main__":
    unittest.main()
