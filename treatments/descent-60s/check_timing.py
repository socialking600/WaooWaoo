#!/usr/bin/env python3
"""
Beat-sheet validator for treatments/descent-60s/directors-treatment.md

Parses the shot lines out of the two prompt code blocks and checks:
  1. shots are contiguous (no gaps, no overlaps) and cover the video exactly
  2. the shot count matches the number declared in the prompt header
  3. no *continuous* shot exceeds the stated maximum (internal cuts split a
     compound shot into sub-shots, and each sub-shot is checked too)
  4. every peak in the beat-map table falls inside a shot or on a cut
  5. the declared clip split is contiguous, covers the video, and every clip is
     within the per-generation duration ceiling

Run:  python3 treatments/descent-60s/check_timing.py
"""

import re
import sys
from pathlib import Path

DOC = Path(__file__).with_name("directors-treatment.md")

CEILING = 10.0  # seconds, per-generation clip ceiling we design against

# (label, shots, max continuous shot, start, end, clip boundaries)
VIDEOS = [
    ("VIDEO 1", 10, 3.5, 0.0, 25.0, [0.0, 9.0, 18.5, 25.0]),
    ("VIDEO 2", 10, 3.5, 25.0, 60.0, [25.0, 33.0, 40.0, 46.0, 49.0, 55.5, 60.0]),
]

PEAKS = [9.0, 25.0, 43.0, 56.0]

SHOT_RE = re.compile(r"^\s*(\d+)\s+\((\d+(?:\.\d+)?)-(\d+(?:\.\d+)?)s\)", re.M)
COUNT_RE = re.compile(r"(\d+)\s+shots with hard cuts")
MAXLEN_RE = re.compile(r"longest continuous shot\s+(\d+(?:\.\d+)?)\s+seconds")
INTERNAL_RE = re.compile(
    r"internal cuts? at\s+"
    r"(\d+(?:\.\d+)?s?(?:\s*,?\s*(?:and\s+)?\d+(?:\.\d+)?s?)*)"
)
PEAK_ROW_RE = re.compile(r"\*\*PEAK \d\*\*")
BEAT_RE = re.compile(r"^\|\s*\**\s*(\d+(?:\.\d+)?)[–-](\d+(?:\.\d+)?)\s*\**\s*\|", re.M)

failures: list[str] = []
notes: list[str] = []


def check(cond: bool, ok_msg: str, fail_msg: str) -> bool:
    if cond:
        notes.append(f"  PASS  {ok_msg}")
    else:
        failures.append(f"  FAIL  {fail_msg}")
    return cond


def parse_internal_cuts(block: str, shot_num: int) -> list[float]:
    """Cut times declared inside a compound shot, e.g. 'internal cuts at
    52.5s, 55.5s and 58.5s'. The text wraps across lines, so the whole shot
    block is searched, not just its first line. Returns ascending order."""
    lines = block.splitlines()
    start = None
    for i, raw in enumerate(lines):
        if re.match(rf"^\s*{shot_num}\s+\(\d", raw):
            start = i
            break
    if start is None:
        return []
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if re.match(r"^\s*\d+\s+\(\d", lines[j]):
            end = j
            break
    m = INTERNAL_RE.search(" ".join(lines[start:end]))
    if not m:
        return []
    nums = re.findall(r"\d+(?:\.\d+)?", m.group(1))
    return sorted(float(n) for n in nums)


def main() -> int:
    text = DOC.read_text(encoding="utf-8")

    # --- beat-map table ---
    beats = [(float(a), float(b)) for a, b in BEAT_RE.findall(text)]
    print(f"beat-map rows parsed: {len(beats)}")
    peak_rows = len(PEAK_ROW_RE.findall(text))
    check(peak_rows == len(PEAKS), f"beat map marks {peak_rows} peaks",
          f"beat map marks {peak_rows} peaks, expected {len(PEAKS)}")
    for p in PEAKS:
        hit = any(a <= p <= b for a, b in beats)
        check(hit, f"peak {p}s is covered by a beat-map row",
              f"peak {p}s is NOT inside any beat-map row")
    check(abs(beats[0][0]) < 1e-9, f"beat map opens at {beats[0][0]}s",
          f"beat map opens at {beats[0][0]}s, expected 0.0s")
    check(abs(beats[-1][1] - 60.0) < 1e-9,
          f"beat map closes at {beats[-1][1]}s (loop lands on the cut to black)",
          f"beat map closes at {beats[-1][1]}s, expected 60.0s")
    beat_gaps = [(b0, a1) for (_, b0), (a1, _) in zip(beats, beats[1:])
                 if abs(a1 - b0) > 1e-9]
    check(not beat_gaps, "beat map rows are contiguous",
          f"beat map has gaps/overlaps: {beat_gaps}")

    # --- prompt blocks (fenced blocks that open with the prompt header) ---
    blocks = [b for b in re.findall(r"```\n(.*?)```", text, re.S)
              if b.lstrip().startswith("Photorealistic")]
    print(f"prompt blocks found: {len(blocks)}")
    check(len(blocks) == len(VIDEOS), f"{len(blocks)} prompt blocks found",
          f"expected {len(VIDEOS)} prompt blocks, found {len(blocks)}")

    for (label, want_n, want_max, start, end, clips), block in zip(VIDEOS, blocks):
        print(f"\n{label}  ({start}-{end}s)")

        declared_n = int(COUNT_RE.search(block).group(1))
        check(declared_n == want_n, f"header declares {declared_n} shots",
              f"header declares {declared_n} shots, expected {want_n}")

        declared_max = float(MAXLEN_RE.search(block).group(1))
        check(declared_max == want_max,
              f"header caps continuous shots at {declared_max}s",
              f"header caps continuous shots at {declared_max}s, expected {want_max}s")

        shots = [(int(n), float(a), float(b)) for n, a, b in SHOT_RE.findall(block)]
        nums = [n for n, _, _ in shots]
        check(nums == list(range(1, len(shots) + 1)),
              f"shot numbers are 1..{len(shots)}, no gaps",
              f"shot numbering broken: {nums}")
        check(len(shots) == want_n, f"{len(shots)} shot lines match the header",
              f"{len(shots)} shot lines, header says {want_n}")
        check(abs(shots[0][1] - start) < 1e-9, f"first shot starts at {shots[0][1]}s",
              f"first shot starts at {shots[0][1]}s, expected {start}s")
        check(abs(shots[-1][2] - end) < 1e-9, f"last shot ends at {shots[-1][2]}s",
              f"last shot ends at {shots[-1][2]}s, expected {end}s")

        gaps = [(b0, a1) for (_, _, b0), (_, a1, _) in zip(shots, shots[1:])
                if a1 > b0 + 1e-9]
        overlaps = [(b0, a1) for (_, _, b0), (_, a1, _) in zip(shots, shots[1:])
                    if a1 < b0 - 1e-9]
        check(not gaps, "no gaps between shots", f"gaps: {gaps}")
        check(not overlaps, "no overlaps between shots", f"overlaps: {overlaps}")

        # continuous shots and, inside compound shots, sub-shots
        worst_shot, worst_sub = 0.0, 0.0
        for n, a, b in shots:
            worst_shot = max(worst_shot, b - a)
            cuts = parse_internal_cuts(block, n)
            edges = [a] + [c for c in cuts if a < c < b] + [b]
            for e0, e1 in zip(edges, edges[1:]):
                worst_sub = max(worst_sub, e1 - e0)
            bad = [c for c in cuts if not (a < c < b)]
            check(not bad,
                  f"shot {n} internal cuts {cuts or '—'} all sit inside {a}-{b}s",
                  f"shot {n} declares internal cuts outside its range: {bad}")
        check(worst_shot <= want_max + 1e-9 or worst_sub <= want_max + 1e-9,
              f"longest continuous shot {worst_shot}s; longest after internal "
              f"cuts {worst_sub}s (cap {want_max}s)",
              f"longest shot {worst_shot}s / sub-shot {worst_sub}s exceeds cap {want_max}s")

        for p in PEAKS:
            if start < p <= end:
                inside = [n for n, a, b in shots if a <= p < b]
                on_cut = [n for n, a, b in shots if abs(b - p) < 1e-9]
                if inside:
                    check(True, f"peak {p}s lands inside shot {inside[0]}", "")
                elif on_cut:
                    check(True, f"peak {p}s lands on the cut ending shot {on_cut[-1]}", "")
                else:
                    check(False, "", f"peak {p}s falls on no shot in {label}")

        # clip split
        check(abs(clips[0] - start) < 1e-9 and abs(clips[-1] - end) < 1e-9,
              f"clip split spans {clips[0]}-{clips[-1]}s",
              f"clip split {clips[0]}-{clips[-1]}s does not span {start}-{end}s")
        lens = [round(b - a, 3) for a, b in zip(clips, clips[1:])]
        check(all(a <= b for a, b in zip(clips, clips[1:])),
              "clip boundaries ascend", f"clip boundaries out of order: {clips}")
        over = [x for x in lens if x > CEILING]
        check(not over,
              f"{len(lens)} clips, lengths {lens}, all <= {CEILING}s ceiling",
              f"{len(lens)} clips, lengths {lens}, {len(over)} exceed {CEILING}s")
        for cut in clips[1:-1]:
            on_shot = [n for n, a, b in shots if abs(b - cut) < 1e-9]
            # a join may also land on a declared internal cut inside a compound
            # shot, which is a real edit point even though it is not a shot end
            internal_hit = [
                n for n, a, b in shots
                if a < cut < b and any(abs(c - cut) < 1e-9
                                       for c in parse_internal_cuts(block, n))
            ]
            if on_shot:
                check(True, f"clip join at {cut}s falls on a shot boundary "
                            f"(end of shot {on_shot[-1]})", "")
            elif internal_hit:
                check(True, f"clip join at {cut}s falls on a declared internal cut "
                            f"inside shot {internal_hit[0]}", "")
            else:
                check(False, "",
                      f"clip join at {cut}s cuts through the middle of a shot "
                      f"with no declared edit point")

        dur = end - start
        print(f"  {len(shots)} shots over {dur}s -> average {dur/len(shots):.2f}s/shot, "
              f"{len(clips)-1} clips: {lens}")

    print("\n" + "\n".join(notes))
    if failures:
        print("\n".join(failures))
        print(f"\n{len(failures)} check(s) FAILED")
        return 1
    print(f"\nAll {len(notes)} checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
