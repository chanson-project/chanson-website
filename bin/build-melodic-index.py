#!/usr/bin/env python3
"""
Build a melodic pitch index from chanson **kern encoding files.

Downloads the encoding repository as a single zip (one network request),
extracts the primary melodic line from each **kern file, and writes
assets/melodic-index.json as space-separated pitch-class names.

Usage (run from project root):
    python3 bin/build-melodic-index.py

Requires _includes/metadata/works.json to exist (run 'make download' first).
"""

import io
import json
import re
import sys
import urllib.request
import zipfile
from pathlib import Path

REPO_ZIP   = "https://github.com/chanson-project/chanson-encoding/archive/refs/heads/main.zip"
WORKS_JSON = Path("_includes/metadata/works.json")
OUTPUT     = Path("assets/melodic-index.json")

# 2-char work-ID prefix → subdirectory in the encoding repo
DIR_MAP = {"BC": "bc100", "EG": "eg104"}


def extract_pitches(kern_text):
    """Return list of pitch-class strings from the first **kern spine.

    Kern pitch letters: a-g (upper octaves) / A-G (lower octaves).
    Accidentals: # = sharp, - = flat (kern uses minus, not 'b').
    Rests contain 'r' but no pitch letter; null tokens are '.'.
    Tied continuations begin with '_' and are skipped (same pitch sustained).
    """
    in_kern = False
    pitches = []

    for line in kern_text.split('\n'):
        line = line.rstrip('\r')
        if not line:
            continue

        # Exclusive interpretation — detect spine type
        if line.startswith('**'):
            in_kern = line.split('\t')[0] == '**kern'
            continue

        # End of spine
        if line.startswith('*-'):
            break

        # Skip comments, interpretations, barlines
        if line[0] in ('!', '*', '='):
            continue

        if not in_kern:
            continue

        # Take only the first spine (first tab field)
        token = line.split('\t')[0].strip()
        if not token or token == '.':
            continue

        # Skip tied-note continuations (sustained pitch, no new onset)
        if '_' in token and not re.search(r'[A-Ga-g]', token.replace('_', '')):
            continue

        # Find pitch letter(s) and accidental(s) in the token
        m = re.search(r'([A-Ga-g]+)([#\-]*)', token)
        if not m:
            continue  # rest or unrecognized

        letter      = m.group(1)[0].upper()  # pitch class, case-normalized
        accidentals = m.group(2)

        if '#' in accidentals:
            pitches.append(letter + '#')
        elif '-' in accidentals:
            pitches.append(letter + 'b')
        else:
            pitches.append(letter)

    return pitches


def main():
    if not WORKS_JSON.exists():
        sys.exit(f"ERROR: {WORKS_JSON} not found — run 'make download' first.")

    works = json.loads(WORKS_JSON.read_text(encoding='utf-8'))

    # Build map: zip-internal path → work ID
    path_to_id = {}
    for work in works:
        work_id  = (work.get("!!!id") or "").strip()
        filename = (work.get("!!!file-name") or "").strip()
        prefix   = work_id[:2]
        directory = DIR_MAP.get(prefix)
        if work_id and filename and directory:
            path_to_id[f"{directory}/kern/{filename}"] = work_id

    print(f"Fetching encoding repository ({REPO_ZIP}) …")
    with urllib.request.urlopen(REPO_ZIP) as resp:
        raw = resp.read()
    print(f"Downloaded {len(raw) / 1024:.0f} KB.")

    zf         = zipfile.ZipFile(io.BytesIO(raw))
    zip_root   = "chanson-encoding-main/"   # GitHub zip prefix
    index      = {}
    missing    = []

    for rel_path, work_id in sorted(path_to_id.items()):
        zip_path = zip_root + rel_path
        try:
            kern_bytes = zf.read(zip_path)
        except KeyError:
            missing.append(zip_path)
            continue

        pitches = extract_pitches(kern_bytes.decode('utf-8'))
        if pitches:
            index[work_id] = " ".join(pitches)
            print(f"  {work_id}: {len(pitches)} notes")
        else:
            print(f"  {work_id}: WARNING — no pitches extracted", file=sys.stderr)

    if missing:
        print(f"\nWARNING: {len(missing)} file(s) not found in zip:", file=sys.stderr)
        for p in missing:
            print(f"  {p}", file=sys.stderr)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(index, ensure_ascii=False), encoding='utf-8')
    print(f"\nIndexed {len(index)} works → {OUTPUT}")


if __name__ == "__main__":
    main()
