"""Apply placements exported from the site's edit mode to tools/curation.py.

Usage: python3 tools/apply_moves.py moves.json   (or pipe the JSON on stdin)
Input: {"mistville": {"map": "erukana", "at": [2290, 2395]}, ...}
Then run tools/build.py.
"""
import json
import os
import re
import sys

CURATION = os.path.join(os.path.dirname(os.path.abspath(__file__)), "curation.py")

moves = json.load(open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin)
src = open(CURATION, encoding="utf-8").read()

for pid, move in moves.items():
    if "@" in pid:
        # An extra pin, "<place>@<map>": its entry in the place's also=[(map, at, approx)].
        place, map_id = pid.split("@", 1)
        m = re.search(rf'^    "{re.escape(place)}": dict\((.*?)\),\n(?=    "|\n|}})', src, re.S | re.M)
        pat = rf'(\("{re.escape(map_id)}", )\[[^\]]*\]'
        if not m or not re.search(pat, m.group(1)):
            print(f"skipped {pid}: not found in curation.py")
            continue
        args = re.sub(pat, rf'\g<1>[{move["at"][0]}, {move["at"][1]}]', m.group(1), count=1)
        src = src[:m.start(1)] + args + src[m.end(1):]
        print(f"{pid}: {move['at']}")
        continue
    m = re.search(rf'^    "{re.escape(pid)}": dict\((.*?)\),\n(?=    "|\n|}})', src, re.S | re.M)
    if not m:
        if "note" not in move:
            print(f"skipped {pid}: not found in curation.py")
            continue
        # A location note placed for the first time: add it as a new approximate place.
        entry = (f'    "{pid}": dict(note={json.dumps(move["note"], ensure_ascii=False)}, map="{move["map"]}", '
                 f'at=[{move["at"][0]}, {move["at"][1]}], approx=True, kind="sted"),\n')
        end = src.index("\n}\n\nOFFMAP")
        src = src[:end + 1] + entry + src[end + 1:]
        print(f"{pid}: new place {move['map']} {move['at']}")
        continue
    args = m.group(1)
    at = f'at=[{move["at"][0]}, {move["at"][1]}]'
    new = re.sub(r'offmap="[^"]*",\s*', "", args)
    if re.search(r"\bat=\[[^\]]*\]", new):
        new = re.sub(r'\bmap="[^"]*"', f'map="{move["map"]}"', new)
        new = re.sub(r"\bat=\[[^\]]*\]", at, new)
    else:
        new = re.sub(r'^(note="[^"]*"),', rf'\1, map="{move["map"]}", {at},', new)
    src = src[:m.start(1)] + new + src[m.end(1):]
    print(f"{pid}: {move['map']} {move['at']}")

open(CURATION, "w", encoding="utf-8").write(src)
