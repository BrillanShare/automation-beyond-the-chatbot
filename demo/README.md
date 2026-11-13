# demo/

Sample files for the two live demos described in `../demo.md`. All the data is made up.

| File | Demo | What it is |
|---|---|---|
| `bank.csv`, `ledger.csv` | Example 1: all AI → all script | 30 bank lines and 29 ledger entries to match |
| `match.py` | Example 1 | Backup script: matches by reference, amount and dates within 3 days |
| `transactions.csv` | Example 2: all AI → hybrid | 40 credit card lines to categorize |
| `vendor_rules.csv` | Example 2 | "If the memo contains X, the category is Y": 21 rules |
| `categorize.py` | Example 2 | Backup script: applies the rules and lists the leftovers |

**What to do with them:** upload them to Claude during the demo, following the steps in `../demo.md`. The scripts are backups in case the live version goes sideways. To run one yourself: `python match.py` or `python categorize.py` in this folder.

The scripts write their results (`matched.csv`, `leftovers.csv` and so on) into this folder. They never change the input files.
