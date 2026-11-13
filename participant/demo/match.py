"""Match bank lines to ledger entries (no AI at run time).

A bank line and a ledger entry match when the reference and the amount are
the same and the dates are no more than 3 days apart.

Reads bank.csv and ledger.csv from this folder.
Writes:
  matched.csv              pairs that matched
  bank_not_in_ledger.csv   bank lines with no ledger entry
  ledger_not_in_bank.csv   ledger entries that haven't cleared the bank

Run:  python match.py
"""
import csv
from datetime import date
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).parent
MAX_DAYS_APART = 3


def read(name):
    with open(HERE / name, newline="") as f:
        return list(csv.DictReader(f))


def write(name, rows, fields):
    with open(HERE / name, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main():
    bank, ledger = read("bank.csv"), read("ledger.csv")
    unmatched_ledger = list(ledger)
    matched, bank_only = [], []
    for b in bank:
        hit = next((l for l in unmatched_ledger
                    if l["reference"] == b["reference"]
                    and Decimal(l["amount"]) == Decimal(b["amount"])
                    and abs((date.fromisoformat(l["date"]) - date.fromisoformat(b["date"])).days) <= MAX_DAYS_APART),
                   None)
        if hit:
            unmatched_ledger.remove(hit)
            matched.append({"reference": b["reference"], "payee": hit["payee"], "amount": b["amount"],
                            "bank_date": b["date"], "ledger_date": hit["date"]})
        else:
            bank_only.append(b)

    write("matched.csv", matched, ["reference", "payee", "amount", "bank_date", "ledger_date"])
    write("bank_not_in_ledger.csv", bank_only, ["date", "reference", "amount"])
    write("ledger_not_in_bank.csv", unmatched_ledger, ["date", "reference", "payee", "amount"])

    # Control totals: every line is accounted for.
    assert len(matched) + len(bank_only) == len(bank)
    assert len(matched) + len(unmatched_ledger) == len(ledger)
    print(f"Bank lines: {len(bank)}. Ledger entries: {len(ledger)}.")
    print(f"Matched: {len(matched)}. Bank lines not in ledger: {len(bank_only)}. "
          f"Ledger entries not yet in bank: {len(unmatched_ledger)}.")


if __name__ == "__main__":
    main()
