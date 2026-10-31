"""Video studio jobs: check a job and plan the 'one video -> pack' drafts."""

KINDS = ("prompt", "pack")
PACK_FORMAT = {"instagram": "carousel", "linkedin": "text", "x": "thread", "threads": "text",
               "facebook": "text", "youtube": "text"}


def check_job(job):
    problems = []
    if not job.get("accountId"):
        problems.append("Pick an account.")
    if job.get("kind") not in KINDS:
        problems.append("Kind must be prompt or pack.")
    if not (job.get("brief") or "").strip() and not (job.get("clipUrl") or "").strip():
        problems.append("Add a brief or a clip link.")
    return problems


def pack_plan(job, accounts):
    if job.get("kind") != "pack":
        return []
    return [{"accountId": a["id"], "platform": a["platform"], "format": PACK_FORMAT[a["platform"]]}
            for a in accounts if a.get("status") == "active" and a.get("platform") in PACK_FORMAT]
