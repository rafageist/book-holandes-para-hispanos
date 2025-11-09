from __future__ import annotations

from pathlib import Path

ACCENT_MAP = {
    "Introduccion": "Introducción",
    "introduccion": "introducción",
    "Descripcion": "Descripción",
    "descripcion": "descripción",
    "Leccion": "Lección",
    "Lecciones": "Lecciones",
    "leccion": "lección",
    "lecciones": "lecciones",
    "Seccion": "Sección",
    "seccion": "sección",
    "pronunciacion": "pronunciación",
    "Pronunciacion": "Pronunciación",
    "Gramatica": "Gramática",
    "gramatica": "gramática",
    "Ortografia": "Ortografía",
    "ortografia": "ortografía",
    "Autodiagnostico": "Autodiagnóstico",
    "autodiagnostico": "autodiagnóstico",
    "evaluacion": "evaluación",
    "Evaluacion": "Evaluación",
    "habitacion": "habitación",
    "habitaciones": "habitaciones",
    "Numero": "Número",
    "numero": "número",
    "Numeros": "Números",
    "numeros": "números",
    "Resumen": "Resumen",
    "resumen": "resumen",
    "Logica": "Lógica",
    "logica": "lógica",
    "Musica": "Música",
    "musica": "música",
    "Practica": "Práctica",
    "practica": "práctica",
    "Cultura": "Cultura",
    "cultura": "cultura",
    "dificil": "difícil",
    "dificiles": "difíciles",
    "dificil": "difícil",
    "dificilmente": "difícilmente",
    "Examen": "Examen",
    "examen": "examen",
    "Andres": "Andrés",
    "andres": "andrés",
}

def fix_file(path: Path) -> None:
    original = path.read_text(encoding="utf-8")
    updated = original
    for source, target in ACCENT_MAP.items():
        updated = updated.replace(source, target)
    if updated != original:
        path.write_text(updated, encoding="utf-8")


def main() -> None:
    root = Path(".")
    for md_file in root.rglob("*.md"):
        if md_file.parts[0] == ".git":
            continue
        fix_file(md_file)


if __name__ == "__main__":
    main()
