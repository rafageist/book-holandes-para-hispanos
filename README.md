# Holandés para hispanohablantes

Repositorio en Markdown para construir un curso completo de neerlandés pensado como vault de Obsidian y, a la vez, como base de libros en PDF. El objetivo es cubrir todos los niveles (A1, A2 y los que se agreguen después) con materiales 100 % textuales, listos para imprimir.

## Visión general

- **Contenido modular**: cada nivel se organiza en carpetas numeradas (`A1/01_Les1`, `A2/02_Les2`, etc.) con cuatro archivos base (`00_Indice.md`, `01_Leccion.md`, `02_Vocabulario-…`, `03_Ejercicios-…`).
- **Libro standalone**: no se depende de audios, videos ni enlaces externos; todas las referencias a canciones o clases se convierten en lecturas o ejercicios escritos.
- **Generación de PDF**: el workflow `build-pdf-book.yml` arma un PDF por nivel usando `manifest.yml` para obtener la versión (`version: 1.0.0-draft`) y `A#/pdf-order.txt` para fijar el orden de los capítulos.
- **Complementos externos**: aunque el libro sea autosuficiente, el proyecto incorpora (en notas separadas) referencias a bibliografía, plataformas comunitarias, podcasts o cursos abiertos que sirvan a hispanohablantes residentes en los Países Bajos, Bélgica o Surinam. Estas referencias se documentan como anexos opcionales y se revisan periódicamente para reflejar nuevos hallazgos.

## Estructura actual

- `A1/` – Curso nivel A1 completo: lecciones, vocabulario general, pronunciación, ejercicios y anexos. Cada lección ya sigue la convención `00_Indice.md` + `01_Leccion.md` + materiales complementarios.
- `A2/` – Nivel en progreso. Usa el mismo formato que A1 y se irá poblando conforme se normalicen los contenidos.
- `.github/workflows/` – Automatizaciones para validar y generar los libros (por nivel).
- `manifest.yml` – Metadatos compartidos (versionamiento del libro, ajustes globales).

## Flujo de trabajo recomendado

1. **Clonar y abrir**: usa Obsidian o el editor de Markdown de tu preferencia sobre la carpeta raíz.
2. **Editar en ASCII**: todas las notas se guardan en UTF-8 pero con caracteres ASCII por compatibilidad; añade tildes y caracteres especiales solo cuando el contenido lo requiera (como en este README).
3. **Mantener enlaces internos**: aunque el PDF no use enlaces clicables, el vault debe conservar referencias cruzadas (`[[...]]` o rutas relativas) para navegar dentro de Obsidian.
4. **Actualizar `A#/pdf-order.txt`** cuando cambie la jerarquía del nivel, para que el PDF respete el orden deseado.
5. **Ejecutar el workflow**: al hacer push a la rama principal, GitHub Actions genera el PDF del nivel correspondiente con el nombre `holandes-curso-A*-<version>.pdf`.

## Línea editorial y recursos complementarios

- El libro funciona como estructura principal para autoestudio y acompañamiento de comunidades hispanohablantes en países de idioma neerlandés.
- Los recursos externos (libros recomendados, videos oficiales, plataformas gubernamentales, podcasts, guías cívicas, etc.) se recopilan en secciones específicas del nivel o en carpetas de anexos. Cada referencia debe indicar por qué es útil, cómo acceder y si requiere registro.
- Se planean actualizaciones periódicas para agregar nuevos materiales detectados en internet o recibir aportes de la comunidad. Documenta cada incorporación para que las versiones PDF reflejen la misma información.

## Buenas prácticas

- Añadir comentarios breves solo cuando sean necesarios para entender bloques complejos.
- Evitar mencionar orígenes como “videos”, “transcripts” o “profesora”; todo el material se escribe como libro independiente.
- Registrar cambios de fuentes o migraciones en `A#/processed_fuentes.txt` si corresponde a la operación diaria.
- Revisar con `rg -n` antes de subir cambios para asegurarte de que no queden caracteres corruptos ni menciones a multimedia.

## Licencia

Creative Commons Attribution 4.0 International (CC BY 4.0). Consulta `LICENSE` para los términos completos.
