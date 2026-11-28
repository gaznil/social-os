import unittest

from tools.sos.results import best_times, find_heaters, growth_metrics, growth_tiles


def post(acc, at, views, status="posted", pid=None, shelf="evergreen"):
    return {
        "id": pid or at,
        "accountId": acc,
        "status": status,
        "postedAt": at,
        "shelfLife": shelf,
        "metrics": {"views": views},
    }


class BestTimesTest(unittest.TestCase):
    def test_ranks_hours_in_india_time(self):
        posts = [post("ig-a", "2026-10-01T13:30:00Z", 900),   # 19:00 IST
                 post("ig-a", "2026-10-02T13:30:00Z", 1100),
                 post("ig-a", "2026-10-03T03:30:00Z", 200),   # 09:00 IST
                 post("ig-a", "2026-10-04T03:30:00Z", 300),
                 post("ig-a", "2026-10-05T07:30:00Z", 500),   # 13:00 IST
                 post("ig-a", "2026-10-06T07:30:00Z", 500)]
        self.assertEqual(best_times(posts), {"ig-a": ["19:00", "13:00", "09:00"]})

    def test_too_few_posts(self):
        self.assertEqual(best_times([post("ig-a", "2026-10-01T13:30:00Z", 9)]), {"ig-a": None})

    def test_skips_unposted_and_unmeasured(self):
        posts = [post("ig-a", "2026-10-01T13:30:00Z", 9, status="approved"),
                 {"accountId": "ig-a", "status": "posted", "postedAt": "2026-10-01T13:30:00Z"}]
        self.assertEqual(best_times(posts), {})


STATS = [
    {"accountId": "ig-a", "date": "2026-10-20", "followers": 100, "views": 50, "posts": 1},
    {"accountId": "ig-a", "date": "2026-10-27", "followers": 120, "views": 70, "posts": 2},
    {"accountId": "ig-a", "date": "2026-10-31", "followers": 130, "views": 30, "posts": 1},
    {"accountId": "li-a", "date": "2026-10-31", "followers": 40, "views": 10, "posts": 0},
]


class GrowthTilesTest(unittest.TestCase):
    def test_one_account(self):
        self.assertEqual(growth_tiles(STATS, "ig-a", "2026-10-31"),
                         {"followers": 130, "viewsWeek": 100, "postsWeek": 3, "change": 30})

    def test_all_accounts(self):
        t = growth_tiles(STATS, "all", "2026-10-31")
        self.assertEqual((t["followers"], t["viewsWeek"]), (170, 110))

    def test_no_data(self):
        self.assertEqual(growth_tiles([], "ig-a", "2026-10-31"),
                         {"followers": None, "viewsWeek": 0, "postsWeek": 0, "change": None})

    def test_skips_null_followers(self):
        stats = [
            {"accountId": "ig-a", "date": "2026-10-30", "followers": 100, "views": 20, "posts": 1},
            {"accountId": "ig-a", "date": "2026-10-31", "followers": None, "views": 10, "posts": 0},
        ]
        t = growth_tiles(stats, "ig-a", "2026-10-31")
        self.assertEqual(t["followers"], 100)
        self.assertEqual(t["viewsWeek"], 30)


class HeatersTest(unittest.TestCase):
    def test_finds_2x_outliers_and_flags_90d_evergreen_recycle(self):
        posts = [
            post("ig-a", "2026-07-01T13:30:00Z", 4200, pid="old-winner", shelf="evergreen"),
            post("ig-a", "2026-11-10T13:30:00Z", 1000, pid="p2"),
            post("ig-a", "2026-11-12T13:30:00Z", 900, pid="p3"),
            post("ig-a", "2026-11-15T13:30:00Z", 1100, pid="p4"),
            post("ig-a", "2026-11-18T13:30:00Z", 2500, pid="recent-heater", shelf="trend"),
        ]
        got = find_heaters(posts, today="2026-11-21")
        self.assertEqual([h["id"] for h in got], ["old-winner", "recent-heater"])
        self.assertTrue(got[0]["evergreenRecycle"])
        self.assertFalse(got[1]["evergreenRecycle"])


class ScorecardTest(unittest.TestCase):
    def mk(self, pid, views, reach, shares, likes, watch=None):
        return {"id": pid, "accountId": "ig-a", "status": "posted", "format": "reel",
                "metrics": {"views": views, "reach": reach, "shares": shares, "likes": likes, "avgWatchSec": watch}}

    def test_rates_and_multiples_vs_own_median(self):
        from tools.sos.results import scorecard, signal_rates
        self.assertEqual(signal_rates({"reach": 100, "shares": 5, "likes": 10})["sharesPerReach"], 0.05)
        self.assertIsNone(signal_rates({"reach": 0, "shares": 5})["sharesPerReach"])
        posts = [self.mk("a", 1000, 800, 8, 40), self.mk("b", 1200, 900, 9, 45),
                 self.mk("c", 900, 700, 7, 35), self.mk("star", 800, 400, 40, 60)]
        cards = {c["id"]: c for c in scorecard(posts)}
        self.assertGreater(cards["star"]["multiples"]["sharesPerReach"], 4)
        self.assertIsNone(cards["a"]["multiples"]["avgWatchSec"])  # no watch data -> None, not 0
        self.assertEqual(scorecard(posts)[0]["id"], "star")  # ranked by signals, not views

    def test_under_three_posts_has_no_multiple(self):
        from tools.sos.results import scorecard
        c = scorecard([self.mk("a", 10, 10, 1, 1), self.mk("b", 10, 10, 1, 1)])
        self.assertIsNone(c[0]["signalMean"])

    def test_heaters_keep_old_shape_and_add_signals(self):
        posts = [post("ig-a", "2026-11-10T13:30:00Z", 1000, pid="p1"), post("ig-a", "2026-11-12T13:30:00Z", 900, pid="p2"),
                 post("ig-a", "2026-11-15T13:30:00Z", 1100, pid="p3"), post("ig-a", "2026-11-18T13:30:00Z", 2500, pid="h")]
        got = find_heaters(posts, today="2026-11-21")
        self.assertEqual(got[0]["id"], "h")
        self.assertIn("multiple", got[0])


class GrowthMetricsTest(unittest.TestCase):
    STATS = [
        {"accountId": "ig-a", "date": "2026-10-31", "reach": 300, "likes": 10, "views": 100, "followerGain": 5},
        {"accountId": "ig-a", "date": "2026-10-30", "reach": 200, "likes": 20, "views": 100, "followerGain": 3},
        {"accountId": "ig-a", "date": "2026-10-20", "reach": 250, "views": 100},   # previous window
        {"accountId": "ig-b", "date": "2026-10-31", "reach": 50, "views": 10},
    ]

    def test_week_prev_and_pct(self):
        m = growth_metrics(self.STATS, "ig-a", "2026-10-31")
        self.assertEqual(m["reach"], {"week": 500, "prev": 250, "pct": 100})
        self.assertEqual(m["views"]["pct"], 100)
        self.assertEqual(m["likes"]["week"], 30)

    def test_missing_field_is_none_not_zero(self):
        m = growth_metrics(self.STATS, "ig-a", "2026-10-31")
        self.assertIsNone(m["profileViews"]["week"])
        self.assertIsNone(m["followerGain"]["pct"])

    def test_all_accounts_adds_up(self):
        self.assertEqual(growth_metrics(self.STATS, "all", "2026-10-31")["reach"]["week"], 550)
