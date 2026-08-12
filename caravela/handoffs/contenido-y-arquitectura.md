# HANDOFF · Claude Design

## Propuesta Growth & Strategic Projects Lead para Caravela Coffee

**De:** Alejandro Gil Rivera (autor, orquestador y responsable del análisis)
**Para:** Claude Design
**Versión origen:** `caravela-growth-lead-propuesta-v2.html` (596 KB, autocontenido)
**Objetivo de esta iteración:** v3
**Fecha:** 12 de agosto de 2026

---

# 0. LA MISIÓN EN UNA FRASE

Convertir un documento que hoy **se lee como un informe** en un artefacto que **se recorre como una landing**, sin perder un solo dato, y que al abrirse comunique de inmediato que **detrás hubo un humano investigando**, no un modelo generando texto.

El contenido ya está investigado, verificado y es correcto. **No hay que añadir información: hay que quitar palabras y añadir estructura visual.** Cada párrafo que sobrevive debe justificar su existencia.

---

# 1. EL LECTOR

**Alejandro Cadena.** Cofundador y CEO de Caravela Coffee. Veinticinco años construyendo la compañía. Colombiano, opera en inglés y español. Lee LinkedIn a diario y su perfil personal rinde 3,6 veces más que la página corporativa de su empresa (lo sabe o lo intuye, pero nunca lo había visto medido).

**Cómo lee:** rápido, en móvil o en pantalla, entre reuniones. Va a escanear primero y leer después solo lo que le enganche. Si en los primeros quince segundos percibe "esto es un texto genérico de consultor", cierra.

**Qué le importa:** los números de su negocio, la evidencia verificable, y que quien le escribe entienda de café de verdad. Dijo textualmente que no sabe comunicar y que valora a las personas que **piensan y hacen**.

**Qué lo aleja:** el lenguaje de agencia. Ya contrató una agencia de community management y no funcionó. Cualquier olor a plantilla activa esa memoria.

**El riesgo específico a combatir:** que asuma que el documento fue generado automáticamente y lo lea en diagonal. La defensa no es escribir "esto lo hice yo": es **mostrar el rastro del trabajo humano** (ver sección 8).

---

# 2. QUÉ FALLA EN LA v2 (diagnóstico honesto del artefacto)

| Sección | Problema | Dirección de arreglo |
|---|---|---|
| Hero + El Reto | Funciona bien. Buen ritmo, buen contraste. | Conservar el enfoque. Solo pulir. |
| **Modus operandi** | Cuatro tarjetas con párrafo largo cada una. Denso. | **Convertir en diagrama de proceso (BPM)**: el ciclo de una misión, visual. |
| **Por qué este perfil** | Dos bloques de texto corrido con demasiados nombres propios. | **Palabras clave + logos + iconos.** Añadir enlace al sistema construido. |
| **Misión: resultados clave** | Siete KR. Varios son actividades disfrazadas de resultado. | **Reducir a 3 KR reales.** Lo demás baja a entregables por fase. |
| **Objetivo del rol (M1)** | Prometía mover el lifetime value en 120 días. **No es realista.** | **Reinterpretado.** Ver sección 5.2. Es la corrección conceptual más importante. |
| **Riesgos** | Cinco tarjetas extensas. Ocupan más peso visual del que merecen. | **Tarjetas verticales pequeñas, colapsables.** Título visible, detalle al desplegar. |
| **Línea base por canal** | Ocho indicadores en rejilla plana. No se distinguen los canales. | **Gráficos pequeños por indicador.** Comparar LinkedIn vs Instagram visualmente. |
| Hallazgos 01 a 06 | **El análisis es sólido. Conservar casi tal cual.** | Solo añadir miniaturas de evidencia y aligerar párrafos. |
| Formato | Diseñado solo para pantalla. | **HTML + PDF.** Ver sección 7. |

---

# 3. BRANDING BOOK · CARAVELA COFFEE

Extraído el 12 de agosto de 2026 del sitio oficial y del logo oficial. **Los tres primeros hexadecimales están escritos literalmente en el código del sitio; el olivo se muestreó píxel a píxel del logo.** No inventar colores adicionales.

## 3.1 Paleta

| Token | Hex | Origen | Uso |
|---|---|---|---|
| `--olive` | `#4E4E24` | **Muestreado del logo** (25,7% de píxeles opacos) | Color de marca principal. Fondos de sección, tipografía de titulares. |
| `--olive-d` | `#3A3A1B` | Derivado | Fondos profundos, citas destacadas, pie. |
| `--olive-l` | `#6B6B33` | Derivado | Bordes y estados intermedios. |
| `--gold` | `#D6BE5C` | **Literal en el sitio** (`style="color:#D6BE5C"`) | Acento primario sobre olivo. Titulares en secciones oscuras. |
| `--pink` | `#E0B2BB` | **Literal en el sitio** (`style="color:#E0B2BB"`) | Acento secundario. Bloque "Empowering Communities". |
| `--terra` | `#DB8358` | **Literal en el sitio** (`style="color:#DB8358"`) | Acento de énfasis. "Making Coffee Better". Datos críticos. |
| `--sage` | `#B7C4A0` | Derivado del token `green-20/30` | Estados positivos, riesgo bajo. |
| `--cream` | `#F7F4E9` | Derivado del token `main` | Fondo principal claro. |
| `--cream2` | `#EFE9D8` | Derivado | Fondos alternos, pistas de gráficos. |
| `--white` | `#FFFDF7` | Derivado | Tarjetas sobre crema. |
| `--ink` | `#2A2A14` | Derivado del olivo | Texto principal. |
| `--txt2` | `#78785F` | Derivado | Texto secundario. |
| `--bdr` | `#DDD6C0` | Derivado | Bordes estándar. |

**Tokens Tailwind reales del sitio de Caravela** (para referencia de nomenclatura): `bg-brown`, `text-main`, `bg-main`, `bg-main-light`, `bg-yellow`, `bg-yellow-light`, `bg-green-20`, `bg-green-30`, `bg-pink`, `bg-orange`.

## 3.2 Tipografía

El sitio usa `font-bayard` (display, siempre en mayúsculas), `font-robotoc` (Roboto Condensed) y `font-vtcmarsha`. **Bayard no está en Google Fonts.**

| Rol | Fuente sustituta | Justificación |
|---|---|---|
| Display / titulares | **Archivo** 800-900, mayúsculas, `letter-spacing:-.02em` | Es la aproximación más cercana a Bayard: geométrica, condensable, peso alto. |
| Cuerpo | **DM Sans** 400-500 | Humanista, legible en pantalla y papel. |
| Datos y cifras | **DM Mono** 500 | Distingue el dato del texto. Refuerza la sensación de instrumento de medición. |

Escala: H1 `clamp(34px,6.4vw,74px)` · H2 `clamp(27px,4.1vw,46px)` · H3 21px · cuerpo 16px · nota 11,5px.

## 3.3 Patrones de movimiento del sitio de Caravela

Replicar estos, están tomados del marcado real:

- Secciones a **pantalla completa** (`h-screen` / `min-h-screen`).
- Entradas laterales con `translate-x` desde `-100%`.
- Fundidos con `transition-opacity ease-in duration-[1200ms]`.
- **Marca de agua del logo rotada 30° al 5% de opacidad**, escalada en X negativo, en zonas amplias.
- Video a pantalla completa en el hero (aquí sustituido por composición tipográfica).
- Bloques de color contiguos en rejilla de tres (rosa / naranja / verde) con texto en mayúsculas centrado.

## 3.4 Reglas de marca

- **Nunca** poner el logo de Caravela sobre fondo que no sea crema, blanco u olivo.
- La marca de agua siempre por debajo del 6% de opacidad.
- El olivo es de Caravela; el terracota es el acento de **este documento** (los datos propios). Mantener esa distinción: lo que es de Caravela va en olivo y dorado, lo que aporta el autor va en terracota.

---

# 4. ARQUITECTURA DE LA v3

Scroll continuo, seis secciones ancladas, navegación superior que aparece al pasar el hero, barra de progreso.

```
HERO ...................... pantalla completa, olivo, tipografía grande
01 EL RETO ................ crema · 4 KPI + cita del CEO + regla de dos audiencias
02 EL ROL ................. olivo · foto + 4 métricas + DIAGRAMA BPM + keywords
03 LA MISIÓN .............. blanco · 3 KR + fases + timeline + riesgos colapsables
04 LO QUE DICEN LOS DATOS . crema · línea base con gráficos + 6 hallazgos
05 INSUMOS ................ olivo · 10 preguntas
06 SIGUIENTE .............. blanco · 3 pasos + cierre
```

**Ritmo cromático:** oscuro → claro → blanco → claro → oscuro → blanco. Ya funciona en la v2, conservar.

---

# 5. CONTENIDO FINAL (usar este texto, ya acotado)

## 5.1 HERO

```
Eyebrow:  PROPUESTA DE ROL Y PRIMERA MISIÓN
H1:       GROWTH & STRATEGIC PROJECTS LEAD
Bajada:   Caravela tiene las mejores historias del café de especialidad
          latinoamericano. Hoy viven en la intranet.
Meta:     Para: Alejandro Cadena, CEO  ·  De: Alejandro Gil Rivera
          Misión 1: 100 a 120 días  ·  Incluye: Inception Report v0
```

La bajada actual tiene 42 palabras. **Reducir a las dos frases de arriba.**

## 5.2 CORRECCIÓN CONCEPTUAL CRÍTICA · Objetivo del rol

La v2 prometía **aumentar el lifetime value de los tostadores** en la ventana de la misión. **Eso no es realista y hay que cambiarlo.** El ciclo de venta de café verde es largo; en 120 días no se cierran recompras atribuibles a contenido. Prometerlo destruye credibilidad ante un CEO que conoce su propio ciclo comercial.

**Reemplazar por esto:**

> ### Objetivo del rol
> Convertir los activos estratégicos de Caravela (datos, relaciones, calidad, presencia en origen) en crecimiento medible. En la primera misión eso significa **construir el instrumento de medición, no forzar el resultado**: definir qué es el valor de una relación en Caravela, establecer su línea base para las dos audiencias, y abrir el primer flujo de demanda atribuible a contenido.

Y las cuatro métricas del rol quedan así (tarjetas pequeñas, no párrafos):

| # | Métrica | Horizonte |
|---|---|---|
| 01 | **Valor de relación con el tostador**: años de vínculo, volumen, número de orígenes comprados, participación en programas de impacto | Línea base en misión 1, movimiento a 12-18 meses |
| 02 | **Valor de relación con el productor**: años vendiendo a Caravela, volumen, participación en PECA, asistencia técnica recibida, visibilidad obtenida | Línea base en misión 1, movimiento a 12-18 meses |
| 03 | **Demanda atribuible a contenido**: leads y conversaciones comerciales trazables al funnel | Primeros datos en misión 1 |
| 04 | **Conversión de lead a conversación**: tasa y tiempo | Se instrumenta en misión 1, se optimiza después |

**Nota de diseño:** las métricas 01 y 02 deben verse como un par simétrico (tostador / productor). Es la manifestación visual de la regla de las dos audiencias.

## 5.3 MODUS OPERANDI → DIAGRAMA BPM

**Eliminar las cuatro tarjetas de texto.** Sustituir por un diagrama SVG del ciclo de una misión, con esta secuencia:

```
[CEO] ──confía una misión──▶ [ENCUADRE]
                                 │  objetivos + KR fijados en conjunto
                                 ▼
                            [DIAGNÓSTICO]
                                 │  datos internos + externos
                                 ▼
                            [DISEÑO] ◀──────────┐
                                 │              │
                                 ▼              │ aprendizaje
                            [EJECUCIÓN]         │ de cada ciclo
                                 │  equipo armado por misión
                                 ▼              │
                            [MEDICIÓN] ─────────┘
                                 │  tablero visible sin pedir reportes
                                 ▼
                            [DECISIÓN]
                          escalar / iterar / cerrar
                                 │
                                 ▼
                          [SIGUIENTE MISIÓN]
```

**Especificación visual:**
- Formato: SVG horizontal, `viewBox="0 0 1000 320"`, responsivo.
- Dos carriles: **CEO** (arriba, dorado) y **Growth Lead** (abajo, terracota). El CEO aparece en tres momentos: confía la misión, fija los KR, decide al cierre. El resto es del rol.
- El bucle de retroalimentación de Ejecución → Diseño debe ser **visualmente prominente**: es el argumento de "una misión, varias iteraciones".
- Etiquetas cortas dentro de cada caja (2-4 palabras). Ninguna frase larga.
- Cuatro leyendas laterales máximo, de una línea: *misiones no funciones · pensar y hacer · equipo por misión · autonomía con visibilidad*.

Este diagrama sustituye unas 180 palabras por una imagen. Es el cambio de mayor impacto del documento.

## 5.4 POR QUÉ ESTE PERFIL → KEYWORDS + LOGOS

**Eliminar los dos párrafos.** Sustituir por:

**Fila de logos** (organizaciones con las que ha trabajado, en escala de grises sobre crema, altura uniforme 28px):
`IDH` · `Conservation International` · `CRECE` · `NKG Group` · `GIZ` · `Starbucks` · `Ishimitsu` · `Renault` · `Sistema B`

**Rejilla de credenciales** (icono + cifra + etiqueta de máximo 5 palabras):

| Icono | Dato | Etiqueta |
|---|---|---|
| Hoja / cafeto | **15 ha** | Finca de café propia, Eje Cafetero |
| Taza | **84-85** | Puntos de taza, venta a Alemania |
| Base de datos | **€80.000** | Sistema de información cafetera (HYLEA) |
| Globo | **4** | Idiomas de trabajo |
| Sello B | **Multiplicador B** | Certificado, marco B Corp |
| Código | **Sistema propio** | Motor de contenido en producción |

**Bloque destacado con enlace** (esto es nuevo y es importante):

> **El sistema que propongo construir, ya lo construí.**
> Motor propio de contenido en Python: extracción vía Apify, normalización, cálculo de métricas semanales y tablero de resultados, desplegado en servidor propio con rutina automática. El diagnóstico de la sección 04 se produjo con ese mismo instrumental en menos de 24 horas.
> `github.com/agr-git` → repositorio `autonomia-linkedin-story-engine`

**Advertencia para el diseño:** enlazar al perfil de GitHub, **no** presentar métricas de resultados de ese sistema. Se vende la capacidad demostrada de construir el instrumento, no un caso de éxito.

## 5.5 LOS TRES RESULTADOS CLAVE (reemplazan a los siete)

Los siete KR de la v2 mezclaban resultados con actividades. Estos tres son resultados verificables; el resto baja a entregables por fase.

> ### KR 1 · Saber quién nos escucha
> Clasificación de la audiencia que interactúa en LinkedIn e Instagram por tipo (productor, tostador, industria, otro), con porcentaje por canal.
> **Meta:** al menos el 70% de los perfiles que interactuaron en los últimos seis meses, clasificados.
> **Por qué importa:** hoy nadie tiene este dato. Sin él, toda segmentación es una suposición.

> ### KR 2 · Abrir demanda atribuible
> Conversaciones comerciales nuevas originadas en contenido, registradas y trazables de punta a punta.
> **Meta:** N conversaciones. **El valor de N se fija con el CEO en el kickoff**, anclado al plan comercial del año.
> **Por qué importa:** es la prueba de que la comunicación puede ser un canal de ingreso y no un centro de costo.

> ### KR 3 · Instalar el medidor de valor de relación
> Métricas de valor de relación definidas y con línea base establecida para las dos audiencias, operando en un tablero que el CEO consulta por su cuenta.
> **Meta:** definición cerrada y línea base poblada para tostadores y productores.
> **Por qué importa:** en 120 días no se mueve el lifetime value, pero sí se construye el instrumento que permitirá medirlo. Sin instrumento, cualquier cifra futura es una opinión.

**Nota de honestidad métrica que debe conservarse visible** (caja pequeña, no párrafo):
> El ciclo de venta de café verde es largo. En 120 días se miden con rigor los leads y las conversaciones abiertas. Los cierres se atribuyen en la ventana que dicte el ciclo real de la compañía, no en la de la misión.

## 5.6 FASES (los entregables que bajaron de los KR)

Mantener la estructura de cinco fases de la v2, pero cada una con **máximo 2 líneas** y sus entregables como etiquetas, no como prosa.

| Fase | Semanas | Entregables (etiquetas) |
|---|---|---|
| **00 Inception** | Entregado | Diagnóstico externo v0 · Marco de rol y misión · 10 preguntas |
| **01 Diagnóstico** | 1 a 4 | Clasificación de audiencia · Benchmark competidores · Inmersión en intranet · Mapa de voces |
| **02 Estrategia** | 4 a 6 | 4 líneas editoriales · Banco de 20+ historias · Tablero del CEO · Equipo armado |
| **03 Iteración** | 6 a 14 | 4 ciclos quincenales · Piloto en tiendas · Funnel instrumentado |
| **04 Cierre** | 14 a 17 | Reporte contra KR · Curva de rendimiento · Propuesta de Misión 2 |

## 5.7 RIESGOS → TARJETAS COLAPSABLES

Cinco riesgos, **tarjetas verticales pequeñas en rejilla de 3+2**. Estado cerrado: solo nivel, título y un icono. Estado abierto: descripción y mitigación.

| Nivel | Título (visible siempre) | Detalle (colapsado) |
|---|---|---|
| Alto | Acceso tardío a datos internos | Las historias con más potencial viven en la intranet. Si el acceso se demora, la fase 02 arranca con material incompleto. **Mitigación:** candado explícito en kickoff (qué datos, quién, cuándo). Ruta alterna con datos externos mientras se abre. |
| Medio | Fricción con quien comunica hoy | Si el rol se percibe como reemplazo, se fabrica resistencia el día uno. **Mitigación:** el rol es capa de estrategia y medición sobre quien ejecuta. La fase 01 mapea quién hace qué. |
| Medio | Atribución en ciclo de venta largo | El café verde no se vende con un clic. **Mitigación:** los KR separan lo medible en la ventana de lo medible en el ciclo real. |
| Medio | La fórmula que funciona se agota | Los formatos que hoy rinden pierden efectividad al repetirse. **Mitigación:** el diseño por iteraciones es la respuesta. Cada ciclo mide rendimiento por formato y ángulo. |
| Bajo | Repetir la experiencia de la agencia | Caravela ya tercerizó community management sin éxito. **Mitigación:** diferencia estructural (ejecución sin estrategia frente a rol con misiones y KR). El kickoff documenta qué falló. |

**Peso visual:** esta sección no debe ocupar más de una pantalla. En la v2 ocupa tres.

## 5.8 LÍNEA BASE POR CANAL → GRÁFICOS

**Reemplazar la rejilla de ocho KPI planos.** Datos verificados el 12 de agosto de 2026:

### Gráfico A · Audiencia total y reparto
- **Tipo:** dona o barra apilada horizontal.
- **Total al centro:** `50.728`
- LinkedIn `23.466` (46,3%) → color olivo
- Instagram `27.262` (53,7%) → color terracota
- **Titular:** "La audiencia está repartida casi por mitades. El mensaje no."

### Gráfico B · Tasa de interacción por canal
- **Tipo:** dos barras horizontales comparadas.
- LinkedIn: `0,10%` (24,4 reacciones sobre 23.466 seguidores)
- Instagram: `0,18%` (47,9 likes sobre 27.262 seguidores)
- **Titular:** "Instagram convierte casi el doble de su audiencia en interacción."

### Gráfico C · Rendimiento por formato (Instagram)
- **Tipo:** barras horizontales, ya existe en la v2 y funciona.
- Carrusel `62,4` likes (n=12) → terracota
- Video `32,6` (n=8) → dorado
- Imagen `22,8` (n=4) → sage
- **Titular:** "El formato que mejor rinde no es el que más se usa."

### Gráfico D · Conversación
- **Tipo:** representación de proporción (11 de 20 marcadores apagados).
- `0,7` comentarios por publicación en LinkedIn
- `11 de 20` publicaciones sin ningún comentario
- **Titular:** "Difusión sin diálogo."

### Gráfico E · Alcance por tipo de voz
- **Tipo:** tres barras comparadas. **Es el gráfico más importante del documento.**
- Perfil del CEO `88,0` reacciones de media → terracota, destacado
- José Manjarres `25,2` → dorado
- Página corporativa `24,4` → olivo claro
- **Anotación superpuesta:** "12 de agosto: el CEO obtuvo 142 reacciones. La página, 6. El mismo día."
- **Titular:** "La voz personal rinde 3,6 veces más que la corporativa."

### Cadencia (dato suelto, no gráfico)
`2,3` publicaciones por semana en LinkedIn · `3.389` publicaciones históricas en Instagram

## 5.9 HALLAZGOS 01 a 06

**Conservar el análisis textual casi tal cual.** Está verificado y es el corazón del documento. Solo dos cambios:

1. **Añadir miniatura de la pieza de evidencia** en cada tarjeta (ver sección 6.2).
2. Reducir cada párrafo de hallazgo a **máximo 3 líneas**. El detalle largo puede ir en un desplegable.

Los seis hallazgos, con su cifra ancla:

| # | Hallazgo | Cifra ancla |
|---|---|---|
| 01 | Un solo mensaje duplicado para dos audiencias | **16 de 20** publicaciones idénticas entre canales |
| 02 | Se le habla al productor en el idioma del tostador | **100%** de LinkedIn en inglés |
| 03 | El formato que mejor rinde no es el que más se usa | Carrusel **1,9x** sobre video |
| 04 | Difusión sin conversación | **11 de 20** publicaciones sin comentarios |
| 05 | Un canal de autoridad dormido | Estudio de costo de producción: **casi 4 años** sin actualizar |
| 06 | La estrategia que se busca ya funciona, sin sistema | Perfil del CEO **3,6x** sobre la página |

**Hallazgo 02 · conservar obligatoriamente esta salvedad:**
> Esta afirmación se apoya en la lectura del CEO más el dato de idioma: es una hipótesis fuerte, no un hecho verificado. Por eso existe el KR 1.

Distinguir lo verificado de lo inferido es una de las señales más potentes de que hubo criterio humano. **No eliminar.**

## 5.10 BANCO DE VOCES

Conservar la rejilla de seis perfiles con foto. Funciona. Solo reducir cada descripción a **una línea**.

| Persona | Cargo | Ángulo (una línea) | Estado |
|---|---|---|---|
| Alejandro Cadena | Cofundador y CEO | La voz de mayor alcance: 88 reacciones de media | Ya publica |
| José Manjarres | Café de especialidad, 7 orígenes | Su titular ya es el mensaje al tostador | Ya publica |
| Giancarlo Ghiretti | Cofundador, CFO y COO desde 2002 | 24 años de historia y la economía del modelo | Sin actividad editorial |
| Nicole Freydell | Brand Business Leader | Contraparte natural del rol: se diseña con ella | Aliada clave |
| Adela Vavreckova | Product Specialist, Reino Unido | Fue tostadora y compradora en Londres: fue el cliente | Puente con tostador UE |
| Juan Camilo Aristizabal | Business Development Lead | Dueño del funnel comercial a medir | Vínculo con pipeline |

## 5.11 SIGUIENTES PASOS

Conservar los tres pasos. **Corregir el paso 02** para que sea explícito:

> **02 · Acuerdo de colaboración.** El modelo de vinculación y las condiciones económicas se conversan directamente **en la sesión de kickoff**. El formato de misión está propuesto precisamente para eso: que Caravela compre resultados verificables con reglas claras para ambas partes, dentro del principio de equidad de la casa.

---

# 6. ASSETS

## 6.1 Disponibles y verificados

| Asset | Estado | Nota |
|---|---|---|
| Logo Caravela | Embebido, PNG base64 (256x37) | Fuente del muestreo de color |
| Foto de Alejandro Gil | Embebida, JPEG 520x520 | Recorte de retrato |
| CV en PDF | Embebido base64, 205 KB | Botón de descarga |
| Fotos de las 6 voces | Embebidas, JPEG 64-112px | Extraídas de LinkedIn el 12 ago 2026 |

## 6.2 PENDIENTE · Miniaturas de evidencia

**Tarea específica para Claude Design.** Cada tarjeta de evidencia de los hallazgos 01, 03, 04 y 06 debe llevar la miniatura de la publicación. No se pudieron embeber en la v2 porque las URLs del CDN de Instagram traen tokens que expiran en horas.

**Método:**
1. Ejecutar el actor de Apify `apify/instagram-post-scraper` sobre `caravelacoffee` y `apimaestro/linkedin-company-posts` sobre `caravela-coffee`.
2. Tomar el campo `displayUrl` (Instagram) o `media.items[0].thumbnail` (LinkedIn).
3. Descargar, recortar a cuadrado, redimensionar a 96px, calidad 45.
4. Embeber como base64.

**Piezas necesarias (11):**

| Clave | Publicación | Métrica |
|---|---|---|
| `h1_li` | LinkedIn "Traceability is no longer a back-office requirement" (15 jul) | 38 reacciones |
| `h1_ig` | Instagram mismo texto, carrusel (14 jul), `Daw57NOjGty` | 82 likes |
| `h3_sidra` | Instagram "Special Release: Ecuador Sidra", `DbWAVgPFBwB` | 113 likes, 7 com |
| `h3_yacur` | Instagram "New Coffee Release: Ecuador Yacur", `DZ73fsqm6Yj` | 106 likes |
| `h3_oaxaca` | Instagram "Coffee brewed in Oaxaca City", `DaDz8LRGWQM` | 101 likes |
| `h3_harvest` | LinkedIn "Harvest is moving across Colombia, Ecuador and Peru" | 38 reacciones |
| `h3_pink` | LinkedIn "Pink Bourbon has become one of Colombia's..." | 35 reacciones |
| `h4_direct` | LinkedIn "Direct Trade has become one of specialty coffee's..." (12 ago) | 6 reacciones, 0 com |
| `h4_julian` | LinkedIn "Knowledge creates value..." (Julián Olivera, productor) | 10 reacciones, 0 com |
| `h6_ceo` | LinkedIn perfil de Alejandro Cadena (12 ago) | **142 reacciones, 15 com** |
| `h6_jose` | LinkedIn "Harvest Coffee Update: Peru" de José Manjarres | 42 reacciones |

**Enlaces permanentes de las publicaciones** (estos no expiran, van en el `href` de cada tarjeta):

```
h1_li      linkedin.com/posts/caravela-coffee_traceability-is-no-longer-a-back-office-requirement-activity-7483067975076511744-bKOH
h1_ig      instagram.com/p/Daw57NOjGty/
h3_sidra   instagram.com/p/DbWAVgPFBwB/
h3_yacur   instagram.com/p/DZ73fsqm6Yj/
h3_oaxaca  instagram.com/p/DaDz8LRGWQM/
h3_harvest linkedin.com/posts/caravela-coffee_harvest-is-moving-across-colombia-ecuador-activity-7478888123460927488-yH-F
h3_pink    linkedin.com/posts/caravela-coffee_pink-bourbon-has-become-one-of-colombias-activity-7472543665308155904-4vrG
h4_direct  linkedin.com/posts/caravela-coffee_direct-trade-has-become-one-of-specialty-activity-7493214748411494400-GDKD
h4_julian  linkedin.com/posts/caravela-coffee_knowledge-creates-value-when-it-leads-to-activity-7488896320317865984-ycJv
h6_ceo     linkedin.com/posts/alejandro-c-74241a_following-my-post-yesterday-i-wanted-to-ugcPost-7493061742126731265-KsGO
h6_jose    linkedin.com/posts/josemanjarres_specialtycoffee-greencoffee-coffeesourcing-activity-7480969102820409344--tJz
```

**Hallazgo 05 (blog)** no tiene miniaturas disponibles: resolverlo con composición tipográfica (título del artículo + fecha grande + los años transcurridos como dato visual).

## 6.3 Logos de terceros

Para la sección "Por qué este perfil" hacen falta los logotipos de IDH, Conservation International, CRECE, NKG Group, GIZ, Starbucks, Ishimitsu, Renault y Sistema B. Tratamiento: escala de grises, opacidad 65%, altura uniforme, sin recuadros.

---

# 7. DOBLE FORMATO · HTML Y PDF

El documento se envía por correo y también se imprime. Debe funcionar en ambos.

## Requisitos de impresión

```css
@media print {
  /* fondos de sección deben imprimirse */
  * { -webkit-print-color-adjust: exact; print-color-adjust: exact; }

  /* cada sección arranca en página nueva */
  section { break-before: page; break-inside: avoid; }

  /* nada colapsado se pierde en papel */
  details { display: block; }
  details > summary { list-style: none; }
  details[open], details:not([open]) > * { display: block !important; }

  /* elementos que no aplican en papel */
  .nav, #prog, .scroll-hint { display: none; }

  /* animaciones desactivadas: todo visible */
  .rv, .rvx { opacity: 1 !important; transform: none !important; }

  /* enlaces: mostrar destino */
  a[href^="http"]::after { content: " (" attr(href) ")"; font-size: 9px; color: #78785F; }

  /* tarjetas y gráficos no se parten */
  .card, .voz, .risk, .kpi, svg { break-inside: avoid; }
}
@page { size: A4; margin: 14mm; }
```

**Regla dura:** ningún dato puede existir solo en un estado interactivo. Los riesgos colapsables deben desplegarse en impresión. Los gráficos deben ser SVG (no canvas) para que impriman nítidos.

**Extensión objetivo en PDF:** 8 a 10 páginas A4. La v2 daría alrededor de 16.

---

# 8. LA SEÑAL HUMANA

Este es el requisito más difícil y el más importante. El documento debe demostrar que hubo una persona investigando, no un modelo redactando.

**Qué lo demuestra (incorporar todo):**

1. **Fecha y método de extracción visibles.** "Extraído el 12 de agosto de 2026 mediante pipelines propios de scraping" aparece bajo cada bloque de datos. Un modelo no puede fabricar esto.

2. **Distinguir lo verificado de lo inferido.** El hallazgo 02 dice explícitamente que es hipótesis y no hecho. Nadie que quiera impresionar hace esto; solo lo hace quien tiene criterio.

3. **Enlaces a las piezas reales.** Cada cifra es clicable y lleva a la publicación exacta. La verificación está a un clic.

4. **Números con decimal y n muestral.** `62,4 likes (n=12)` en lugar de "los carruseles rinden mejor". El tamaño de muestra revela que alguien contó.

5. **Reconocer los límites del análisis.** El bloque "Lo que este diagnóstico todavía no ve" debe conservarse. Admitir lo que no se sabe es la firma más humana del documento.

6. **Una observación que solo alguien del gremio haría.** Ejemplo a incluir: que la única pieza reciente sobre un productor con nombre propio (Julián Olivera) quedó entre las de peor rendimiento, y que eso no es culpa de la historia sino del formato y del idioma. Ese tipo de lectura no sale de una plantilla.

7. **Nombrar a Nicole Freydell como aliada, no como obstáculo.** Un documento automático la habría ignorado. Reconocerla demuestra lectura política de la organización.

**Qué lo destruye (evitar):**
- Adjetivos de agencia: "innovador", "disruptivo", "360", "holístico", "sinergia".
- Frases de relleno: "en el mundo actual", "hoy más que nunca", "es fundamental destacar".
- Simetría perfecta en todos los bloques. Un poco de asimetría deliberada se lee como diseño, no como plantilla.
- Listas de exactamente tres elementos en todas partes.

**Prohibido en todo el documento:** guiones largos (—) y guiones medios (–). Usar dos puntos y paréntesis. Esta regla ya está aplicada en la v2 y verificada a cero. Mantenerla.

---

# 9. PRESUPUESTO DE PALABRAS

La v2 tiene aproximadamente 4.200 palabras. **Objetivo v3: 2.400 como máximo.** Recorte del 43%.

| Sección | v2 (aprox.) | v3 (objetivo) | Cómo |
|---|---|---|---|
| Hero | 60 | 30 | Bajada a dos frases |
| 01 El Reto | 480 | 320 | Fusionar los dos bloques de problema |
| 02 El Rol | 900 | 380 | BPM sustituye modus operandi; keywords sustituyen perfil |
| 03 La Misión | 1.150 | 620 | 3 KR en vez de 7; riesgos colapsados; fases en tabla |
| 04 Los Datos | 1.100 | 800 | Gráficos absorben cifras; párrafos a 3 líneas |
| 05 Insumos | 380 | 200 | Preguntas sin la explicación de "por qué" en las obvias |
| 06 Siguiente | 130 | 100 | Ya está bien |

---

# 10. CHECKLIST DE ACEPTACIÓN

**Contenido**
- [ ] El objetivo del rol ya no promete mover el lifetime value en 120 días
- [ ] Hay exactamente 3 resultados clave, ninguno es una actividad
- [ ] Las métricas de valor de relación aparecen para tostador **y** productor
- [ ] La salvedad del hallazgo 02 sobre hipótesis está intacta
- [ ] El bloque "lo que el diagnóstico no ve" está intacto
- [ ] Nicole Freydell aparece como aliada
- [ ] El paso 02 dice "en la sesión de kickoff"
- [ ] Enlace a github.com/agr-git presente
- [ ] Cero guiones largos o medios en todo el documento

**Visual**
- [ ] El modus operandi es un diagrama, no párrafos
- [ ] "Por qué este perfil" son keywords, logos e iconos
- [ ] Los riesgos ocupan como máximo una pantalla, en tarjetas colapsables
- [ ] Hay al menos 5 gráficos en la línea base
- [ ] Cada hallazgo con evidencia lleva miniatura de la publicación
- [ ] Ningún párrafo supera 4 líneas en pantalla de escritorio

**Datos (verificar contra esta tabla antes de publicar)**
- [ ] LinkedIn 23.466 · Instagram 27.262 · Total 50.728
- [ ] 24,4 reacciones y 0,7 comentarios de media en LinkedIn
- [ ] 47,9 likes de media en Instagram
- [ ] 16 de 20 publicaciones duplicadas
- [ ] 11 de 20 sin comentarios
- [ ] Carrusel 62,4 · Video 32,6 · Imagen 22,8
- [ ] CEO 88,0 · Manjarres 25,2 · Corporativa 24,4
- [ ] 142 contra 6 el 12 de agosto

**Formato**
- [ ] Imprime a PDF entre 8 y 10 páginas A4 sin cortes en tarjetas ni gráficos
- [ ] Todo lo colapsado se despliega en impresión
- [ ] Gráficos en SVG, no canvas
- [ ] Archivo único autocontenido

---

# 11. FUENTES DEL ANÁLISIS

Todos los datos de este documento provienen de extracción propia realizada el **12 de agosto de 2026**:

- Página de LinkedIn de Caravela Coffee (20 publicaciones más recientes, 12 jun a 12 ago 2026), vía actor `apimaestro/linkedin-company-posts`.
- Instagram `@caravelacoffee` (perfil y 24 publicaciones), vía actores `apify/instagram-profile-scraper` e `instagram-post-scraper`.
- Perfiles públicos de LinkedIn de las seis personas del banco de voces, vía `apimaestro/linkedin-profile-detail`.
- Sitio `caravela.coffee` (marcado completo y tokens de diseño), vía `apify/website-content-crawler`.
- Sección "Notes from the team" del sitio oficial.
- Conversación directa entre Alejandro Cadena (CEO) y Alejandro Gil Rivera, agosto de 2026: origen de las cifras de negocio (800+ productores, 25 quality lab managers en Colombia y cerca de 15 en otros orígenes, 95% de productores en Huila y Tolima, umbral de 83 puntos de taza).

Las métricas de LinkedIn e Instagram son públicas: **no incluyen impresiones ni datos de administrador**, que se incorporan en la fase 01 de la misión.
