# HANDOFF · Formulario "Set up your design system"

Inputs listos para pegar en cada campo. Todo lo que sigue proviene de la extracción de marca del 12 de agosto de 2026.

---

## CAMPO 1 · Company name and blurb

**Pegar esto:**

```
Caravela Coffee · Sistema de propuestas y artefactos de decisión

Caravela es el único exportador latinoamericano de café de especialidad cuya misión
principal es hacer el café tan próspero como delicioso. Opera desde el año 2000 con
más de 200 personas en 11 países, exportación en 7 orígenes de América Latina e
importación en Australia, Norteamérica, Taiwán y Reino Unido. Es empresa B Corp.

Este design system NO es para el producto de Caravela. Es para construir artefactos
de decisión dirigidos a su equipo directivo (propuestas, diagnósticos, reportes de
misión y tableros), usando la identidad visual de Caravela para que el lector los
sienta propios y no como un documento externo.

Formato objetivo: página HTML de scroll continuo, autocontenida en un solo archivo,
que además debe imprimirse limpia a PDF de 8 a 10 páginas A4. Sin dependencias de
build. Sin frameworks. CSS con variables y SVG inline.
```

---

## CAMPO 2 · Link code from GitHub

**Pegar esta URL:**

```
https://github.com/agr-git/autonomia-propuesta
```

**Antes de pegarla, sube ahí el HTML de la v2.** Ese repositorio ya existe, es público y está descrito como "Propuesta, acceso por enlace". Es el sitio natural.

```bash
git checkout -b design-system/caravela
cp caravela-growth-lead-propuesta-v2.html .
cp caravela-design-tokens.css .
git add caravela-growth-lead-propuesta-v2.html caravela-design-tokens.css
git commit -m "feat: propuesta Caravela v2 + tokens de marca extraidos"
git push origin design-system/caravela
```

**Por qué importa:** el HTML de la v2 ya contiene 600 líneas de CSS con la paleta aplicada, los componentes construidos (tarjetas de KPI, tarjetas de evidencia, tarjetas de riesgo, rejilla de voces, gantt, barras) y el sistema de animación por IntersectionObserver. Claude Code va a extraer los patrones de ahí en lugar de inventarlos, que es exactamente lo que quieres.

**Alternativa si prefieres no publicar:** usa el campo "Link code from your computer" y arrastra la carpeta de outputs. El aviso del formulario dice que no sube todo el código, solo los archivos seleccionados.

---

## CAMPO 3 · Upload a .fig file

**Dejar vacío.** No existe archivo de Figma. Toda la identidad se extrajo del sitio en producción y del logo, que es una fuente más fiel que un Figma desactualizado.

---

## CAMPO 4 · Add fonts, logos and assets

**Adjuntar estos cinco archivos** (ya generados en tu carpeta de salida):

| Archivo | Qué es | Para qué sirve |
|---|---|---|
| `caravela-design-tokens.css` | Todas las variables CSS con el origen documentado de cada color | Es el archivo más importante. Distingue lo verificado de lo derivado |
| `caravela-logo.png` | Logotipo completo, 256x37, fondo transparente | Fuente del muestreo de color |
| `caravela-logo@4x.png` | Mismo logotipo a 1024x148 | Uso en cabeceras y alta densidad |
| `caravela-isotipo.png` | Solo la mancha, 256x256 | Marca de agua, favicon, avatar |
| `caravela-logo-knockout.png` | Versión en crema para fondo olivo | Cabecera oscura y pie |

**Tipografías: no adjuntar archivos.** Se cargan desde Google Fonts. Bayard, la display real de Caravela, no es de distribución libre; **Archivo** en pesos 800 y 900 es la sustitución acordada.

```html
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;700;800;900&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
```

---

## CAMPO 5 · Any other notes?

**Pegar todo el bloque siguiente.** Es la parte que determina la calidad del resultado.

```
ORIGEN DE LA MARCA (verificado, no inventar variantes)

Extracción propia del 12 de agosto de 2026 sobre caravela.coffee y el logo oficial.

  #4E4E24  olivo     MUESTREADO por pixel del logo (25,7% de pixeles opacos)
  #D6BE5C  dorado    LITERAL en el marcado del sitio
  #E0B2BB  rosa      LITERAL en el marcado del sitio
  #DB8358  terracota LITERAL en el marcado del sitio

Tokens Tailwind reales expuestos en las clases del sitio, para nomenclatura:
bg-brown, text-main, bg-main, bg-main-light, bg-yellow, bg-yellow-light,
bg-green-20, bg-green-30, bg-pink, bg-orange.

Todo lo demás en el archivo de tokens es derivado y ajustable. Los cuatro de
arriba no se tocan.

REGLA CROMATICA PROPIA DE ESTOS ARTEFACTOS

El olivo y el dorado son de Caravela: se usan para lo que es de ellos (su
contexto, sus cifras de negocio, su identidad).
El terracota es el acento del autor: se usa para lo que aporta el documento
(datos propios, hallazgos, conclusiones).
Mantener esa separacion. Es una decision de significado, no de estetica.

LENGUAJE VISUAL DEL SITIO (replicar)

  · Secciones a pantalla completa, ritmo alterno oscuro-claro-blanco
  · Titulares en display, SIEMPRE en mayusculas, tracking negativo
  · Bloques de color contiguos sin separacion ni sombra
  · SIN esquinas redondeadas en bloques y tarjetas grandes: rectangulos puros.
    Solo redondean etiquetas pequenas y avatares
  · Marca de agua del isotipo rotada 28 grados, escala X invertida, opacidad 0.05
  · Entradas con translate-x desde -100% y fundidos de 1200ms
  · Sin sombras pesadas. Elevacion por borde y desplazamiento sutil

COMPONENTES A EXTRAER DEL HTML DE REFERENCIA

Ya construidos en la v2, extraerlos como componentes del sistema:
  · Tarjeta de KPI (cifra grande en display + etiqueta en versalitas + nota)
  · Tarjeta de evidencia (miniatura + fuente con icono + texto + metrica, clicable)
  · Tarjeta de riesgo (barra lateral de color por nivel)
  · Tarjeta de persona (avatar circular + nombre + cargo + angulo + estado)
  · Bloque de cita (fondo olivo profundo, comilla gigante al 14% de opacidad)
  · Fila de fase (numero grande desaturado + titulo + etiquetas)
  · Gantt simplificado por semanas
  · Barras horizontales comparativas animadas al entrar en viewport
  · Nota de fuente (11,5px, siempre bajo cada bloque de datos)

COMPONENTES NUEVOS QUE FALTAN

  · Diagrama de proceso BPM con dos carriles y bucle de retroalimentacion, en SVG
  · Tarjeta colapsable (details/summary) que se despliega sola al imprimir
  · Grafico de dona con total al centro
  · Grafico de proporcion con marcadores encendidos y apagados
  · Fila de logotipos de terceros en escala de grises al 65% de opacidad
  · Rejilla de credencial: icono + cifra + etiqueta de maximo 5 palabras

REQUISITO DE DOBLE FORMATO

Cada componente debe funcionar en pantalla y en papel. Reglas duras:
  · Ningun dato puede existir solo en estado interactivo. Lo colapsado se
    despliega en @media print
  · Graficos en SVG, nunca canvas
  · print-color-adjust: exact para que los fondos de seccion se impriman
  · break-inside: avoid en tarjetas, graficos y filas de fase
  · Las animaciones de entrada se neutralizan en impresion (opacity 1, sin
    transform), o el PDF sale en blanco
  · Objetivo: 8 a 10 paginas A4

TIPOGRAFIA

  Display: Archivo 800-900, mayusculas, letter-spacing -0.02em
  Cuerpo:  DM Sans 400-500
  Datos:   DM Mono 500 (distingue el dato del texto y refuerza la sensacion
           de instrumento de medicion, no de folleto)

REGLAS DE ESCRITURA DEL SISTEMA

  · PROHIBIDOS los guiones largos y medios en todo el contenido. Usar dos
    puntos y parentesis. Esta regla esta verificada a cero en la v2
  · Las cifras van con decimal y con tamano de muestra cuando aplica:
    "62,4 likes (n=12)", no "los carruseles rinden mejor"
  · Toda seccion de datos lleva nota de fuente con fecha y metodo
  · Ningun parrafo supera cuatro lineas en escritorio
  · Sin adjetivos de agencia: innovador, disruptivo, 360, holistico, sinergia

CRITERIO DE EXITO

El lector es un CEO que lee rapido, entre reuniones, y que ya contrato una
agencia que no funciono. El sistema debe producir documentos que en quince
segundos comuniquen que hubo una persona investigando, no una plantilla
rellenada. Densidad de dato alta, densidad de texto baja.
```

---

## CHECKLIST ANTES DE ENVIAR EL FORMULARIO

- [ ] La v2 y el CSS de tokens subidos a `agr-git/autonomia-propuesta`
- [ ] Campo 1 con el blurb pegado
- [ ] Campo 2 con la URL del repositorio
- [ ] Campo 3 vacío (no hay Figma)
- [ ] Los cinco archivos adjuntos en el campo 4
- [ ] Campo 5 con el bloque completo de notas

---

## QUÉ PEDIRLE A CLAUDE CODE DESPUÉS

Una vez creado el sistema, el primer encargo debería ser este:

> Reconstruye `caravela-growth-lead-propuesta-v2.html` como v3 aplicando el
> design system, siguiendo el documento `HANDOFF_Claude_Design_Caravela.md`.
> Prioridades: reducir de 4.200 a 2.400 palabras, convertir el modus operandi
> en diagrama BPM, los siete resultados clave en tres, los riesgos en tarjetas
> colapsables, y la línea base en cinco gráficos. Verificar contra el checklist
> de aceptación de la sección 10 de ese documento.

Los dos handoffs son complementarios: **este** define cómo se ve el sistema, el **otro** define qué dice el documento.
