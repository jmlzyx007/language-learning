# 📚 Language Learning Journal

Daily reading tracker — one article per day, key expressions, personal summaries.

**Started:** March 2026  
**Goal:** 1 article/day · 30–60 min commute · professional & cultural register

---

## Progress

| Week | FR | EN | Expressions |
|------|----|----|-------------|
| Week 1 | 0/4 | 0/3 | 0 |
| Week 2 | 0/4 | 0/3 | 0 |

Run `python stats.py` to update this automatically.

---

## Structure

```
language-learning/
├── README.md          ← this file
├── fr/                ← French articles (one .md per day)
│   └── YYYY-MM-DD.md
├── en/                ← English articles (one .md per day)
│   └── YYYY-MM-DD.md
├── vocabulary.md      ← master list of all saved expressions
├── new_day.sh         ← creates today's file automatically
├── TEMPLATE.md        ← blank entry template
└── stats.py           ← progress summary script
```

---

## Daily workflow

```bash
# 1. Create today's file
./new_day.sh fr          # or: ./new_day.sh en

# 2. Fill in the article, summary, and expressions in your editor

# 3. Add your best expressions to vocabulary.md

# 4. Commit
git add . && git commit -m "day 3 - Les Echos - croissance française"
```

That's it. The whole thing takes 5 minutes after your reading session.

---

## Entry format

Each file follows this structure:

```markdown
## [Title](url)
**Source:** ...
**Date:** YYYY-MM-DD
**Theme:** ...

### Summary
3–5 sentences in your own words.

### Key expressions
| Expression | Meaning |
|---|---|
| ... | ... |
```

