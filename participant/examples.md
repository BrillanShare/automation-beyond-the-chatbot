# Examples

## Clear-cut: scripting

| Task | Why it's scripting |
|---|---|
| Match bank transactions to the ledger by amount, date and reference | Fixed rules; same data in, same matches out |
| Roll forward a depreciation schedule | Pure calculation; Excel already does this |
| Rename and file 200 PDFs by client ID from a system export | The ID is in a fixed place in each file name |
| Combine monthly CSV exports from the same system into one workbook | Same columns every month |
| Check an invoice-number sequence for gaps | Pure rule |
| Fill the same Excel template from a structured export | Field-to-cell mapping never changes |
| Convert balances at today's published exchange rate | Depends on the internet, so not deterministic, but no judgment |
| Pick a random audit sample | Random on purpose; record the seed so the sample can be reproduced |

## Clear-cut: AI in the loop

| Task | Why it needs an LLM every run |
|---|---|
| Draft a client email explaining a variance | Writing new language for each client |
| Summarize the key terms of a 40-page lease | Every lease is worded differently |
| Answer a client's free-form question | The question is different every time |
| Turn meeting notes into action items | Open-ended language in, judgment about what counts as an action |

## Hard inputs that change the call

| Task that looks like scripting | Hard input that's easy to overlook | What it does to the design |
|---|---|---|
| Pull totals from bank statement PDFs | Some statements are scans or phone photos | Text extraction fails on those; add a local OCR model or AI in the loop for them only |
| Categorize credit card transactions by vendor | "Amazon", "AMZN Mktp US", "Amazon.com*2X4" | Rules need a lookup table that grows; unmatched ones need a review path |
| Read invoice dates | 03/04/2026: March or April? | Need a rule per vendor, or a check that flags ambiguous dates |
| Import a client's Excel export | Merged cells, two header rows, a totals row in the middle | Script needs cleanup steps, tested on real exports |
| Fill a form from vendor invoices | Vendor changed its invoice layout | Fixed-position rules break silently; add a check that catches missing fields |
| Process a folder of client documents | Duplicates, password-protected PDFs | Script needs to detect and list them, not skip them silently |

## Hybrid patterns

Agree on the split for each one before building.

| Pattern | Scripting part | AI-in-the-loop part | The seam |
|---|---|---|---|
| **AI extracts → script processes** | Validate, total, fill the Excel form | Pull fields from messy PDFs into a CSV | Fixed CSV columns; the script rejects rows that fail checks |
| **Script filters → AI judges** | Run the reconciliation, find the exceptions | Draft the explanation for only the exceptions | The script sends only the exception rows, not the whole file |
| **Rules first, AI for leftovers** | Categorize by vendor rules (most transactions) | Categorize only the unmatched ones | Unmatched list → AI → review list; good answers become new rules |
| **AI first, then promote to script** | Later: the script that replaced the AI step | Early: do the task with AI a few times | Once the pattern is stable, ask Claude to turn it into a script |

- **Not hybrid:** AI writing a script's tests or sample data. That's part of building, so it's scripting.

## Zero-token helpers: local machine learning models a script can call

| Need | Local model (examples) | Notes |
|---|---|---|
| Text from scanned documents | Tesseract | Struggles with poor scans and handwriting |
| Speech to text | whisper.cpp, Vosk | Runs offline; larger models need a stronger computer |
| Categorize transactions from the firm's own past entries | scikit-learn | Needs enough past examples to learn from |
| Find names, dates and amounts in text | spaCy | Accuracy depends on the type of text |
| Remove an image background | rembg | Downloads a model file on first run |

- Not LLMs. They run on your computer. Zero tokens.
- Narrow: each one does one job.
- Setting them up takes real technical knowledge. Claude can carry most of it, but expect some back-and-forth.
