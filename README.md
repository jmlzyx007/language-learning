# 📚 Language Learning Journal

Daily reading tracker for French (professional level) and English — one article per day, key expressions, personal summaries.

**Started:** March 2026  
**Goal:** 1 article/day · 30–60 min commute · professional & cultural register

---

## Progress

| Week | FR articles | EN articles | Words saved |
|------|------------|------------|-------------|
| Week 1 | 0/4 | 0/3 | 0 |
| Week 2 | 0/4 | 0/3 | 0 |

> Update this table manually each week, or run `python stats.py` to generate it automatically.

---

## Structure

```
language-learning/
├── README.md             ← this file (progress overview)
├── fr/                   ← French articles
│   └── YYYY-MM-DD.md
├── en/                   ← English articles
│   └── YYYY-MM-DD.md
├── vocabulary.md         ← master vocabulary list (all expressions)
└── stats.py              ← optional script to generate stats
```

---

## How to add a new entry

1. Create a file in `fr/` or `en/` named with today's date: `2026-03-26.md`
2. Use the template below
3. Commit: `git add . && git commit -m "day 1 - Le Monde - déficit public"`

---

## Entry template

```markdown
## [Title of article](url)

**Source:** Le Monde / The Economist / etc.  
**Date:** YYYY-MM-DD  
**Theme:** Politics / Economy / Culture / Society  
**Difficulty:** ⭐ easy · ⭐⭐ medium · ⭐⭐⭐ challenging

---

### My summary (in my own words)

<!-- 3–5 sentences, no copy-paste from the article -->

---

### Key expressions

| Expression | Meaning / context |
|---|---|
| expression 1 | definition |
| expression 2 | definition |
| expression 3 | definition |

---

### Notes

<!-- Anything worth remembering: tone, argument structure, style -->
```

---

## Vocabulary index

All saved expressions are compiled in [`vocabulary.md`](./vocabulary.md).