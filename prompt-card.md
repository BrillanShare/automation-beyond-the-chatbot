# Prompt card

Copy and adapt. The starter [CLAUDE.md](https://code.claude.com/docs/en/memory) already includes the first one.

## 1. Agree on the design first

> Before building anything: restate this task as inputs → outputs. List the hard inputs, not only the typical ones. Propose the design with the least AI in the loop. Label each step Scripting, Local model or AI in the loop, and say why. Rate each step's tokens per run: none, small or large. Wait for my OK.

## 2. Find another way

> How would I do this without AI in the loop? What would I lose?

## 3. Find the hard inputs

> What could arrive for this task that would break the obvious rules? Think about scans, photos, layout changes, spelling variations, date formats, duplicates and missing files.

## 4. Compare designs

> Give me two or three designs for this. Rank them by tokens per run (none, small, large), reliability on the hard inputs, and how hard they are to maintain.

## 5. Define "done" before building

> Before writing the script, write sample inputs, including hard ones, and the output you expect for each. We'll use them to check the script.

## 6. Understand the script

> Explain this script for someone with no computer science background: what it reads, what it does, what it writes, and what could go wrong.

## 7. Turn a chat habit into a script

> I keep asking you to do this in chat. Turn it into a script I can run on my own computer, so it costs no tokens per run.

## 8. Large files

> This file is large. Don't read all of it. Write a script that pulls out only the part you need to see.

## 9. Review a script like an auditor

> Before I rely on this script, review it as an auditor would. Tell me in plain language: what it does with rows it can't process; whether rows and totals in equal rows and totals out; how money is stored and rounded, and whether that matches Excel; what happens if I run it twice; whether it changes any input file; which values are fixed in the code; what it installs and whether it sends data anywhere; whether its rules are reviewed and dated; whether tests are saved next to it; and whether any step still uses tokens on every run. Flag anything you'd fix.

## 10. Is it worth converting?

> I do this task with AI today: [describe it]. Each run handles about [how many] [lines / documents / clients], and I run it [how often]. Before proposing anything, tell me in plain words how the tokens grow as that count grows, and whether any step compares every item with every other item. Then tell me whether my volume is big enough for that to matter, and at what volume it would start to. Then say whether a hybrid or script design would change the shape of that growth or only lower it a little. Use relative amounts, not exact token counts. If you need a number from me, ask. Don't guess my volume.

## 11. Plot it

> First, if I haven't told you, ask how many [lines / documents / clients] each run handles and how often I run it. If the designs would differ too little at my volume to matter, say so in one sentence and don't make a chart. Otherwise, make a chart for this task. Horizontal axis: how many [lines / documents / clients] I process in a year. Vertical axis: tokens, in relative units. Draw one line for how you do it today and one line for each design you'd propose (hybrid, script). Include the one-time tokens to build each design. Mark my volume with a "you are here" line, and mark any break-even point. Plot only steps that use tokens. For a step that compares every item with every other, use the count in one run, not the yearly total. Then explain the chart in plain language: what I'd save in a year at my volume, and what would have to change for the answer to flip. List your assumptions.

## 12. Which one first?

> Here are the tasks I do with AI today, with how many each run handles and how often I run it: [list them]. For each one, say how its tokens grow with volume, whether my volume is big enough for that to matter, and whether converting to hybrid or script would change the shape of the growth. Then rank them by return on my effort: tokens saved in a year against the work to convert. Show one table and one chart, with my volume marked on each line.

# Controls

The starter CLAUDE.md already asks Claude for all of these. Use these prompts to check or fix a script you already have.

## 13. Fail loudly

> Make this script fail loudly: never skip a row silently. List every row it couldn't process, with the reason. Show failures in red capital letters and warnings in yellow, so both you and I see them.

## 14. Control totals

> After each run, report rows in, rows out and rows not processed, and check that they add up. Do the same for the dollar totals.

## 15. Money math

> How does this script store and round money? Use exact decimals, and round the way Excel's ROUND does. Show me an example where it matters.

## 16. Safe to run twice

> What happens if I run this twice on the same file? Make sure a second run can't post anything twice.

## 17. Never overwrite an input

> Does this script change or delete any file it reads? Make it write results to a new file, and ask me before it overwrites anything.

## 18. Text that looks like numbers

> Which columns does this script read as numbers, text and dates? Read account numbers, IDs and ZIP codes as text so leading zeros survive, and tell me how dates are read.

## 19. Rules you review, with a date

> Move the rates, rules and cutoff dates out of the script into a settings file I can review. Add a "review by" date, and show a yellow warning once it passes.

## 20. Run log

> Make each run record the date and time, who ran it, the input file, row counts and the script version.

## 21. What it installs and sends

> Before I run this: what does it install, and does it send any data anywhere? List each one and why.

## 22. Tests that last

> Save the sample inputs and expected outputs as tests next to the script. After any change, rerun all of them and tell me if anything that used to pass now fails.
