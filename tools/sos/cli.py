"""Command line for skills: `due` and `check` on a JSON list of posts (each with an "id")."""
import argparse
import json
import sys
from datetime import datetime, timezone

from tools.sos import preflight, queue


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m tools.sos.cli")
    ap.add_argument("command", choices=["due", "check"])
    ap.add_argument("file")
    ap.add_argument("--now", help="ISO time with offset; default = now")
    args = ap.parse_args(argv)

    with open(args.file, encoding="utf-8") as f:
        posts = json.load(f)

    if args.command == "due":
        now = queue.parse_time(args.now) if args.now else datetime.now(timezone.utc)
        result = queue.due_posts(posts, now)
    else:
        result = {p["id"]: preflight.check(p) for p in posts}

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
