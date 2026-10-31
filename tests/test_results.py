import unittest

from tools.sos.results import best_times, growth_tiles


def post(acc, at, views, status="posted"):
    return {"accountId": acc, "status": status, "postedAt": at, "metrics": {"views": views}}


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
