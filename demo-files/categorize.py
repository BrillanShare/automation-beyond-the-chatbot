"""Categorize credit card lines with vendor rules (no AI at run time).

Reads transactions.csv and vendor_rules.csv from this folder.
Writes:
  categorized.csv  every line that matched a rule
  leftovers.csv    lines no rule matched: only these need AI or a person

Run:  python categorize.py
"""
import csv
from pathlib import Path

HERE = Path(__file__).parent


def main():
    with open(HERE / "vendor_rules.csv", newline="") as f:
        rules = list(csv.DictReader(f))
    with open(HERE / "transactions.csv", newline="") as f:
        lines = list(csv.DictReader(f))

    matched, leftovers = [], []
    for line in lines:
        memo = line["memo"].upper()
        # First matching rule wins, so more specific rules go first in the file.
        category = next((r["category"] for r in rules if r["memo_contains"].upper() in memo), None)
        if category:
            matched.append({**line, "category": category})
        else:
            leftovers.append(line)

    with open(HERE / "categorized.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "memo", "amount", "category"])
        w.writeheader()
        w.writerows(matched)
    with open(HERE / "leftovers.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "memo", "amount"])
        w.writeheader()
        w.writerows(leftovers)

    print(f"{len(lines)} lines: {len(matched)} matched a rule, {len(leftovers)} left over")
    print("Only leftovers.csv needs AI or a person.")


if __name__ == "__main__":
    main()
