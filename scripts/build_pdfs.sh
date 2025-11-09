#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

: "${LEVELS:?LEVELS environment variable is required}"
: "${BOOK_VERSION:?BOOK_VERSION environment variable is required}"
: "${BOOK_DATE:?BOOK_DATE environment variable is required}"

for LEVEL in $LEVELS; do
  if [ ! -d "$LEVEL" ]; then
    echo "Skipping $LEVEL (directory not found)"
    continue
  fi

  echo "Building PDF for $LEVEL"
  rm -f md-order.txt md-list-cover.txt md-list-filtered.txt "combined-$LEVEL.md" "cover-$LEVEL.md"
  ORDER_FILE="$LEVEL/pdf-order.txt"

  if [ -f "$ORDER_FILE" ]; then
    echo "Using $ORDER_FILE for ordering"
    sed -e 's/\r$//' "$ORDER_FILE" | sed '/^[[:space:]]*$/d' | sed '/^[[:space:]]*#/d' > md-order.txt
  else
    echo "Order file not found for $LEVEL; discovering markdown files"
    find "$LEVEL" -path "$LEVEL/tmp" -prune -o -path "$LEVEL/.obsidian" -prune -o -name '*.md' -print | sort > md-order.txt
  fi

  grep -v '^.*/.github/' md-order.txt > md-list-filtered.txt || cp md-order.txt md-list-filtered.txt

  COVER_FILE="cover-$LEVEL.md"
  python scripts/make_cover.py "$COVER_FILE" "$LEVEL" "$BOOK_VERSION" "$BOOK_DATE"

  printf '%s\n' "$COVER_FILE" > md-list-cover.txt
  cat md-list-filtered.txt >> md-list-cover.txt

  COMBINED="combined-$LEVEL.md"
  while IFS= read -r f; do
    if [ -f "$f" ]; then
      printf '\n\n<!-- Source: %s -->\n\n' "$f" >> "$COMBINED"
      python scripts/strip_markdown.py "$f" >> "$COMBINED"
    else
      echo "Warning: listed file '$f' not found" >&2
    fi
  done < md-list-cover.txt

  OUTPUT="holandes-curso-${LEVEL}-${BOOK_VERSION}.pdf"
  pandoc "$COMBINED" -o "$OUTPUT" \
    --pdf-engine=xelatex \
    -V mainfont="DejaVu Sans" \
    -V geometry:a4paper \
    -V geometry:margin=2.5cm \
    --toc --number-sections
done

rm -f md-order.txt md-list-filtered.txt md-list-cover.txt combined-*.md cover-*.md
