"""
stats.py — generates a progress summary from your reading entries.
Run with: python stats.py
"""

import os
import re
from datetime import datetime
from pathlib import Path

def count_entries(folder):
    return len(list(Path(folder).glob("*.md")))

def count_vocab(vocab_file):
    count = 0
    if not os.path.exists(vocab_file):
        return 0
    with open(vocab_file, encoding="utf-8") as f:
        for line in f:
            # Count table rows that are not headers or empty placeholders
            if line.startswith("|") and "---" not in line and "Expression" not in line and "— |" not in line:
                count += 1
    return count

def list_recent(folder, n=5):
    files = sorted(Path(folder).glob("*.md"), reverse=True)[:n]
    entries = []
    for f in files:
        with open(f, encoding="utf-8") as fp:
            first_line = fp.readline().strip()
            title = re.sub(r"##\s*\[?([^\]]+)\]?.*", r"\1", first_line)
            entries.append((f.stem, title))
    return entries

def main():
    base = Path(__file__).parent
    fr_count = count_entries(base / "fr")
    en_count = count_entries(base / "en")
    total = fr_count + en_count
    vocab_count = count_vocab(base / "vocabulary.md")

    print("\n" + "="*50)
    print("  LANGUAGE LEARNING — PROGRESS SUMMARY")
    print("="*50)
    print(f"  Total articles read : {total}")
    print(f"  French articles     : {fr_count}")
    print(f"  English articles    : {en_count}")
    print(f"  Expressions saved   : {vocab_count}")
    print(f"  Generated on        : {datetime.now().strftime('%Y-%m-%d')}")
    print("="*50)

    if fr_count > 0:
        print("\n  Recent FR entries:")
        for date, title in list_recent(base / "fr"):
            print(f"    {date} — {title[:55]}")

    if en_count > 0:
        print("\n  Recent EN entries:")
        for date, title in list_recent(base / "en"):
            print(f"    {date} — {title[:55]}")

    print()

if __name__ == "__main__":
    main()
