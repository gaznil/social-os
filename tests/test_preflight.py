import unittest

from tools.sos import preflight


def post(**kw):
    base = {"platform": "linkedin", "format": "text", "title": "",
            "caption": "A real post.", "mediaUrls": [], "status": "waiting",
            "approvedAt": None}
    base.update(kw)
    return base


class Common(unittest.TestCase):
    def test_clean_post_has_no_problems(self):
        self.assertEqual(preflight.check(post()), [])

    def test_unknown_platform(self):
        self.assertIn("Unknown platform: myspace", preflight.check(post(platform="myspace")))

    def test_empty_caption(self):
        self.assertIn("Caption is empty.", preflight.check(post(caption="  ")))

    def test_approved_needs_time(self):
        self.assertIn("Approved but no approval time recorded.",
                      preflight.check(post(status="approved")))


class Instagram(unittest.TestCase):
    def ig(self, **kw):
        fields = {"platform": "instagram", "format": "image",
                  "mediaUrls": ["https://cdn.example.com/a.jpg"]}
        fields.update(kw)
        return post(**fields)

    def test_needs_media(self):
        p = self.ig()
        p["mediaUrls"] = []
        self.assertIn("Instagram needs at least one image or video.", preflight.check(p))

    def test_hashtag_cap(self):
        cap = "Post " + " ".join(f"#t{i}" for i in range(6))
        self.assertIn("Instagram allows 5 hashtags; this has 6.", preflight.check(self.ig(caption=cap)))

    def test_query_in_url(self):
        p = self.ig()
        p["mediaUrls"] = ["https://cdn.example.com/a.jpg?sig=1"]
        self.assertIn("Media link has '?' in it; Instagram often refuses those: https://cdn.example.com/a.jpg?sig=1",
                      preflight.check(p))

    def test_caption_length(self):
        self.assertIn("Caption is 2201 characters; instagram allows 2200.",
                      preflight.check(self.ig(caption="a" * 2201)))

    def test_story_needs_exactly_one_media(self):
        p = self.ig(format="story")
        p["mediaUrls"] = ["https://cdn.example.com/a.jpg", "https://cdn.example.com/b.jpg"]
        self.assertIn("A story is one image or video; this has 2.", preflight.check(p))

    def test_carousel_size(self):
        p = self.ig(format="carousel")
        p["mediaUrls"] = ["https://cdn.example.com/a.jpg"]
        self.assertIn("A carousel needs 2 to 10 images; this has 1.", preflight.check(p))


class X(unittest.TestCase):
    def test_weighted_length_counts_links_as_23(self):
        cap = "a" * 250 + " https://example.com/a/very/long/path/that/is/long"
        self.assertEqual(preflight.check(post(platform="x", caption=cap)), [])

    def test_too_long(self):
        self.assertIn("Post is 281 weighted characters; x allows 280.",
                      preflight.check(post(platform="x", caption="a" * 281)))

    def test_wide_characters_count_double(self):
        self.assertIn("Post is 282 weighted characters; x allows 280.",
                      preflight.check(post(platform="x", caption="😀" * 141)))


class YouTube(unittest.TestCase):
    def test_needs_title_and_video(self):
        problems = preflight.check(post(platform="youtube", format="video"))
        self.assertIn("YouTube needs a title.", problems)
        self.assertIn("YouTube needs a video file.", problems)

    def test_title_length(self):
        p = post(platform="youtube", format="video", title="t" * 101,
                 mediaUrls=["C:/videos/a.mp4"])
        self.assertIn("Title is 101 characters; YouTube allows 100.", preflight.check(p))


if __name__ == "__main__":
    unittest.main()
