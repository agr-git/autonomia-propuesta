# Codigo fuente del artefacto

`index.html` no se edita a mano. Se genera.

## Como regenerar

```bash
cd caravela/src
python3 build.py          # escribe caravela-growth-lead-propuesta-v2.html
```

## Archivos

| Archivo | Contenido |
|---|---|
| `build.py` | Plantilla HTML completa (CSS, marcado, JS) mas la inyeccion de assets. Editar AQUI, no en index.html. |
| `assets_b64.json` | 3 claves: `logo` (PNG), `foto` (retrato JPEG 520px), `cv` (PDF, 205 KB). |
| `pics_b64.json` | 5 claves: fotos de perfil de manjarres, nicole, adela, giancarlo, juanca. |
| `push-to-github.sh` | Script de publicacion. |

## Como funciona la inyeccion

La plantilla usa marcadores que se sustituyen al final de `build.py`:

```
__LOGO__            -> assets_b64.json["logo"]
__FOTO__            -> assets_b64.json["foto"]
__CV__              -> assets_b64.json["cv"]
__P_MANJARRES__     -> pics_b64.json["manjarres"]
__P_NICOLE__        -> pics_b64.json["nicole"]
__P_ADELA__         -> pics_b64.json["adela"]
__P_GIANCARLO__     -> pics_b64.json["giancarlo"]
__P_JUANCA__        -> pics_b64.json["juanca"]
```

El script verifica al final que no queden marcadores sin sustituir.

## Falta para la v3

Las miniaturas de las publicaciones usadas como evidencia en los hallazgos
01, 03, 04 y 06. Se intentaron descargar pero los strings base64 se corrompieron
en la transferencia entre entornos. El metodo correcto y la lista de las 11
piezas con sus enlaces permanentes esta en
`../handoffs/contenido-y-arquitectura.md`, seccion 6.2.

Convencion sugerida al resolverlo: crear `ev_b64.json` con las claves
`h1_li`, `h1_ig`, `h3_sidra`, `h3_yacur`, `h3_oaxaca`, `h3_harvest`,
`h3_pink`, `h4_direct`, `h4_julian`, `h6_ceo`, `h6_jose` y añadir en
`build.py` la sustitucion `__EV_<CLAVE>__`.
