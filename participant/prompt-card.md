# Prompt card

Copy and adapt. The starter [CLAUDE.md](https://code.claude.com/docs/en/memory) already includes the first one.

## Agree on the design first

> Before building anything: restate this task as inputs → outputs. List the hard inputs, not only the typical ones. Propose the design with the least AI in the loop. Label each step Scripting, Local model or AI in the loop, and say why. Rate each step's tokens per run: none, small or large. Wait for my OK.

## Find another way

> How would I do this without AI in the loop? What would I lose?

## Find the hard inputs

> What could arrive for this task that would break the obvious rules? Think about scans, photos, layout changes, spelling variations, date formats, duplicates and missing files.

## Compare designs

> Give me two or three designs for this. Rank them by tokens per run (none, small, large), reliability on the hard inputs, and how hard they are to maintain.

## Define "done" before building

> Before writing the script, write sample inputs, including hard ones, and the output you expect for each. We'll use them to check the script.

## Understand the script

> Explain this script for someone with no computer science background: what it reads, what it does, what it writes, and what could go wrong.

## Turn a chat habit into a script

> I keep asking you to do this in chat. Turn it into a script I can run on my own computer, so it costs no tokens per run.

## Large files

> This file is large. Don't read all of it. Write a script that pulls out only the part you need to see.

## Review a script like an auditor

> Before I rely on this script, review it as an auditor would. Tell me in plain language: what it does with rows it can't process; whether rows and totals in equal rows and totals out; how money is stored and rounded, and whether that matches Excel; what happens if I run it twice; whether it changes any input file; which values are fixed in the code; what it installs and whether it sends data anywhere; and whether any step still uses tokens on every run. Flag anything you'd fix.

## Is it worth converting?

> I do this task with AI today: [describe it]. I handle about [how many] [lines / documents / clients] each [week / month / year]. Before proposing anything, tell me in plain words how the tokens grow as that count grows, and whether any step compares every item with every other item. Then tell me whether my volume is big enough for that to matter, and at what volume it would start to. Then say whether a hybrid or script design would change the shape of that growth or only lower it a little. Use relative amounts, not exact token counts. If you need a number from me, ask. Don't guess my volume.

## Plot it

> Make a chart for this task. Horizontal axis: how many [lines / documents / clients] I process in a year. Vertical axis: tokens, in relative units. Draw one line for how you do it today and one line for each design you'd propose (hybrid, script). Include the one-time tokens to build each design. Mark my volume with a "you are here" line, and mark any break-even point. Plot only steps that use tokens. Then explain the chart in plain language: what I'd save in a year at my volume, and what would have to change for the answer to flip. List your assumptions.

## Which one first?

> Here are the tasks I do with AI today, with rough volumes: [list them]. For each one, say how its tokens grow with volume, whether my volume is big enough for that to matter, and whether converting to hybrid or script would change the shape of the growth. Then rank them by return on my effort: tokens saved in a year against the work to convert. Show one table and one chart, with my volume marked on each line.
