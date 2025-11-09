from pathlib import Path
import sys


def main() -> None:
    if len(sys.argv) != 5:
        raise SystemExit("Usage: make_cover.py <output> <level> <version> <date>")

    cover_path = Path(sys.argv[1])
    level = sys.argv[2]
    version = sys.argv[3]
    date = sys.argv[4]

    cover_text = f"""\\begin{{titlepage}}
\\centering
\\vspace*{{4cm}}
{{\\Huge Holandes para hispanohablantes}}\\\\[1.5cm]
{{\\Large Nivel {level}}}\\\\[0.5cm]
{{\\large Version {version}}}\\\\[0.5cm]
{{\\large Compilado el {date}}}\\\\[3cm]
{{\\large Curso autodidacta en formato Markdown/PDF}}\\\\
\\end{{titlepage}}
\\clearpage
"""

    cover_path.write_text(cover_text, encoding="utf-8")


if __name__ == "__main__":
    main()
