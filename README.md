[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/c/make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/BeastOrange/thankful-judge-20261127/rank.svg)](https://make.fun/c/make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/BeastOrange/thankful-judge-20261127/reward.svg)](https://make.fun/c/make-the-ai-judge-feel-thankful-20261127-1600)

# Thankful Judge Competition Entry

This repository contains an entry for the make.fun competition **Make the AI Judge Feel Thankful**.

## Overview

The program generates the competition submission by deterministically writing a contemplative, welcoming message to `/output/entry.txt` using standard library Python. It asserts that the message length is within the required 1 to 1000 character limit prior to writing.

## How to Run

Ensure `/output` exists and execute the entry script:

```bash
mkdir -p /output
python3 main.py
```

The script writes `/output/entry.txt` encoded in UTF-8 with a single trailing newline.
