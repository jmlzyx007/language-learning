#!/bin/bash
# Usage:
#   ./new_day.sh fr        → creates fr/YYYY-MM-DD.md
#   ./new_day.sh en        → creates en/YYYY-MM-DD.md

LANG_ARG=${1:-fr}
DATE=$(date +%Y-%m-%d)
FILE="${LANG_ARG}/${DATE}.md"

if [ "$LANG_ARG" != "fr" ] && [ "$LANG_ARG" != "en" ]; then
  echo "Usage: ./new_day.sh fr|en"
  exit 1
fi

if [ -f "$FILE" ]; then
  echo "File $FILE already exists."
  exit 1
fi

if [ "$LANG_ARG" = "fr" ]; then
cat > "$FILE" << 'EOF'
## [Titre de l'article](url)

**Source:**   
**Date:** DATE_PLACEHOLDER
**Thème:** Politique / Économie / Culture / Société  

---

### Résumé

<!-- 3–5 phrases dans tes propres mots — pas de copier-coller -->

---

### Expressions clés

| Expression | Sens / contexte |
|---|---|
| | |
| | |
| | |
EOF
else
cat > "$FILE" << 'EOF'
## [Title of article](url)

**Source:**   
**Date:** DATE_PLACEHOLDER
**Theme:** Politics / Economy / Culture / Society  

---

### Summary

<!-- 3–5 sentences in your own words — no copy-paste -->

---

### Key expressions

| Expression | Meaning / context |
|---|---|
| | |
| | |
| | |
EOF
fi

# Inject today's date
sed -i "s/DATE_PLACEHOLDER/${DATE}/" "$FILE"

echo "Created: $FILE"
echo "Open with: code $FILE   (or vim/nano/any editor)"
