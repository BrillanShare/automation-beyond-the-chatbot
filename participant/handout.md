# Script or AI? Concepts and examples

## Three buckets

![Three buckets: what happens at build time and at run time](buckets.svg)

| Bucket | What happens at run time | Tokens per run |
|---|---|---|
| 📜 Scripting | Code runs on your computer. AI may have written the code, its tests and its sample data, but no LLM runs now. | None |
| 🤖 AI in the loop | An [LLM](https://en.wikipedia.org/wiki/Large_language_model) is called every time the task runs. | Small to large, every run |
| 🔀 Hybrid | Some steps are scripting, some are AI in the loop. | Only for the AI steps |

- AI helping you **build** a script doesn't make it AI in the loop.
- Writing tests and sample data with AI is part of building, so it's scripting too.

## What "deterministic" means

**Strict definition: [deterministic](https://en.wikipedia.org/wiki/Deterministic_algorithm) means the same inputs always give the same output.**

![Venn diagram: where procedures fall](venn.svg)

| Region | Examples |
|---|---|
| 🟢 Same inputs → same output | [`=SUM()`](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89), a tax-bracket lookup, matching invoice numbers |
| 🟠 Also depends on the clock, the internet or a file | [`=NOW()`](https://support.microsoft.com/en-us/office/now-function-3337fd29-145a-4347-b2e6-20c904739c46), today's stock price, today's exchange rate |
| 🎲 Random on purpose (pseudo-random\*) | [`=RAND()`](https://support.microsoft.com/en-us/office/rand-function-4cbfa695-8869-4788-8d90-021ea9f5be73), random IDs, an audit sample |
| 🔴 AI in the loop | Every LLM call: never deterministic |

\* Random in a computer isn't truly random: the picks come from a fixed recipe and a starting number. Same starting number → same picks.

### Randomness in LLMs

- Built into how an LLM picks each word
- Can't be turned off by a Claude user
- Hard to remove completely, even for developers who control every setting
- A tiny change in the input → possibly a different whole answer
- What you type isn't the whole input: the app adds its own instructions, the date, memory, earlier messages

## What a script can't do

A script needs you to say **in advance** where to look and what to do with what it finds.

![Monthly Excel exports with the same shape next to two leases with the rent in different places](script-cant.svg)

| | Changes from run to run | Script still works? |
|---|---|---|
| 📊 Monthly Excel export | The **values**. Column C is always the amount; the steps are always the same. | ✅ Yes |
| 📄 A client's lease | The **shape and wording**. The rent clause can be anywhere, phrased any way, with an exception in a footnote. | ❌ No: finding it means understanding what the words mean |

- **Different values, same shape** → scripting
- **Different shape or wording, same meaning to find** → AI in the loop

## Data type doesn't decide the bucket

![Numbers, language, images and audio: one example each that scripting can handle and one that needs AI in the loop](data-types.svg)

| Data type | 📜 Scripting example | 🤖 AI-in-the-loop example |
|---|---|---|
| 🔢 Numbers | Totals, reconciliations, depreciation schedules | Reviewing a trial balance for balances that look misclassified for this kind of business (a large "office supplies" balance at a consulting firm) |
| 💬 Language | Find-and-replace, templated engagement letters, a date in a fixed-format file name | Drafting a client explanation of a variance |
| 🖼️ Images | Removing a plain background by color | Reading a crumpled receipt photo |
| 🎙️ Audio | Detecting a sound (a clap, a beep) | A punctuated transcript of a client call |

## The input/output lens defines the task, but doesn't decide the bucket

- **Use it to describe the task:** what goes in, what has to come out, in what format.
- **Don't use it to pick the bucket:** the same input and output can land in different buckets.

![Bank statements in, Excel form out: text PDFs from one bank are scripting; scans and photos from many banks are hybrid](io-lens.svg)

## Clear-cut examples

| Task | Bucket | Why |
|---|---|---|
| Match bank transactions to the ledger by amount, date and reference | 📜 Scripting | Fixed rules; same data in, same matches out |
| Roll forward a depreciation schedule | 📜 Scripting | Pure calculation; Excel already does this |
| Rename and file 200 PDFs by client ID from a system export | 📜 Scripting | The ID is in a fixed place in each file name |
| Combine monthly CSV exports from the same system into one workbook | 📜 Scripting | Same columns every month |
| Convert balances at today's published exchange rate | 📜 Scripting | Depends on the internet, but needs no judgment |
| Pick a random audit sample | 📜 Scripting | Random on purpose; the script saves the starting number for its (pseudo) random picks, so anyone can draw the exact same sample again |
| Draft a client email explaining a variance | 🤖 AI in the loop | New wording for each client and situation |
| Summarize the key terms of a 40-page lease | 🤖 AI in the loop | The terms can be anywhere, worded any way |
| Answer a client's free-form question | 🤖 AI in the loop | No way to list the questions in advance |
| Turn meeting notes into action items | 🤖 AI in the loop | Deciding what counts as an action means understanding the conversation |

## Rules for deciding, and their limits

**Rules of thumb:**

- Same shape every time, known cases → 📜 Scripting
- Open-ended wording, varied documents, judgment calls → 🤖 AI in the loop
- Mostly the same shape, with some messy cases → 🔀 Hybrid

**Why they're hard to apply:** we picture the typical input, not the hard ones.

![Six hard inputs: a tilted scan, one vendor under many names, a rules list that keeps growing, a messy Excel export, a changed invoice layout, duplicate and locked files](hard-inputs.svg)

| Task that looks like scripting | ⚠️ Hard input that's easy to overlook | What it does to the design |
|---|---|---|
| Pull totals from bank statement PDFs | 📷 Some statements are scans or phone photos | Text extraction fails on those; add a local model or AI in the loop for those files only |
| Categorize credit card transactions by vendor | 🔤 "Amazon", "AMZN Mktp US", "Amazon.com*2X4" | Rules need a **lookup table that grows**; unmatched lines need a review path |
| Categorize transactions from free-text memo lines | 🌀 Hundreds of wordings, abbreviations and typos | The script **grows to an enormous size and still misses cases**; that's the signal to move to hybrid |
| Import a client's Excel export | 🧩 Merged cells, two header rows, a totals row in the middle | The script needs cleanup steps, tested on real exports |
| Fill a form from vendor invoices | 🔁 A vendor changed its invoice layout | Fixed-position rules break silently; add a check that catches missing fields |
| Process a folder of client documents | 🔒 Duplicates, password-protected PDFs | The script needs to detect and list them, not skip them silently |

**So:** agree on the design with Claude **before** building anything.

- Ask for the hard inputs, not only the typical ones.
- Ask for the design with the least AI in the loop.
- Ask Claude to compare designs by tokens per run: none / small / large.
- See the prompt card and the starter [CLAUDE.md](https://code.claude.com/docs/en/memory).

## Tokens

| | 📜 Scripting | 🔀 Hybrid | 🤖 AI in the loop |
|---|---|---|---|
| Tokens to build | Once | Once | A prompt |
| Tokens per run | None | Small: only the slice that needs judgment | Large: every run |
| 500 invoices | Build once, then free | 500 small calls | 500 full calls |
| A large spreadsheet | The script reads it on your computer for free | The script sends only the rows that need judgment | Pasting it into chat burns tokens just to read it |

- **Big files make it worse.** Pasting a large spreadsheet into chat burns tokens just to read it.
- **Hybrid:** send only the slice that needs judgment to the LLM; let the script do the rest.

## Hybrid patterns

Agree on the split for each one before building.

| Pattern | 📜 Scripting part | 🤖 AI-in-the-loop part | The seam |
|---|---|---|---|
| **AI extracts → script processes** | Validate, total, fill the Excel form | Pull fields from messy PDFs into a [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) | Fixed CSV columns; the script rejects rows that fail checks |
| **Script filters → AI judges** | Run the reconciliation, find the exceptions | Draft the explanation for only the exceptions | The script sends only the exception rows, not the whole file |
| **Rules first, AI for leftovers** | Categorize by vendor rules (most transactions) | Categorize only the unmatched ones | Unmatched list → AI → review list; good answers become new rules |
| **AI first, then promote to script** | Later: the script that replaced the AI step | Early: do the task with AI a few times | Once the pattern is stable, ask Claude to turn it into a script |

- **Not hybrid:** AI writing a script's tests or sample data. That's part of building, so it's scripting.

## Zero-token helpers: local machine learning models a script can call

| Need | 💻 Local model | Notes |
|---|---|---|
| Text from scanned documents (optical character recognition) | [Tesseract](https://github.com/tesseract-ocr/tesseract) | Struggles with poor scans and handwriting |
| Speech to text | [whisper.cpp](https://github.com/ggml-org/whisper.cpp), [Vosk](https://alphacephei.com/vosk/) | Runs offline; larger models need a stronger computer |
| Categorize transactions from the firm's own past entries | [scikit-learn](https://scikit-learn.org/stable/) | Needs enough past examples to learn from |
| Find names, dates and amounts in text | [spaCy](https://spacy.io/) | Accuracy depends on the type of text |
| Remove an image background | [rembg](https://github.com/danielgatis/rembg) | Downloads a model file on first run |

- Not LLMs. They run on your computer. Zero tokens.
- Narrow: each one does one job.
- Setting them up takes real technical knowledge. Claude can carry most of it, but expect some back-and-forth.

## Sort these: discuss and vote

For each task, vote: 📜 Scripting, 🤖 AI in the loop or 🔀 Hybrid. Then ask: what hard inputs could change the answer? Reveal the hints one at a time, then the answer.

<div class="vote" markdown="1">

**1. Email every client a reminder 30 days before their filing deadline**

<details markdown="1">
<summary>Hints and answer</summary>

- Hint: Where does each deadline come from: a list, or someone's judgment?
- Hint: Is the email wording the same for every client?
- Answer: 📜 Scripting. Depends on the clock, but the rule is fixed: deadline minus 30 days, same template.

</details>
</div>

<div class="vote" markdown="1">

**2. Write a personal year-end note to each client about their year**

<details markdown="1">
<summary>Hints and answer</summary>

- Hint: Which part is pulling each client's figures, and which part is writing?
- Hint: Does each note need new wording?
- Answer: 🔀 Hybrid. The script pulls each client's figures; AI writes the note from only those figures.

</details>
</div>

<div class="vote" markdown="1">

**3. Flag possible duplicate vendor payments**

<details markdown="1">
<summary>Hints and answer</summary>

- Hint: What if the same invoice was entered twice with the same number and amount?
- Hint: What about "ACME Inc" vs. "Acme, Inc." with amounts a cent apart?
- Answer: 📜 Scripting, maybe 🔀 Hybrid. Exact matches are rules; near-matches may need AI for the leftovers.

</details>
</div>

<div class="vote" markdown="1">

**4. Turn client voicemails into tasks with the client's name and a due date**

<details markdown="1">
<summary>Hints and answer</summary>

- Hint: Turning speech into text: does that need an LLM, or can a local model do it?
- Hint: Picking a name and a due date out of a rambling message: rules, or understanding?
- Answer: 🔀 Hybrid. A local speech-to-text model (zero tokens), then AI picks out the name and due date from the transcript.

</details>
</div>

<div class="vote" markdown="1">

**5. Build a monthly KPI summary from the general ledger export**

<details markdown="1">
<summary>Hints and answer</summary>

- Hint: Does the export have the same columns every month?
- Hint: Are the KPI formulas the same every month?
- Answer: 📜 Scripting. Same export, same calculations every month.

</details>
</div>

<div class="vote" markdown="1">

**6. Pull box amounts from W-2s that clients upload**

<details markdown="1">
<summary>Hints and answer</summary>

- Hint: What if every W-2 is a text PDF from the same payroll provider?
- Hint: What if some are phone photos?
- Answer: 🔀 Hybrid. Text PDFs → script; scans and photos → local optical character recognition or AI; the script checks totals either way.

</details>
</div>

<div class="vote" markdown="1">

**7. Categorize 3,000 credit card lines from their memo text**

<details markdown="1">
<summary>Hints and answer</summary>

- Hint: How many lines could a vendor lookup table catch?
- Hint: What happens to the rules list as you chase the rest?
- Answer: 🔀 Hybrid. Rules first, AI for leftovers; the rules list grows from the AI's reviewed answers.

</details>
</div>

<div class="vote" markdown="1">

**8. Decide whether a receipt is a deductible business expense for this client**

<details markdown="1">
<summary>Hints and answer</summary>

- Hint: Can you list in advance every kind of receipt and every kind of business?
- Hint: Who is accountable for the decision?
- Answer: 🤖 AI in the loop, plus a person. Judgment about this client's business; a person signs off.

</details>
</div>

## Testing (if there's time)

- Testability comes from written-down code you can run on controlled inputs.
- **Random IDs:** test the properties: right length and format, no duplicates in 10,000 runs.
- **Today's stock price:** test the calculation with a fake price source that always returns $100.
- **Due-date reminders:** test with the clock frozen ("pretend today is April 10").
- **Audit sample:** the script saves the starting number for its (pseudo) random picks in the workpapers, so a reviewer can draw the exact same sample again and check it.
