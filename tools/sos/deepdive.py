"""Deep dive on one video: 6-frame contact sheet + timestamped transcript + a card for Claude to fill.
Transcript: ElevenLabs Scribe v2 (ELEVENLABS_API_KEY), local faster-whisper as the free fallback.

python -m tools.sos.deepdive <video file or direct http(s) link> --out <folder> [--model small] [--source <post link>]
Writes <folder>/frames.jpg, transcript.json, card.md. Prints a JSON summary.
"""
import argparse
import json
import os
import subprocess
import sys
import urllib.request
import uuid
from pathlib import Path


def fetch(src, out):
    """Return a local path for src, downloading direct http(s) links into out/video.mp4."""
    if not src.startswith(("http://", "https://")):
        return Path(src)
    dest = out / "video.mp4"
    req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
        f.write(r.read())
    return dest


def duration(video):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=nw=1:nk=1", str(video)],
                         capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def contact_sheet(video, dest, frames=6, width=360):
    """Evenly spaced frames tiled 3 across into one image."""
    rate = frames / duration(video)
    cols = 3
    rows = -(-frames // cols)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-vf",
                    f"fps={rate:.6f},scale={width}:-2,tile={cols}x{rows}",
                    "-frames:v", "1", str(dest)], check=True)
    return dest


def elevenlabs(video, key):
    """ElevenLabs Scribe v2 (free plan ~12 min/month). Word timestamps grouped into sentence lines."""
    boundary = uuid.uuid4().hex
    data = Path(video).read_bytes()
    body = b"".join([
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nscribe_v2\r\n".encode(),
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"tag_audio_events\"\r\n\r\nfalse\r\n".encode(),
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{Path(video).name}\"\r\n"
        f"Content-Type: application/octet-stream\r\n\r\n".encode(), data, f"\r\n--{boundary}--\r\n".encode()])
    req = urllib.request.Request("https://api.elevenlabs.io/v1/speech-to-text", data=body, method="POST",
                                 headers={"xi-api-key": key,
                                          "Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(req, timeout=300) as r:
        res = json.load(r)
    return {"language": res.get("language_code", "?"), "engine": "elevenlabs", "segments": lines(res.get("words", []))}


def lines(words):
    """Join ElevenLabs words into lines that end at . ! or ?"""
    out, cur = [], []
    for w in words:
        if w.get("type") != "word" and not cur:
            continue
        cur.append(w)
        if w.get("type") == "word" and w["text"].rstrip().endswith((".", "!", "?")):
            out.append(cur)
            cur = []
    if any(w.get("type") == "word" for w in cur):
        out.append(cur)
    real = [[w for w in ln if w.get("type") == "word"] for ln in out]
    return [{"start": round(ws[0]["start"], 1), "end": round(ws[-1]["end"], 1),
             "text": "".join(w["text"] for w in ln).strip()} for ln, ws in zip(out, real)]


def transcribe(video, model="small"):
    """ElevenLabs when ELEVENLABS_API_KEY is set; local faster-whisper if it is missing or fails (e.g. credits used up)."""
    key = os.environ.get("ELEVENLABS_API_KEY")
    if key:
        try:
            return elevenlabs(video, key)
        except Exception as e:  # out of credits, network down: fall back, never stop the run
            print(f"ElevenLabs failed ({e}); using local Whisper", file=sys.stderr)
    return whisper(video, model)


def whisper(video, model="small"):
    """Segments from the very start (no voice filter, so the hook at 0.0 s is kept)."""
    from faster_whisper import WhisperModel
    m = WhisperModel(model, device="cpu", compute_type="int8")
    segments, info = m.transcribe(str(video), vad_filter=False)
    return {"language": info.language, "engine": "whisper",
            "segments": [{"start": round(s.start, 1), "end": round(s.end, 1), "text": s.text.strip()}
                         for s in segments]}


def card(transcript, source=None):
    lines = [f"- [{s['start']:.1f}s] {s['text']}" for s in transcript["segments"]] or ["- (no speech)"]
    return "\n".join([
        "# Deep dive card",
        "",
        f"Source: {source or 'unknown'}",
        "",
        "![frames](frames.jpg)",
        "",
        f"## Transcript ({transcript['language']})",
        *lines,
        "",
        "## Hook (first 2 s)",
        "",
        "## Formula (with blanks)",
        "",
        "## Our version (account voice)",
        "",
    ])


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m tools.sos.deepdive")
    ap.add_argument("src")
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="small")
    ap.add_argument("--source", help="link to the original post, written on the card")
    args = ap.parse_args(argv)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    video = fetch(args.src, out)
    contact_sheet(video, out / "frames.jpg")
    t = transcribe(video, args.model)
    (out / "transcript.json").write_text(json.dumps(t, ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "card.md").write_text(card(t, args.source or args.src), encoding="utf-8")
    json.dump({"folder": str(out), "seconds": round(duration(video), 1),
               "segments": len(t["segments"]), "language": t["language"], "engine": t["engine"]},
              sys.stdout, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
