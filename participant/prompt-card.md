# Prompt card

Copy and adapt. The starter CLAUDE.md already includes the first one.

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
