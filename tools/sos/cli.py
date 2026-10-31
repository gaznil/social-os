"""Command line for skills: `due` and `check` on a JSON list of posts (each with an "id");
`studio-check <job.json>` and `pack-plan <job.json> <accounts.json>` for video studio jobs."""
import argparse
import json
import sys
from datetime import datetime, timezone

from tools.sos import preflight, queue, studio


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m tools.sos.cli")
    ap.add_argument("command", choices=["due", "check", "studio-check", "pack-plan"])
    ap.add_argument("file")
    ap.add_argument("accounts", nargs="?", help="pack-plan only: JSON list of accounts")
    ap.add_argument("--now", help="ISO time with offset; default = now")
    args = ap.parse_args(argv)

    posts = load(args.file)

    if args.command == "studio-check":
        result = studio.check_job(posts)
    elif args.command == "pack-plan":
        if not args.accounts:
            ap.error("pack-plan needs <job.json> <accounts.json>")
        result = studio.pack_plan(posts, load(args.accounts))
    elif args.command == "due":
        now = queue.parse_time(args.now) if args.now else datetime.now(timezone.utc)
        result = queue.due_posts(posts, now)
    else:
        result = {p["id"]: preflight.check(p) for p in posts}

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
