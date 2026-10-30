import unittest
from datetime import datetime, timezone, timedelta

from tools.sos import queue

IST = timezone(timedelta(hours=5, minutes=30))
NOW = datetime(2026, 11, 2, 19, 0, tzinfo=IST)


def post(**kw):
    base = {"id": "p1", "platform": "linkedin", "status": "approved",
            "plannedAt": "2026-11-02T18:00:00+05:30"}
    base.update(kw)
    return base


class CanMove(unittest.TestCase):
    def test_normal_path(self):
        for old, new in [("draft", "waiting"), ("waiting", "approved"),
                         ("approved", "posting"), ("posting", "posted")]:
            self.assertTrue(queue.can_move(old, new), (old, new))

    def test_cannot_skip_approval(self):
        self.assertFalse(queue.can_move("draft", "approved"))
        self.assertFalse(queue.can_move("waiting", "posting"))

    def test_posted_is_final(self):
        for s in queue.STATUSES:
            self.assertFalse(queue.can_move("posted", s))

    def test_failed_can_be_reapproved(self):
        self.assertTrue(queue.can_move("failed", "approved"))

    def test_unknown_status(self):
        self.assertFalse(queue.can_move("banana", "approved"))


class ParseTime(unittest.TestCase):
    def test_offset_required(self):
        with self.assertRaises(ValueError):
            queue.parse_time("2026-11-02T18:00:00")

    def test_z_suffix(self):
        self.assertEqual(queue.parse_time("2026-11-02T12:30:00Z"),
                         datetime(2026, 11, 2, 18, 0, tzinfo=IST))


class DuePosts(unittest.TestCase):
    def test_only_approved_and_past(self):
        posts = [post(id="a"),
                 post(id="b", status="waiting"),
                 post(id="c", plannedAt="2026-11-02T20:00:00+05:30"),
                 post(id="d", status="posted")]
        self.assertEqual([p["id"] for p in queue.due_posts(posts, NOW)], ["a"])

    def test_oldest_first(self):
        posts = [post(id="late", plannedAt="2026-11-02T18:30:00+05:30"),
                 post(id="early", plannedAt="2026-11-02T09:00:00+05:30")]
        self.assertEqual([p["id"] for p in queue.due_posts(posts, NOW)],
                         ["early", "late"])

    def test_manual_platforms_never_due(self):
        posts = [post(id="x1", platform="x"), post(id="t1", platform="threads")]
        self.assertEqual(queue.due_posts(posts, NOW), [])

    def test_missing_time_skipped(self):
        self.assertEqual(queue.due_posts([post(plannedAt=None)], NOW), [])


if __name__ == "__main__":
    unittest.main()
