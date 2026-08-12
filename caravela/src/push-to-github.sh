#!/usr/bin/env bash
# ============================================================
#  Sube los artefactos de Caravela a agr-git/autonomia-propuesta
#  Uso:  bash push-to-github.sh
#  Ejecutar DESDE la carpeta donde estan los archivos.
# ============================================================
set -euo pipefail

REPO="git@github.com:agr-git/autonomia-propuesta.git"
REPO_HTTPS="https://github.com/agr-git/autonomia-propuesta.git"
BRANCH="design-system/caravela"
SRC="$(pwd)"
WORK="${TMPDIR:-/tmp}/autonomia-propuesta"

echo "==> Origen: $SRC"

# --- verificar que los archivos existen antes de nada ---
FILES=(
  "caravela-growth-lead-propuesta-v2.html"
  "caravela-design-tokens.css"
  "caravela-logo.png"
  "caravela-logo@4x.png"
  "caravela-isotipo.png"
  "caravela-logo-knockout.png"
  "HANDOFF_Claude_Design_Caravela.md"
  "HANDOFF_Design_System_Setup.md"
)
MISSING=0
for f in "${FILES[@]}"; do
  if [ ! -f "$SRC/$f" ]; then echo "    FALTA: $f"; MISSING=1; fi
done
if [ "$MISSING" -eq 1 ]; then
  echo "==> Faltan archivos. Ejecuta el script desde la carpeta de salida."
  exit 1
fi

# --- clonar o reutilizar ---
if [ -d "$WORK/.git" ]; then
  echo "==> Repositorio ya clonado, actualizando"
  cd "$WORK" && git fetch origin && git checkout main && git pull --ff-only origin main
else
  echo "==> Clonando"
  rm -rf "$WORK"
  git clone "$REPO" "$WORK" 2>/dev/null || git clone "$REPO_HTTPS" "$WORK"
  cd "$WORK"
fi

# --- rama ---
git checkout -B "$BRANCH"

# --- estructura ---
mkdir -p caravela/assets caravela/handoffs

cp "$SRC/caravela-growth-lead-propuesta-v2.html" caravela/index.html
cp "$SRC/caravela-design-tokens.css"             caravela/design-tokens.css
cp "$SRC/caravela-logo.png"                      caravela/assets/logo.png
cp "$SRC/caravela-logo@4x.png"                   caravela/assets/logo@4x.png
cp "$SRC/caravela-isotipo.png"                   caravela/assets/isotipo.png
cp "$SRC/caravela-logo-knockout.png"             caravela/assets/logo-knockout.png
cp "$SRC/HANDOFF_Claude_Design_Caravela.md"      caravela/handoffs/contenido-y-arquitectura.md
cp "$SRC/HANDOFF_Design_System_Setup.md"         caravela/handoffs/design-system-setup.md

# --- README para que Claude Code entienda el repo al leerlo ---
cat > caravela/README.md <<'MD'
# Caravela · Sistema de propuestas y artefactos de decision

Artefactos construidos para el equipo directivo de Caravela Coffee usando su
identidad visual extraida del sitio en produccion y del logo oficial.

## Contenido

| Ruta | Que es |
|---|---|
| `index.html` | Propuesta Growth & Strategic Projects Lead v2. Archivo unico autocontenido (610 KB). Contiene el CSS completo y los componentes ya construidos. |
| `design-tokens.css` | Variables de marca. Cada color documenta su origen: verificado o derivado. |
| `assets/` | Logotipo en cuatro variantes. |
| `handoffs/contenido-y-arquitectura.md` | Que debe decir el documento. Contenido final ya acotado, 3 KR, correccion del objetivo de valor de relacion, presupuesto de palabras y checklist de aceptacion. |
| `handoffs/design-system-setup.md` | Como debe verse. Inputs del formulario de design system y reglas visuales. |

## Colores verificados (no sustituir)

| Hex | Origen |
|---|---|
| `#4E4E24` | Muestreado por pixel del logo oficial (25,7% de pixeles opacos) |
| `#D6BE5C` | Literal en el marcado de caravela.coffee |
| `#E0B2BB` | Literal en el marcado de caravela.coffee |
| `#DB8358` | Literal en el marcado de caravela.coffee |

Todo lo demas en `design-tokens.css` es derivado y ajustable.

## Componentes ya construidos en index.html

Tarjeta de KPI, tarjeta de evidencia clicable, tarjeta de riesgo con barra de
nivel, tarjeta de persona, bloque de cita, fila de fase, gantt por semanas,
barras comparativas animadas y nota de fuente.

## Pendiente en la v3

Diagrama BPM del modus operandi, tarjetas colapsables para riesgos, cinco
graficos en la linea base, miniaturas de evidencia embebidas y reduccion de
4.200 a 2.400 palabras. Detalle en `handoffs/contenido-y-arquitectura.md`.

Extraccion de marca y datos: 12 de agosto de 2026.
MD

# --- commit ---
git add caravela
if git diff --cached --quiet; then
  echo "==> Sin cambios que subir"
  exit 0
fi

git commit -m "feat: propuesta Caravela v2, tokens de marca y handoffs

- index.html: propuesta autocontenida con CSS y componentes aplicados
- design-tokens.css: 59 variables, origen documentado por color
- assets: logotipo en 4 variantes
- handoffs: contenido y arquitectura + setup de design system

Extraccion de marca y datos: 12 ago 2026"

git push -u origin "$BRANCH"

echo ""
echo "==> Listo"
echo "    Repositorio: https://github.com/agr-git/autonomia-propuesta/tree/$BRANCH/caravela"
echo "    Pega esta URL en el formulario de design system:"
echo "    https://github.com/agr-git/autonomia-propuesta"
