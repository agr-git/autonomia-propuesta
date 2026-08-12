#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construye la propuesta v2 (landing con branding Caravela) inyectando assets base64."""
import json, io, os

A = json.load(open("assets_b64.json"))
FOTO, LOGO, CV = A["foto"], A["logo"], A["cv"]
P = json.load(open("pics_b64.json"))

HTML = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Growth &amp; Strategic Projects Lead · Propuesta para Caravela Coffee</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;700;800;900&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{
  --olive:#4E4E24; --olive-d:#3A3A1B; --olive-l:#6B6B33; --olive-xl:#8A8A55;
  --gold:#D6BE5C; --pink:#E0B2BB; --terra:#DB8358; --sage:#B7C4A0;
  --cream:#F7F4E9; --cream2:#EFE9D8; --white:#FFFDF7;
  --ink:#2A2A14; --txt:#3D3D28; --txt2:#78785F; --txt3:#A3A38C;
  --bdr:#DDD6C0; --bdr2:#C8C0A6;
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{background:var(--cream);color:var(--txt);font-family:'DM Sans',sans-serif;font-size:16px;line-height:1.65;-webkit-font-smoothing:antialiased;overflow-x:hidden;}
::selection{background:var(--gold);color:var(--olive-d);}

/* ---------- PROGRESO + NAV ---------- */
#prog{position:fixed;top:0;left:0;height:3px;background:var(--terra);width:0;z-index:300;transition:width .1s linear;}
.nav{position:fixed;top:0;left:0;right:0;height:64px;background:rgba(78,78,36,.97);backdrop-filter:blur(8px);z-index:200;display:flex;align-items:center;justify-content:space-between;padding:0 clamp(16px,4vw,48px);transform:translateY(-100%);transition:transform .45s cubic-bezier(.4,0,.2,1);}
.nav.show{transform:translateY(0);}
.nav-l{display:flex;align-items:center;gap:12px;}
.nav-l img{height:17px;filter:brightness(0) invert(1);opacity:.95;}
.nav-l span{font-family:'Archivo',sans-serif;font-size:11px;font-weight:700;color:var(--gold);letter-spacing:.12em;text-transform:uppercase;}
.nav-r{display:flex;gap:2px;}
.nav-r a{font-size:11px;font-weight:600;color:rgba(255,253,247,.72);text-decoration:none;padding:7px 12px;border-radius:3px;letter-spacing:.06em;text-transform:uppercase;transition:all .2s;white-space:nowrap;}
.nav-r a:hover,.nav-r a.act{color:var(--olive-d);background:var(--gold);}
@media(max-width:900px){.nav-r{display:none;}}

/* ---------- REVEAL ---------- */
.rv{opacity:0;transform:translateY(26px);transition:opacity 1s cubic-bezier(.2,.7,.3,1),transform 1s cubic-bezier(.2,.7,.3,1);}
.rv.in{opacity:1;transform:none;}
.rvx{opacity:0;transform:translateX(-52px);transition:opacity 1.1s cubic-bezier(.2,.7,.3,1),transform 1.1s cubic-bezier(.2,.7,.3,1);}
.rvx.in{opacity:1;transform:none;}
.d1{transition-delay:.09s}.d2{transition-delay:.18s}.d3{transition-delay:.27s}.d4{transition-delay:.36s}.d5{transition-delay:.45s}.d6{transition-delay:.54s}

/* ---------- LAYOUT ---------- */
section{padding:clamp(64px,9vw,120px) clamp(20px,5vw,64px);position:relative;}
.wrap{max-width:1120px;margin:0 auto;}
.eyebrow{font-family:'Archivo',sans-serif;font-size:11px;font-weight:800;letter-spacing:.22em;text-transform:uppercase;color:var(--terra);margin-bottom:14px;display:flex;align-items:center;gap:10px;}
.eyebrow::before{content:'';width:26px;height:2px;background:var(--terra);display:inline-block;}
h1{font-family:'Archivo',sans-serif;font-weight:900;font-size:clamp(34px,6.4vw,74px);line-height:.98;letter-spacing:-.025em;text-transform:uppercase;color:var(--cream);}
h2{font-family:'Archivo',sans-serif;font-weight:800;font-size:clamp(27px,4.1vw,46px);line-height:1.06;letter-spacing:-.02em;color:var(--olive-d);margin-bottom:18px;text-transform:uppercase;}
h3{font-family:'Archivo',sans-serif;font-weight:700;font-size:clamp(17px,2vw,21px);color:var(--olive-d);margin-bottom:11px;letter-spacing:-.01em;}
h4{font-family:'Archivo',sans-serif;font-weight:700;font-size:15px;color:var(--olive-d);margin-bottom:7px;}
.lead{font-size:clamp(16px,1.9vw,20px);color:var(--txt2);max-width:70ch;line-height:1.68;}
.sec-cream{background:var(--cream);}
.sec-white{background:var(--white);}
.sec-olive{background:var(--olive);color:var(--cream2);}
.sec-olive h2{color:var(--gold);} .sec-olive h3,.sec-olive h4{color:var(--cream);}
.sec-olive .lead{color:rgba(247,244,233,.76);}
.sec-olive .eyebrow{color:var(--gold);} .sec-olive .eyebrow::before{background:var(--gold);}

/* ---------- HERO ---------- */
.hero{min-height:100svh;background:var(--olive);display:flex;flex-direction:column;justify-content:center;padding:clamp(28px,6vw,64px);position:relative;overflow:hidden;}
.hero-wm{position:absolute;right:-14%;top:-8%;width:min(78vw,880px);opacity:.052;transform:rotate(28deg) scaleX(-1);pointer-events:none;}
.hero-inner{max-width:1120px;margin:0 auto;width:100%;position:relative;z-index:2;}
.hero-logo{height:clamp(24px,3vw,34px);filter:brightness(0) invert(1);opacity:.9;margin-bottom:clamp(28px,5vw,52px);}
.hero h1 span.g{color:var(--gold);} .hero h1 span.t{color:var(--terra);} .hero h1 span.p{color:var(--pink);}
.hero-sub{margin-top:clamp(22px,3vw,34px);font-size:clamp(15px,1.8vw,19px);color:rgba(247,244,233,.7);max-width:62ch;line-height:1.7;}
.hero-meta{margin-top:clamp(30px,4.5vw,52px);display:flex;gap:clamp(16px,4vw,44px);flex-wrap:wrap;padding-top:22px;border-top:1px solid rgba(214,190,92,.26);}
.hero-meta div span{display:block;}
.hero-meta .hm-l{font-size:9.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:5px;font-family:'Archivo',sans-serif;}
.hero-meta .hm-v{font-size:13.5px;color:var(--cream2);font-weight:500;}
.scroll-hint{position:absolute;bottom:26px;left:50%;transform:translateX(-50%);color:rgba(247,244,233,.4);font-size:10px;letter-spacing:.2em;text-transform:uppercase;display:flex;flex-direction:column;align-items:center;gap:7px;font-family:'Archivo',sans-serif;font-weight:600;}
.scroll-hint i{width:1px;height:26px;background:linear-gradient(var(--gold),transparent);animation:sd 2s ease-in-out infinite;}
@keyframes sd{0%,100%{opacity:.2;transform:scaleY(.5)}50%{opacity:1;transform:scaleY(1)}}

/* ---------- KPI ---------- */
.kpi-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1px;background:var(--bdr);border:1px solid var(--bdr);margin:34px 0;}
.kpi{background:var(--white);padding:22px 18px;}
.sec-olive .kpi-row{background:rgba(214,190,92,.2);border-color:rgba(214,190,92,.2);}
.sec-olive .kpi{background:var(--olive);}
.kpi .v{font-family:'Archivo',sans-serif;font-size:clamp(28px,3.6vw,40px);font-weight:800;color:var(--olive);line-height:1;letter-spacing:-.025em;}
.sec-olive .kpi .v{color:var(--gold);}
.kpi .v.t{color:var(--terra);} .kpi .v.gd{color:#A38A2E;}
.kpi .l{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--txt2);margin-top:9px;line-height:1.35;font-family:'Archivo',sans-serif;}
.sec-olive .kpi .l{color:rgba(247,244,233,.62);}
.kpi .s{font-size:11px;color:var(--txt3);margin-top:6px;}
.sec-olive .kpi .s{color:rgba(247,244,233,.4);}

/* ---------- CARDS ---------- */
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px;}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(228px,1fr));gap:16px;}
.card{background:var(--white);border:1px solid var(--bdr);padding:26px;transition:transform .3s,box-shadow .3s,border-color .3s;}
.card:hover{transform:translateY(-4px);box-shadow:0 14px 34px rgba(78,78,36,.09);border-color:var(--bdr2);}
.card p{font-size:14.5px;color:var(--txt2);line-height:1.7;}
.card.acc{border-left:3px solid var(--terra);}
.card.acc-g{border-left:3px solid var(--gold);}
.card.acc-p{border-left:3px solid var(--pink);}
.card.acc-s{border-left:3px solid var(--sage);}
.ico{width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:16px;}
.ico svg{width:21px;height:21px;stroke-width:1.8;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.i1{background:rgba(219,131,88,.15);} .i1 svg{stroke:var(--terra);}
.i2{background:rgba(214,190,92,.22);} .i2 svg{stroke:#9C8526;}
.i3{background:rgba(224,178,187,.24);} .i3 svg{stroke:#B5717E;}
.i4{background:rgba(183,196,160,.26);} .i4 svg{stroke:#6B7D4E;}

/* ---------- QUOTE ---------- */
.quote{background:var(--olive-d);color:var(--cream);padding:clamp(28px,4vw,44px);margin:32px 0;position:relative;overflow:hidden;}
.quote::before{content:'"';position:absolute;top:-24px;left:14px;font-family:'Archivo',serif;font-size:150px;color:rgba(214,190,92,.14);line-height:1;}
.quote p{font-family:'Archivo',sans-serif;font-size:clamp(18px,2.5vw,27px);font-weight:600;line-height:1.34;position:relative;z-index:2;letter-spacing:-.015em;}
.quote cite{display:block;margin-top:16px;font-size:12px;color:var(--gold);font-style:normal;letter-spacing:.1em;text-transform:uppercase;font-weight:700;font-family:'Archivo',sans-serif;}

/* ---------- DUAL AUDIENCIA ---------- */
.dual{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1px solid var(--bdr);margin-top:26px;}
.dual > div{padding:26px;}
.dual .a1{background:rgba(219,131,88,.07);border-right:1px solid var(--bdr);}
.dual .a2{background:rgba(214,190,92,.1);}
.dual h4{display:flex;align-items:center;gap:9px;margin-bottom:11px;text-transform:uppercase;letter-spacing:.08em;font-size:12px;}
.dot{width:8px;height:8px;border-radius:50%;display:inline-block;}
.dot.t{background:var(--terra);} .dot.g{background:#A38A2E;}
.dual p{font-size:14px;color:var(--txt2);line-height:1.68;}
@media(max-width:640px){.dual{grid-template-columns:1fr;}.dual .a1{border-right:none;border-bottom:1px solid var(--bdr);}}

/* ---------- PERFIL ---------- */
.perfil{display:grid;grid-template-columns:230px 1fr;gap:36px;align-items:start;}
@media(max-width:760px){.perfil{grid-template-columns:1fr;gap:24px;}}
.perfil-foto{width:100%;aspect-ratio:1;object-fit:cover;border:1px solid rgba(214,190,92,.3);}
.links{display:flex;gap:9px;flex-wrap:wrap;margin-top:20px;}
.lnk{display:inline-flex;align-items:center;gap:7px;padding:9px 15px;border:1px solid var(--gold);color:var(--gold);text-decoration:none;font-size:12px;font-weight:700;letter-spacing:.05em;transition:all .22s;font-family:'Archivo',sans-serif;text-transform:uppercase;}
.lnk:hover{background:var(--gold);color:var(--olive-d);}
.lnk svg{width:14px;height:14px;fill:currentColor;}
.lnk.solid{background:var(--terra);border-color:var(--terra);color:var(--white);}
.lnk.solid:hover{background:var(--gold);border-color:var(--gold);color:var(--olive-d);}

/* ---------- KR LIST ---------- */
.kr{display:flex;gap:16px;padding:17px 0;border-bottom:1px solid var(--bdr);align-items:flex-start;}
.sec-olive .kr{border-color:rgba(214,190,92,.2);}
.kr:last-child{border-bottom:none;}
.kr-n{font-family:'DM Mono',monospace;font-size:12px;font-weight:500;color:var(--terra);background:rgba(219,131,88,.13);padding:4px 9px;flex-shrink:0;letter-spacing:.04em;}
.sec-olive .kr-n{color:var(--gold);background:rgba(214,190,92,.16);}
.kr-b strong{display:block;font-size:14.5px;color:var(--olive-d);margin-bottom:4px;font-weight:600;}
.sec-olive .kr-b strong{color:var(--cream);}
.kr-b span{font-size:13px;color:var(--txt2);}
.sec-olive .kr-b span{color:rgba(247,244,233,.6);}

/* ---------- FASES ---------- */
.fase{display:grid;grid-template-columns:76px 1fr;gap:20px;padding:24px 0;border-top:1px solid var(--bdr);}
.fase-n{font-family:'Archivo',sans-serif;font-size:34px;font-weight:800;color:var(--bdr2);line-height:.9;letter-spacing:-.04em;}
.fase-b p{font-size:14px;color:var(--txt2);line-height:1.7;margin-top:7px;}
.pill{display:inline-block;padding:3px 11px;font-size:10.5px;font-weight:700;margin:9px 6px 0 0;letter-spacing:.06em;text-transform:uppercase;font-family:'Archivo',sans-serif;}
.p-t{background:rgba(219,131,88,.14);color:#B5642F;}
.p-g{background:rgba(214,190,92,.24);color:#8A7420;}
.p-s{background:rgba(183,196,160,.3);color:#5C6E42;}
.p-n{background:var(--cream2);color:var(--txt2);}
@media(max-width:640px){.fase{grid-template-columns:1fr;gap:6px;}}

/* ---------- EVIDENCIA ---------- */
.ev{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:12px;margin-top:20px;}
.ev a{display:block;background:var(--white);border:1px solid var(--bdr);padding:16px;text-decoration:none;transition:all .25s;}
.ev a:hover{border-color:var(--terra);transform:translateY(-3px);box-shadow:0 10px 24px rgba(78,78,36,.08);}
.ev .src{display:flex;align-items:center;gap:6px;font-size:9.5px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--txt3);margin-bottom:9px;font-family:'Archivo',sans-serif;}
.ev .src svg{width:12px;height:12px;fill:currentColor;}
.ev .txt{font-size:13px;color:var(--txt);line-height:1.5;margin-bottom:10px;font-weight:500;}
.ev .m{font-family:'DM Mono',monospace;font-size:11.5px;color:var(--terra);font-weight:500;}
.ev .m b{color:var(--olive-d);}

/* comparativa duplicados */
.dupe{display:grid;grid-template-columns:1fr 34px 1fr;gap:0;align-items:stretch;border:1px solid var(--bdr);margin-top:14px;background:var(--white);}
.dupe > a{padding:16px 18px;text-decoration:none;transition:background .22s;}
.dupe > a:hover{background:var(--cream2);}
.dupe .mid{display:flex;align-items:center;justify-content:center;background:var(--cream2);font-family:'Archivo',sans-serif;font-size:11px;font-weight:800;color:var(--txt3);border-left:1px solid var(--bdr);border-right:1px solid var(--bdr);}
@media(max-width:640px){.dupe{grid-template-columns:1fr;}.dupe .mid{padding:5px;border:none;border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);}}


/* ---------- VOCES ---------- */
.voces{display:grid;grid-template-columns:repeat(auto-fit,minmax(252px,1fr));gap:12px;margin-top:20px;}
.voz{background:var(--white);border:1px solid var(--bdr);padding:20px;display:flex;gap:14px;align-items:flex-start;transition:transform .28s,box-shadow .28s,border-color .28s;text-decoration:none;}
.voz:hover{transform:translateY(-4px);box-shadow:0 12px 28px rgba(78,78,36,.1);border-color:var(--bdr2);}
.voz img{width:52px;height:52px;border-radius:50%;object-fit:cover;flex-shrink:0;border:2px solid var(--cream2);}
.voz.on img{border-color:var(--terra);}
.voz-n{font-family:'Archivo',sans-serif;font-size:14px;font-weight:700;color:var(--olive-d);line-height:1.2;}
.voz-c{font-size:11px;color:var(--txt2);margin-top:3px;line-height:1.4;}
.voz-a{font-size:12px;color:var(--txt);margin-top:9px;line-height:1.5;}
.voz-t{display:inline-block;margin-top:9px;padding:2px 8px;font-size:9px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;font-family:'Archivo',sans-serif;}
.vt-on{background:rgba(219,131,88,.15);color:#B5642F;}
.vt-off{background:var(--cream2);color:var(--txt2);}

/* ---------- BARRAS ---------- */
.bars{margin-top:22px;}
.bar-row{display:grid;grid-template-columns:112px 1fr 66px;gap:14px;align-items:center;margin-bottom:11px;}
.bar-lbl{font-size:12px;color:var(--txt2);font-weight:600;text-align:right;}
.bar-tr{height:24px;background:var(--cream2);position:relative;overflow:hidden;}
.bar-fl{height:100%;width:0;transition:width 1.5s cubic-bezier(.2,.8,.3,1);}
.bar-val{font-family:'DM Mono',monospace;font-size:13px;color:var(--olive-d);font-weight:500;}

/* ---------- TIMELINE ---------- */
.gantt{margin-top:26px;overflow-x:auto;}
.gantt-in{min-width:640px;}
.g-head{display:grid;grid-template-columns:120px repeat(17,1fr);gap:2px;margin-bottom:7px;}
.g-head span{font-size:9px;color:var(--txt3);text-align:center;font-family:'DM Mono',monospace;}
.g-row{display:grid;grid-template-columns:120px repeat(17,1fr);gap:2px;margin-bottom:5px;align-items:center;}
.g-row > b{font-size:11px;color:var(--txt2);font-weight:600;padding-right:8px;text-align:right;}
.g-c{height:20px;background:var(--cream2);}
.g-c.on{background:var(--terra);} .g-c.g{background:var(--gold);} .g-c.s{background:var(--sage);}

/* ---------- RIESGOS ---------- */
.risk{border-left:3px solid;padding:20px 22px;background:var(--white);margin-bottom:12px;}
.risk.hi{border-color:#C2543A;} .risk.md{border-color:var(--gold);} .risk.lo{border-color:var(--sage);}
.risk .lv{font-size:9.5px;font-weight:800;letter-spacing:.13em;text-transform:uppercase;margin-bottom:9px;font-family:'Archivo',sans-serif;}
.risk.hi .lv{color:#C2543A;} .risk.md .lv{color:#8A7420;} .risk.lo .lv{color:#5C6E42;}
.risk p{font-size:13.5px;color:var(--txt2);line-height:1.65;margin-bottom:11px;}
.risk .mit{font-size:12.5px;color:#5C6E42;font-weight:500;padding-top:11px;border-top:1px solid var(--bdr);}

/* ---------- PREGUNTAS ---------- */
.q{display:flex;gap:18px;padding:19px 0;border-bottom:1px solid rgba(214,190,92,.18);align-items:flex-start;}
.q:last-child{border-bottom:none;}
.q-n{font-family:'DM Mono',monospace;font-size:13px;color:var(--gold);flex-shrink:0;padding-top:2px;font-weight:500;}
.q-t{font-size:15px;color:var(--cream);font-weight:500;margin-bottom:5px;line-height:1.45;}
.q-w{font-size:13px;color:rgba(247,244,233,.56);line-height:1.6;}
.q-w b{color:var(--gold);font-weight:600;}

/* ---------- PASOS ---------- */
.paso{display:grid;grid-template-columns:58px 1fr;gap:20px;padding:26px 0;border-top:1px solid var(--bdr);}
.paso-n{font-family:'Archivo',sans-serif;font-size:30px;font-weight:800;color:var(--terra);line-height:.9;}
.paso p{font-size:14.5px;color:var(--txt2);line-height:1.7;margin-top:7px;}

/* ---------- FOOTER ---------- */
footer{background:var(--olive-d);color:rgba(247,244,233,.5);padding:34px clamp(20px,5vw,64px);font-size:11.5px;display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;align-items:center;}
footer img{height:15px;filter:brightness(0) invert(1);opacity:.4;}
.note{font-size:11.5px;color:var(--txt3);margin-top:14px;line-height:1.6;}
.sec-olive .note{color:rgba(247,244,233,.42);}
a.inl{color:var(--terra);text-decoration:none;border-bottom:1px solid rgba(219,131,88,.35);}
a.inl:hover{border-color:var(--terra);}
.sec-olive a.inl{color:var(--gold);border-color:rgba(214,190,92,.35);}
ul.bl{list-style:none;margin-top:12px;}
ul.bl li{position:relative;padding-left:19px;font-size:14px;color:var(--txt2);margin-bottom:9px;line-height:1.62;}
ul.bl li::before{content:'';position:absolute;left:0;top:9px;width:6px;height:6px;background:var(--terra);}
.sec-olive ul.bl li{color:rgba(247,244,233,.72);}
.sec-olive ul.bl li::before{background:var(--gold);}
</style>
</head>
<body>

<div id="prog"></div>

<nav class="nav" id="nav">
  <div class="nav-l"><img src="data:image/png;base64,__LOGO__" alt="Caravela"><span>Propuesta 2026</span></div>
  <div class="nav-r">
    <a href="#reto">El Reto</a><a href="#rol">El Rol</a><a href="#mision">La Misión</a>
    <a href="#inception">Diagnóstico</a><a href="#insumos">Insumos</a><a href="#pasos">Siguiente</a>
  </div>
</nav>

<!-- ============ HERO ============ -->
<header class="hero">
  <img class="hero-wm" src="data:image/png;base64,__LOGO__" alt="">
  <div class="hero-inner">
    <img class="hero-logo rv in" src="data:image/png;base64,__LOGO__" alt="Caravela Coffee">
    <div class="eyebrow rvx in d1" style="color:var(--gold);">Propuesta de rol y primera misión</div>
    <h1 class="rvx in d2">Growth &amp;<br><span class="g">Strategic</span> <span class="t">Projects</span><br>Lead</h1>
    <p class="hero-sub rv in d4">Caravela tiene las mejores historias del café de especialidad latinoamericano: están en 800 productores, en 40 laboratorios de calidad y en 25 años de relaciones. Hoy viven en la intranet. Esta propuesta es el sistema que las convierte en crecimiento medible (para el productor y para el tostador).</p>
    <div class="hero-meta rv in d5">
      <div><span class="hm-l">Para</span><span class="hm-v">Alejandro Cadena, CEO</span></div>
      <div><span class="hm-l">De</span><span class="hm-v">Alejandro Gil Rivera</span></div>
      <div><span class="hm-l">Misión 1</span><span class="hm-v">100 a 120 días</span></div>
      <div><span class="hm-l">Incluye</span><span class="hm-v">Inception Report v0</span></div>
    </div>
  </div>
  <div class="scroll-hint"><span>Recorrer</span><i></i></div>
</header>

<!-- ============ 1. EL RETO ============ -->
<section id="reto" class="sec-cream">
 <div class="wrap">
  <div class="eyebrow rv">01 · El Reto</div>
  <h2 class="rv d1">El activo más valioso<br>no se está comunicando</h2>
  <p class="lead rv d2">Caravela construyó en 25 años lo que ningún competidor puede copiar: relaciones reales con cientos de productores, un cuerpo técnico en origen y datos operativos de toda la cadena. Ese activo vive hoy en la intranet y en el campo, no en los canales donde el tostador decide a quién comprarle.</p>

  <div class="kpi-row rv d3">
    <div class="kpi"><div class="v">800+</div><div class="l">Productores este año</div><div class="s">Historias sin contar</div></div>
    <div class="kpi"><div class="v gd">25</div><div class="l">Quality Lab Managers en Colombia</div><div class="s">Cerca de 15 en otros orígenes</div></div>
    <div class="kpi"><div class="v t">95%</div><div class="l">Productores en Huila y Tolima</div><div class="s">5% en Nariño</div></div>
    <div class="kpi"><div class="v">83+</div><div class="l">Puntos de taza objetivo</div><div class="s">En alto porcentaje de compras</div></div>
  </div>
  <p class="note rv">Fuentes: conversación directa entre Alejandro Cadena (CEO de Caravela Coffee) y Alejandro Gil Rivera, agosto de 2026. Los indicadores digitales de este documento provienen de extracción propia sobre los canales públicos de Caravela (ver sección 04).</p>

  <div class="grid2" style="margin-top:34px;">
    <div class="card acc rv d1">
      <h3>El problema, en lenguaje de negocio</h3>
      <p>La comunicación llega hoy principalmente a un rol (el productor) pero el cliente final es el tostador. No existe un puente medible entre lo que se publica y dos cosas que sí importan: la lealtad de los tostadores actuales (lifetime value) y la generación de nuevos clientes (pipeline). El mejor argumento comercial de la compañía no está trabajando para el negocio.</p>
    </div>
    <div class="card acc-g rv d2">
      <h3>Y la evidencia externa lo confirma</h3>
      <p>El diagnóstico incluido en esta propuesta (sección 04) encontró que el 80% de las publicaciones se duplican palabra por palabra entre canales, que a LinkedIn (donde lee el productor) se le habla 100% en inglés, y que la conversación es casi nula: 0,7 comentarios por publicación. No es un problema de volumen: es de estrategia, segmentación y medición.</p>
    </div>
  </div>

  <div class="quote rv">
    <p>Siempre hay que buscar beneficiar a las dos audiencias.</p>
    <cite>Alejandro Cadena · CEO de Caravela Coffee</cite>
  </div>
  <p class="lead rv" style="font-size:16px;">Ese principio gobierna cada decisión de esta propuesta. No significa que cada pieza hable a los dos por igual: significa que ninguna pieza puede beneficiar a uno a costa del otro.</p>

  <div class="dual rv d1">
    <div class="a1"><h4><i class="dot t"></i>Productor</h4><p>Cada pieza dignifica, da visibilidad o transfiere conocimiento al productor. Nunca es materia prima narrativa: es co-protagonista con nombre propio y con algo que ganar.</p></div>
    <div class="a2"><h4><i class="dot g"></i>Tostador</h4><p>Cada pieza reduce la incertidumbre de compra: calidad consistente, trazabilidad verificable e historias que el tostador puede llevar a su propio consumidor final.</p></div>
  </div>

  <div class="card rv d2" style="margin-top:26px;">
    <h3>Por qué ahora</h3>
    <p>Caravela quiere vender café de nuevas formas (por región, por productor, por perfil, por historia) y quiere que sus tiendas y espacios comerciales jueguen un papel activo. Ese roadmap necesita la capa de contenido y medición construida antes de escalar, no después. Los datos ya existen, las historias ya existen y (según el diagnóstico) ese contenido ya es el que mejor rinde cuando aparece.</p>
  </div>
 </div>
</section>

<!-- ============ 2. EL ROL ============ -->
<section id="rol" class="sec-olive">
 <div class="wrap">
  <div class="eyebrow rv">02 · El Rol</div>
  <h2 class="rv d1">Growth &amp; Strategic<br>Projects Lead</h2>
  <p class="lead rv d2">Un rol que opera por misiones: el CEO confía un reto con objetivos y resultados clave medibles, y el rol lo ejecuta pensando y haciendo, construyendo el equipo que cada misión necesite. Ni consultor que recomienda y se va, ni empleado de funciones fijas.</p>

  <div class="perfil rv d3" style="margin-top:44px;">
    <div>
      <img class="perfil-foto" src="data:image/jpeg;base64,__FOTO__" alt="Alejandro Gil Rivera">
      <div class="links">
        <a class="lnk" href="https://www.linkedin.com/in/alejandrogilrivera" target="_blank" rel="noopener"><svg viewBox="0 0 24 24"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.55V9h3.57v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.72v20.56C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.72V1.72C24 .77 23.2 0 22.22 0z"/></svg>LinkedIn</a>
        <a class="lnk" href="https://github.com/agr-git" target="_blank" rel="noopener"><svg viewBox="0 0 24 24"><path d="M12 .3a12 12 0 0 0-3.8 23.4c.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.6-1.4-1.4-1.8-1.4-1.8-1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.7-1.6-2.7-.3-5.5-1.3-5.5-6 0-1.2.5-2.3 1.3-3.1-.2-.4-.6-1.6.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0C17.3 4.9 18.3 5.2 18.3 5.2c.7 1.6.3 2.8.1 3.2.8.8 1.3 1.9 1.3 3.1 0 4.7-2.8 5.7-5.5 6 .4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 12 .3"/></svg>GitHub</a>
        <a class="lnk solid" href="data:application/pdf;base64,__CV__" download="CV_Alejandro_Gil_Rivera.pdf"><svg viewBox="0 0 24 24"><path d="M12 16l-6-6h4V2h4v8h4l-6 6zm-8 2h16v2H4v-2z"/></svg>Ver CV</a>
      </div>
    </div>
    <div>
      <h3>Objetivo del rol</h3>
      <p style="color:rgba(247,244,233,.76);font-size:15px;line-height:1.72;">Convertir los activos estratégicos de Caravela (datos, relaciones, calidad, presencia en origen) en crecimiento medible sobre cuatro indicadores concretos:</p>
      <div style="margin-top:20px;">
        <div class="kr"><span class="kr-n">M1</span><div class="kr-b"><strong>Lifetime value de los tostadores actuales</strong><span>Medido por permanencia, recompra y profundidad de relación comercial.</span></div></div>
        <div class="kr"><span class="kr-n">M2</span><div class="kr-b"><strong>Leads calificados originados en contenido</strong><span>Volumen y calidad de oportunidades atribuibles al funnel de comunicación.</span></div></div>
        <div class="kr"><span class="kr-n">M3</span><div class="kr-b"><strong>Conversión de lead a conversación comercial</strong><span>Tasa y tiempo entre el primer contacto y la conversación de negocio.</span></div></div>
        <div class="kr"><span class="kr-n">M4</span><div class="kr-b"><strong>Beneficio verificable para el productor</strong><span>Visibilidad, conocimiento transferido y participación: la segunda audiencia también se mide.</span></div></div>
      </div>
      <p class="note">Estos son los indicadores del rol en el tiempo. Los resultados clave específicos de la primera misión están en la sección 03.</p>
    </div>
  </div>

  <h3 class="rv" style="margin-top:52px;">Modus operandi</h3>
  <div class="grid3 rv d1" style="margin-top:18px;">
    <div class="card acc" style="background:rgba(247,244,233,.05);border-color:rgba(214,190,92,.22);">
      <div class="ico i1"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="1" fill="currentColor" stroke="none"/></svg></div>
      <h4 style="color:var(--cream);">Misiones, no funciones</h4>
      <p style="color:rgba(247,244,233,.66);">Cada misión tiene duración definida, resultados clave medibles y un cierre formal con decisión: escalar, iterar o terminar. Se compran resultados verificables, no horas.</p>
    </div>
    <div class="card acc-g" style="background:rgba(247,244,233,.05);border-color:rgba(214,190,92,.22);">
      <div class="ico i2"><svg viewBox="0 0 24 24"><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M5.6 18.4l2.1-2.1M16.3 7.7l2.1-2.1"/><circle cx="12" cy="12" r="3.4"/></svg></div>
      <h4 style="color:var(--cream);">Pensar y hacer</h4>
      <p style="color:rgba(247,244,233,.66);">El rol diseña la estrategia y la ejecuta: extracción y análisis de datos, arquitectura editorial, dirección del equipo creativo, instrumentación del funnel. La primera prueba es este documento, que llega con el diagnóstico ya hecho.</p>
    </div>
    <div class="card acc-p" style="background:rgba(247,244,233,.05);border-color:rgba(214,190,92,.22);">
      <div class="ico i3"><svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.2"/><path d="M2.5 20c0-3.6 2.9-6.2 6.5-6.2s6.5 2.6 6.5 6.2"/><circle cx="17.5" cy="9.5" r="2.4"/><path d="M17.5 14c2.6 0 4 1.9 4 4.4"/></svg></div>
      <h4 style="color:var(--cream);">Equipo por misión</h4>
      <p style="color:rgba(247,244,233,.66);">El rol arma el equipo mínimo que cada misión requiera (producción audiovisual, edición) e integra a las áreas existentes: Customer Experience, el nuevo Product Developer y los equipos de origen. Multiplicador, no estructura paralela.</p>
    </div>
    <div class="card acc-s" style="background:rgba(247,244,233,.05);border-color:rgba(214,190,92,.22);">
      <div class="ico i4"><svg viewBox="0 0 24 24"><path d="M3 20h18"/><rect x="4.5" y="12" width="3.4" height="8"/><rect x="10.3" y="7.5" width="3.4" height="12.5"/><rect x="16.1" y="3.5" width="3.4" height="16.5"/></svg></div>
      <h4 style="color:var(--cream);">Autonomía con visibilidad</h4>
      <p style="color:rgba(247,244,233,.66);">Tablero de resultados clave siempre disponible para el CEO, sin necesidad de pedir reportes. La autonomía se sostiene con transparencia total en la medición, no con confianza ciega.</p>
    </div>
  </div>

  <h3 class="rv" style="margin-top:52px;">Por qué este perfil</h3>
  <div class="grid2 rv d1" style="margin-top:18px;">
    <div class="card" style="background:rgba(247,244,233,.05);border-color:rgba(214,190,92,.22);">
      <h4 style="color:var(--gold);">Conoce las dos audiencias por dentro</h4>
      <p style="color:rgba(247,244,233,.66);">12 años de proyectos entre datos, sostenibilidad y cadena agrícola: sistemas de información cafetera con IDH y Conservation International, proyectos de cooperación con GIZ, Starbucks e Ishimitsu dentro del grupo NKG. Y administra directamente una finca de café de especialidad de 15 hectáreas en el Eje Cafetero (84 a 85 puntos, venta local y a un cliente en Alemania): la perspectiva del productor no es teórica.</p>
    </div>
    <div class="card" style="background:rgba(247,244,233,.05);border-color:rgba(214,190,92,.22);">
      <h4 style="color:var(--gold);">Ya construyó este sistema, para sí mismo</h4>
      <p style="color:rgba(247,244,233,.66);">Opera un motor propio de contenido en Python (extracción vía Apify, normalización, cálculo de métricas semanales y tablero de resultados) desplegado en servidor propio con rutina automática. El diagnóstico de la sección 04 se produjo con ese mismo instrumental en menos de 24 horas. Multiplicador B certificado, alineado con el marco B Corp que Caravela usa como referencia de mejora.</p>
    </div>
  </div>
 </div>
</section>

<!-- ============ 3. MISIÓN ============ -->
<section id="mision" class="sec-white">
 <div class="wrap">
  <div class="eyebrow rv">03 · Misión 1</div>
  <h2 class="rv d1">De la intranet<br>al tostador</h2>
  <p class="lead rv d2">Construir y probar el sistema que convierte datos y relaciones en contenido que fideliza tostadores y genera nuevas oportunidades, con medición de punta a punta. Duración: 100 a 120 días.</p>

  <div class="card acc rv d3" style="margin-top:30px;">
    <h3>Una misión, varias iteraciones</h3>
    <p>Esto no es una campaña que se lanza y se evalúa al final. La misión está diseñada como ciclos quincenales de publicación, medición y ajuste, porque en comunicación lo que funciona hoy deja de funcionar: las plataformas cambian los formatos que privilegian, las audiencias se saturan y los ángulos se agotan. Lo que la misión entrega al cierre no es un calendario de contenidos, es <b>un sistema de iteración que sabe leerse a sí mismo</b>, junto con la evidencia de qué funcionó, para qué audiencia y por cuánto tiempo. Eso es lo que permite decidir con datos si se escala a un horizonte más largo.</p>
  </div>

  <h3 class="rv" style="margin-top:44px;">Resultados clave</h3>
  <div class="rv d1" style="margin-top:14px;">
    <div class="kr"><span class="kr-n">KR 1</span><div class="kr-b"><strong>Diagnóstico completo y línea base validada</strong><span>Extensión del diagnóstico externo más inmersión interna (intranet, métricas de administrador, CRM). Semana 3.</span></div></div>
    <div class="kr"><span class="kr-n">KR 2</span><div class="kr-b"><strong>Análisis de audiencia real por canal</strong><span>Extracción detallada de quién reacciona y comenta en LinkedIn e Instagram: perfil, cargo, país y tipo de organización, para saber si quien escucha es productor, tostador o industria. Este es el dato que hoy nadie tiene y sin el cual toda segmentación es una suposición. Semana 4.</span></div></div>
    <div class="kr"><span class="kr-n">KR 3</span><div class="kr-b"><strong>Arquitectura editorial de las 4 líneas</strong><span>Región, productor, perfil e historia, con banco inicial de 20 o más historias extraídas de datos reales y adaptación por canal y por audiencia. Semana 6.</span></div></div>
    <div class="kr"><span class="kr-n">KR 4</span><div class="kr-b"><strong>Iteraciones publicadas y medidas</strong><span>Al menos 4 ciclos quincenales en 2 o más canales, incluido un piloto en tiendas y espacios comerciales, cada uno ajustado con los datos del anterior. Semanas 6 a 14.</span></div></div>
    <div class="kr"><span class="kr-n">KR 5</span><div class="kr-b"><strong>Funnel instrumentado y visible</strong><span>Leads atribuibles a contenido en un tablero que el CEO consulta por su cuenta. Semana 10.</span></div></div>
    <div class="kr"><span class="kr-n">KR 6</span><div class="kr-b"><strong>N conversaciones comerciales nuevas originadas en contenido</strong><span>El valor de N se fija con el CEO en la sesión de kickoff, anclado al plan comercial real del año.</span></div></div>
    <div class="kr"><span class="kr-n">KR 7</span><div class="kr-b"><strong>Beneficio medido para el productor</strong><span>Número de productores con historia publicada, alcance obtenido y (donde aplique) conocimiento técnico transferido. La segunda audiencia también rinde cuentas.</span></div></div>
  </div>
  <p class="note rv">Nota de honestidad métrica: el ciclo de venta de café verde es largo. En 120 días se miden con rigor los leads y las conversaciones abiertas; los cierres se atribuyen en la ventana que dicte el ciclo real de la compañía, no en la de la misión.</p>

  <h3 class="rv" style="margin-top:48px;">Fases</h3>
  <div class="rv d1">
    <div class="fase"><div class="fase-n">00</div><div class="fase-b"><h4>Inception</h4><p>Este documento: diagnóstico externo v0, marco de rol y misión, preguntas de insumo. Cierra con la sesión de kickoff.</p><span class="pill p-s">Entregado con la propuesta</span></div></div>
    <div class="fase"><div class="fase-n">01</div><div class="fase-b"><h4>Diagnóstico profundo</h4><p>Extracción detallada de audiencias por canal, benchmark de competidores directos, mapeo de voces personales del equipo e inmersión interna en intranet, métricas de administrador y CRM. Conversaciones con Customer Experience, Product Developer y equipos de origen.</p><span class="pill p-t">Semanas 1 a 4</span><span class="pill p-n">Extracción y análisis</span></div></div>
    <div class="fase"><div class="fase-n">02</div><div class="fase-b"><h4>Estrategia editorial y arquitectura de medición</h4><p>Diseño de las 4 líneas con la regla de doble audiencia aplicada pieza por pieza, banco de historias desde datos reales, definición del tablero del CEO y armado del equipo creativo de apoyo.</p><span class="pill p-g">Semanas 4 a 6</span><span class="pill p-n">Diseño</span></div></div>
    <div class="fase"><div class="fase-n">03</div><div class="fase-b"><h4>Iteración</h4><p>Ciclos quincenales de publicación en canales priorizados más piloto en tiendas. Cada ciclo se ajusta con los datos del anterior: formato, idioma, ángulo y audiencia. El funnel se instrumenta en paralelo y las conversaciones comerciales se registran desde el primer ciclo.</p><span class="pill p-t">Semanas 6 a 14</span><span class="pill p-n">4 ciclos</span></div></div>
    <div class="fase"><div class="fase-n">04</div><div class="fase-b"><h4>Medición, cierre y decisión</h4><p>Reporte contra los 7 resultados clave, curva de rendimiento por línea editorial y por audiencia, aprendizajes sobre qué se agotó y qué escaló, y propuesta de Misión 2. Decisión conjunta: escalar, iterar o cerrar.</p><span class="pill p-s">Semanas 14 a 17</span></div></div>
  </div>

  <div class="gantt rv"><div class="gantt-in">
    <div class="g-head"><span></span><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span><span>10</span><span>11</span><span>12</span><span>13</span><span>14</span><span>15</span><span>16</span><span>17</span></div>
    <div class="g-row"><b>01 Diagnóstico</b><i class="g-c on"></i><i class="g-c on"></i><i class="g-c on"></i><i class="g-c on"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i></div>
    <div class="g-row"><b>02 Estrategia</b><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c g"></i><i class="g-c g"></i><i class="g-c g"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i></div>
    <div class="g-row"><b>03 Iteración</b><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c on"></i><i class="g-c on"></i><i class="g-c on"></i><i class="g-c on"></i><i class="g-c on"></i><i class="g-c on"></i><i class="g-c on"></i><i class="g-c on"></i><i class="g-c on"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i></div>
    <div class="g-row"><b>04 Cierre</b><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c"></i><i class="g-c s"></i><i class="g-c s"></i><i class="g-c s"></i><i class="g-c s"></i></div>
  </div></div>

  <h3 class="rv" style="margin-top:48px;">Riesgos y mitigación</h3>
  <div class="rv d1" style="margin-top:16px;">
    <div class="risk hi"><div class="lv">Alto · Datos</div><h4>El acceso a datos internos llega tarde</h4><p>Las historias con más potencial viven en la intranet. Si el acceso se demora, la fase 02 arranca con material incompleto y el banco de historias se construye sobre supuestos.</p><div class="mit">Mitigación: candado explícito en el kickoff (qué datos, quién los habilita, en qué fecha). La fase 01 tiene ruta alterna con datos externos y entrevistas mientras se abre el acceso.</div></div>
    <div class="risk md"><div class="lv">Medio · Organización</div><h4>Fricción con quien comunica hoy</h4><p>Si el rol se percibe como reemplazo de las personas o proveedores que hoy publican, se fabrica resistencia interna desde el día uno.</p><div class="mit">Mitigación: el rol se posiciona como capa de estrategia y medición que potencia a quien ejecuta. La fase 01 incluye el mapeo explícito de quién hace qué hoy, y el diseño respeta lo que ya funciona.</div></div>
    <div class="risk md"><div class="lv">Medio · Medición</div><h4>Atribución en un ciclo de venta largo</h4><p>El café verde no se vende con un clic. Prometer cierres atribuidos en 120 días sería prometer de más.</p><div class="mit">Mitigación: los resultados clave separan lo medible en la ventana (leads, conversaciones abiertas, participación de clientes actuales) de lo medible en el ciclo real (cierres).</div></div>
    <div class="risk md"><div class="lv">Medio · Contenido</div><h4>La fórmula que funciona se agota</h4><p>Los formatos que hoy rinden (por ejemplo los carruseles de lanzamiento) pierden efectividad cuando se repiten, y las plataformas cambian lo que privilegian.</p><div class="mit">Mitigación: el diseño por iteraciones es precisamente la respuesta. Cada ciclo mide rendimiento por formato y ángulo, y el sistema queda instalado para que Caravela siga ajustando después de la misión.</div></div>
    <div class="risk lo"><div class="lv">Bajo · Antecedente</div><h4>Que termine como la agencia anterior</h4><p>Caravela ya intentó tercerizar community management y no funcionó.</p><div class="mit">Mitigación: diferencia estructural (ejecución sin estrategia ni conocimiento de la cadena, frente a un rol con misiones, resultados clave y criterio de café). Además, en el kickoff se documenta qué falló exactamente para no repetirlo: es la pregunta 02 de la sección 05.</div></div>
  </div>
 </div>
</section>

<!-- ============ 4. INCEPTION ============ -->
<section id="inception" class="sec-cream">
 <div class="wrap">
  <div class="eyebrow rv">04 · Inception Report v0</div>
  <h2 class="rv d1">Lo que ya dicen<br>los datos</h2>
  <p class="lead rv d2">Primer entregable de la misión, ejecutado antes de firmar nada. Diagnóstico de los activos digitales públicos de Caravela extraído el 12 de agosto de 2026 mediante pipelines propios de scraping y análisis. Es la fotografía desde afuera: la misma que ve un tostador que evalúa a Caravela por primera vez.</p>

  <h3 class="rv" style="margin-top:40px;">Línea base por canal</h3>
  <div class="kpi-row rv d1" style="grid-template-columns:repeat(auto-fit,minmax(126px,1fr));">
    <div class="kpi"><div class="v">50.728</div><div class="l">Audiencia total</div><div class="s">Suma de ambos canales</div></div>
    <div class="kpi"><div class="v gd">23.466</div><div class="l">LinkedIn</div><div class="s">46,3% del total</div></div>
    <div class="kpi"><div class="v t">27.262</div><div class="l">Instagram</div><div class="s">53,7% del total</div></div>
    <div class="kpi"><div class="v">2,3</div><div class="l">Publicaciones semana</div><div class="s">LinkedIn, jun 12 a ago 12</div></div>
    <div class="kpi"><div class="v">24,4</div><div class="l">Reacciones por post</div><div class="s">LinkedIn, 0,10% de su base</div></div>
    <div class="kpi"><div class="v">47,9</div><div class="l">Likes por post</div><div class="s">Instagram, 0,18% de su base</div></div>
    <div class="kpi"><div class="v t">0,7</div><div class="l">Comentarios por post</div><div class="s">LinkedIn, 14 en 20 posts</div></div>
    <div class="kpi"><div class="v">3.389</div><div class="l">Publicaciones históricas</div><div class="s">Instagram, cuenta business</div></div>
  </div>
  <p class="note rv">Fuentes de extracción propia, 12 de agosto de 2026: <a class="inl" href="https://www.linkedin.com/company/caravela-coffee/posts/" target="_blank" rel="noopener">página de LinkedIn de Caravela</a> (20 publicaciones más recientes) e <a class="inl" href="https://www.instagram.com/caravelacoffee/" target="_blank" rel="noopener">Instagram @caravelacoffee</a> (perfil y 24 publicaciones). Son métricas públicas: no incluyen impresiones ni datos de administrador, que se incorporan en la fase 01.</p>

  <!-- H1 -->
  <h3 class="rv" style="margin-top:52px;">Hallazgo 01 · Un solo mensaje duplicado para dos audiencias</h3>
  <div class="card acc rv d1"><p><b>16 de las 20 publicaciones de LinkedIn (80%) tienen texto idéntico a su gemela de Instagram.</b> Hoy no existe una estrategia de dos audiencias: existe una sola voz clonada entre canales. El principio que rige la casa (beneficiar siempre a las dos audiencias) no puede cumplirse con el mismo texto para ambas, porque el productor y el tostador no necesitan lo mismo de una misma historia.</p></div>
  <div class="dupe rv d2">
    <a href="https://www.linkedin.com/posts/caravela-coffee_traceability-is-no-longer-a-back-office-requirement-activity-7483067975076511744-bKOH" target="_blank" rel="noopener"><div class="src"><svg viewBox="0 0 24 24"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.55V9h3.57v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.72v20.56C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.72V1.72C24 .77 23.2 0 22.22 0z"/></svg>LinkedIn · 15 jul</div><div class="txt">"Traceability is no longer a back-office requirement..."</div><div class="m"><b>38</b> reacciones · <b>0</b> comentarios</div></a>
    <div class="mid">=</div>
    <a href="https://www.instagram.com/p/Daw57NOjGty/" target="_blank" rel="noopener"><div class="src"><svg viewBox="0 0 24 24"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23a3.8 3.8 0 0 1-.9 1.38c-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41a3.8 3.8 0 0 1-1.38-.9 3.8 3.8 0 0 1-.9-1.38c-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16zM12 0C8.74 0 8.33.01 7.05.07 5.78.13 4.9.33 4.14.63a5.9 5.9 0 0 0-2.13 1.38A5.9 5.9 0 0 0 .63 4.14c-.3.76-.5 1.64-.56 2.91C.01 8.33 0 8.74 0 12s.01 3.67.07 4.95c.06 1.27.26 2.15.56 2.91a5.9 5.9 0 0 0 1.38 2.13 5.9 5.9 0 0 0 2.13 1.38c.76.3 1.64.5 2.91.56C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c1.27-.06 2.15-.26 2.91-.56a5.9 5.9 0 0 0 2.13-1.38 5.9 5.9 0 0 0 1.38-2.13c.3-.76.5-1.64.56-2.91.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.06-1.27-.26-2.15-.56-2.91a5.9 5.9 0 0 0-1.38-2.13A5.9 5.9 0 0 0 19.86.63c-.76-.3-1.64-.5-2.91-.56C15.67.01 15.26 0 12 0zm0 5.84a6.16 6.16 0 1 0 0 12.32 6.16 6.16 0 0 0 0-12.32zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm7.85-10.4a1.44 1.44 0 1 1-2.88 0 1.44 1.44 0 0 1 2.88 0z"/></svg>Instagram · 14 jul</div><div class="txt">Mismo texto, publicado como carrusel</div><div class="m"><b>82</b> likes · <b>0</b> comentarios</div></a>
  </div>
  <p class="note rv">Un mismo mensaje rinde el doble en un canal que en el otro: la diferencia no está en el contenido sino en el formato y la audiencia. Ese margen es exactamente lo que la misión captura.</p>

  <!-- H2 -->
  <h3 class="rv" style="margin-top:52px;">Hallazgo 02 · Se le habla al productor en el idioma del tostador</h3>
  <div class="card acc-g rv d1"><p><b>Las 20 publicaciones recientes de LinkedIn están 100% en inglés.</b> Según la lectura del propio CEO, quien lee a Caravela en LinkedIn es principalmente el productor, hispanohablante. La audiencia que efectivamente recibe el mensaje no coincide con la audiencia a la que el mensaje apunta.</p></div>
  <div class="card rv d2" style="margin-top:12px;">
    <h4>Cómo se verifica esto en la fase 01</h4>
    <p>Esta afirmación se apoya hoy en la lectura del CEO más el dato de idioma: es una hipótesis fuerte, no un hecho verificado. Por eso el resultado clave 2 de la misión existe. En la fase 01 se ejecuta una <b>extracción detallada de quién reacciona y comenta cada publicación</b>, tanto en LinkedIn como en Instagram, y de quién publica contenido alrededor de Caravela, para clasificar cada perfil por cargo, país y tipo de organización. Solo entonces sabremos con certeza si la audiencia que escucha es productora, tostadora o industria, y en qué proporción por canal. Sin ese dato, cualquier decisión de idioma y segmentación sería una apuesta.</p>
  </div>

  <!-- H3 -->
  <h3 class="rv" style="margin-top:52px;">Hallazgo 03 · El formato que mejor rinde no es el que más se usa</h3>
  <div class="card acc-p rv d1"><p>En Instagram, los <b>carruseles promedian 62,4 likes frente a 32,6 de video y 22,8 de imagen simple</b>: casi el doble. Y los tres primeros lugares son carruseles de lanzamiento de producto con historia detrás. Es decir: la dirección estratégica que Caravela quiere tomar (café por región, por productor, por perfil, por historia) <b>ya está validada por su propia audiencia</b>. La demanda existe; falta sistematizar la oferta.</p></div>
  <div class="bars rv d2" id="bars">
    <div class="bar-row"><span class="bar-lbl">Carrusel (12)</span><div class="bar-tr"><div class="bar-fl" data-w="100" style="background:var(--terra);"></div></div><span class="bar-val">62,4</span></div>
    <div class="bar-row"><span class="bar-lbl">Video (8)</span><div class="bar-tr"><div class="bar-fl" data-w="52" style="background:var(--gold);"></div></div><span class="bar-val">32,6</span></div>
    <div class="bar-row"><span class="bar-lbl">Imagen (4)</span><div class="bar-tr"><div class="bar-fl" data-w="37" style="background:var(--sage);"></div></div><span class="bar-val">22,8</span></div>
  </div>
  <p class="note rv">Promedio de likes por tipo de publicación sobre 24 publicaciones de Instagram analizadas.</p>
  <div class="ev rv d3">
    <a href="https://www.instagram.com/p/DbWAVgPFBwB/" target="_blank" rel="noopener"><div class="src">Instagram · Carrusel</div><div class="txt">"Special Release: Ecuador Sidra"</div><div class="m"><b>113</b> likes · <b>7</b> comentarios</div></a>
    <a href="https://www.instagram.com/p/DZ73fsqm6Yj/" target="_blank" rel="noopener"><div class="src">Instagram · Carrusel</div><div class="txt">"New Coffee Release: Ecuador Yacur"</div><div class="m"><b>106</b> likes · <b>1</b> comentario</div></a>
    <a href="https://www.instagram.com/p/DaDz8LRGWQM/" target="_blank" rel="noopener"><div class="src">Instagram · Carrusel</div><div class="txt">"Coffee brewed in Oaxaca City with our sourcing and milling partners"</div><div class="m"><b>101</b> likes · <b>2</b> comentarios</div></a>
    <a href="https://www.linkedin.com/posts/caravela-coffee_harvest-is-moving-across-colombia-ecuador-activity-7478888123460927488-yH-F" target="_blank" rel="noopener"><div class="src">LinkedIn · Mejor pieza</div><div class="txt">"Harvest is moving across Colombia, Ecuador and Peru"</div><div class="m"><b>38</b> reacciones · <b>1</b> comentario</div></a>
    <a href="https://www.linkedin.com/posts/caravela-coffee_pink-bourbon-has-become-one-of-colombias-activity-7472543665308155904-4vrG" target="_blank" rel="noopener"><div class="src">LinkedIn · Producto</div><div class="txt">"Pink Bourbon has become one of Colombia's most sought-after varieties"</div><div class="m"><b>35</b> reacciones · <b>0</b> comentarios</div></a>
    <a href="https://www.linkedin.com/posts/caravela-coffee_better-coffee-does-not-begin-at-the-cupping-activity-7482705669691748352-njWp" target="_blank" rel="noopener"><div class="src">LinkedIn · Origen</div><div class="txt">"Better coffee does not begin at the cupping table"</div><div class="m"><b>33</b> reacciones · <b>2</b> comentarios</div></a>
  </div>

  <!-- H4 -->
  <h3 class="rv" style="margin-top:52px;">Hallazgo 04 · Difusión sin conversación</h3>
  <div class="card acc rv d1"><p>Con 23.466 seguidores, LinkedIn produce <b>0,7 comentarios por publicación</b>: 14 comentarios en 20 publicaciones, y <b>11 de esas 20 no generaron ni un solo comentario</b>. Hay difusión, no diálogo. Un canal sin conversación no produce leads: produce impresiones.</p></div>
  <div class="ev rv d2">
    <a href="https://www.linkedin.com/posts/caravela-coffee_direct-trade-has-become-one-of-specialty-activity-7493214748411494400-GDKD" target="_blank" rel="noopener"><div class="src">LinkedIn · 12 ago</div><div class="txt">"Direct Trade has become one of specialty coffee's most widely used terms"</div><div class="m"><b>6</b> reacciones · <b>0</b> comentarios</div></a>
    <a href="https://www.linkedin.com/posts/caravela-coffee_knowledge-creates-value-when-it-leads-to-activity-7488896320317865984-ycJv" target="_blank" rel="noopener"><div class="src">LinkedIn · 31 jul</div><div class="txt">"Knowledge creates value..." (historia de Julián Olivera, productor con nombre propio)</div><div class="m"><b>10</b> reacciones · <b>0</b> comentarios</div></a>
    <a href="https://www.linkedin.com/posts/caravela-coffee_trust-in-coffee-is-never-instant-it-is-activity-7481263515207442432-5jXB" target="_blank" rel="noopener"><div class="src">LinkedIn · 10 jul</div><div class="txt">"Trust in coffee is never instant"</div><div class="m"><b>23</b> reacciones · <b>0</b> comentarios</div></a>
  </div>
  <p class="note rv">El caso del medio merece atención: la única pieza reciente centrada en un productor con nombre propio quedó entre las de menor rendimiento. No porque la historia no valga, sino porque el formato, el idioma y el ángulo no estaban diseñados para la audiencia de ese canal. Es el mejor argumento de por qué las 4 líneas editoriales necesitan diseño por canal y no solo por tema.</p>

  <!-- H5 -->
  <h3 class="rv" style="margin-top:52px;">Hallazgo 05 · Un canal de autoridad dormido</h3>
  <div class="card acc-s rv d1"><p>"Notes from the team" contiene material de alto valor comercial: precisamente el que un tostador consulta antes de comprometer contratos. Pero la cadencia es irregular, con saltos de meses y hasta años entre publicaciones. Es autoridad construida y desaprovechada.</p></div>
  <div class="ev rv d2">
    <a href="https://www.caravela.coffee/en/notes-from-the-team" target="_blank" rel="noopener"><div class="src">Blog · 5 jul 2026</div><div class="txt">"Direct Trade Coffee: What It Really Means for Your Business"</div><div class="m">Publicación más reciente</div></a>
    <a href="https://www.caravela.coffee/en/notes-from-the-team" target="_blank" rel="noopener"><div class="src">Blog · 10 jun 2025</div><div class="txt">White Paper: "Caravela Responds to Misrepresentations in Coffee Intelligence Articles"</div><div class="m">13 meses sin secuela</div></a>
    <a href="https://www.caravela.coffee/en/notes-from-the-team" target="_blank" rel="noopener"><div class="src">Blog · 20 nov 2022</div><div class="txt">"Cost of Production Spotlight: Price Spikes, Higher Incomes"</div><div class="m">El activo más valioso, sin actualizar</div></a>
  </div>
  <p class="note rv">El estudio de costo de producción es, en criterio del diagnóstico, el contenido con mayor potencial comercial de todo el sitio: es el que demuestra que Caravela sabe de qué habla cuando dice prosperidad. Lleva casi cuatro años sin actualizarse.</p>

  <!-- H6 -->
  <h3 class="rv" style="margin-top:52px;">Hallazgo 06 · La estrategia que se busca ya está funcionando, sin sistema</h3>
  <div class="card acc rv d1" style="border-left-width:5px;"><p>El hallazgo más accionable del diagnóstico. <b>El 12 de agosto, el perfil personal del CEO publicó una pieza que obtuvo 142 reacciones y 15 comentarios. El mismo día, la página corporativa publicó y obtuvo 6 reacciones y 0 comentarios.</b> Una diferencia de <b>23 veces</b> en reacciones, el mismo día, la misma compañía.</p></div>
  <div class="kpi-row rv d2">
    <div class="kpi"><div class="v t">88,0</div><div class="l">Reacciones media · perfil del CEO</div><div class="s">9,0 comentarios de media</div></div>
    <div class="kpi"><div class="v gd">25,2</div><div class="l">Reacciones media · José Manjarres</div><div class="s">2,5 comentarios de media</div></div>
    <div class="kpi"><div class="v">24,4</div><div class="l">Reacciones media · página corporativa</div><div class="s">0,7 comentarios de media</div></div>
    <div class="kpi"><div class="v t">12,9x</div><div class="l">Más conversación en el perfil del CEO</div><div class="s">Frente a la página</div></div>
  </div>
  <div class="ev rv d3">
    <a href="https://www.linkedin.com/posts/alejandro-c-74241a_following-my-post-yesterday-i-wanted-to-ugcPost-7493061742126731265-KsGO" target="_blank" rel="noopener"><div class="src">LinkedIn · Alejandro Cadena · 12 ago</div><div class="txt">Publicación personal del CEO sobre un hecho ocurrido en la trilladora de Armenia</div><div class="m"><b>142</b> reacciones · <b>15</b> comentarios</div></a>
    <a href="https://www.linkedin.com/posts/caravela-coffee_direct-trade-has-become-one-of-specialty-activity-7493214748411494400-GDKD" target="_blank" rel="noopener"><div class="src">LinkedIn · Página corporativa · 12 ago</div><div class="txt">"Direct Trade has become one of specialty coffee's most widely used terms"</div><div class="m"><b>6</b> reacciones · <b>0</b> comentarios</div></a>
    <a href="https://www.linkedin.com/posts/josemanjarres_specialtycoffee-greencoffee-coffeesourcing-activity-7480969102820409344--tJz" target="_blank" rel="noopener"><div class="src">LinkedIn · José Manjarres · 9 jul</div><div class="txt">"Harvest Coffee Update: Peru" (línea editorial por región, publicada de forma espontánea)</div><div class="m"><b>42</b> reacciones · <b>0</b> comentarios</div></a>
  </div>
  <div class="card rv" style="margin-top:20px;">
    <h4>Lo que esto significa</h4>
    <ul class="bl">
      <li>La palanca de mayor retorno y menor costo no es producir más contenido corporativo: es <b>activar y dar sistema a las voces personales</b> del equipo, empezando por las dos que ya publican.</li>
      <li>El perfil de José Manjarres ya se describe públicamente como quien ayuda a tostadores a abastecerse en 7 orígenes latinoamericanos: <b>es el mensaje al tostador que el CEO quiere construir, ya escrito</b>, y sus publicaciones propias sobre cosecha en Perú y Ecuador son exactamente la línea editorial "café por región" ocurriendo de forma espontánea.</li>
      <li>La pieza del CEO que más rindió no era corporativa ni promocional: era humana, concreta y verificable. Eso indica el registro que su audiencia premia, y es la dirección que el banco de historias debe tomar.</li>
      <li>No se trata de reemplazar la página corporativa, sino de darle a las voces personales <b>materia prima, cadencia y medición</b>, que es precisamente lo que hoy no tienen.</li>
    </ul>
  </div>


  <h3 class="rv" style="margin-top:44px;">El banco de voces disponible</h3>
  <p class="lead rv d1" style="font-size:15px;">Seis perfiles del equipo con audiencia propia y ángulo editorial distinto. Dos ya publican de forma sostenida; los otros cuatro tienen el perfil, el conocimiento y la relación con el cliente, pero no la estructura para hacerlo. Esa estructura es lo que la misión construye.</p>
  <div class="voces rv d2">
    <a class="voz on" href="https://www.linkedin.com/in/alejandro-c-74241a" target="_blank" rel="noopener">
      <img src="data:image/png;base64,__LOGO__" alt="" style="object-fit:contain;background:var(--cream2);padding:6px;">
      <div><div class="voz-n">Alejandro Cadena</div><div class="voz-c">Cofundador y CEO</div>
      <div class="voz-a">La voz de mayor alcance de la compañía: 88 reacciones y 9 comentarios de media. Su registro más efectivo es el humano y concreto, no el corporativo.</div>
      <span class="voz-t vt-on">Ya publica</span></div>
    </a>
    <a class="voz on" href="https://www.linkedin.com/in/josemanjarres" target="_blank" rel="noopener">
      <img src="data:image/jpeg;base64,__P_MANJARRES__" alt="José Manjarres">
      <div><div class="voz-n">José Manjarres</div><div class="voz-c">Café de especialidad, abastecimiento en 7 orígenes</div>
      <div class="voz-a">Su titular ya es el mensaje al tostador que se quiere construir. Sus notas de cosecha en Perú y Ecuador son la línea "café por región" ocurriendo sola.</div>
      <span class="voz-t vt-on">Ya publica</span></div>
    </a>
    <a class="voz" href="https://www.linkedin.com/in/giancarlo-ghiretti-b9a276" target="_blank" rel="noopener">
      <img src="data:image/jpeg;base64,__P_GIANCARLO__" alt="Giancarlo Ghiretti">
      <div><div class="voz-n">Giancarlo Ghiretti</div><div class="voz-c">Cofundador, CFO y COO (desde 2002)</div>
      <div class="voz-a">24 años de historia de la compañía y la única voz que puede hablar con autoridad de la economía del modelo: precio, costo de producción y por qué el negocio se sostiene.</div>
      <span class="voz-t vt-off">Sin actividad editorial</span></div>
    </a>
    <a class="voz" href="https://www.linkedin.com/in/nicole-freydell" target="_blank" rel="noopener">
      <img src="data:image/jpeg;base64,__P_NICOLE__" alt="Nicole Freydell">
      <div><div class="voz-n">Nicole Freydell</div><div class="voz-c">Brand Business Leader (desde abril 2025)</div>
      <div class="voz-a">MBA con siete años en gestión de marca internacional. Es la contraparte natural de este rol dentro de Caravela: la misión se diseña con ella, no sobre ella.</div>
      <span class="voz-t vt-off">Aliada clave del rol</span></div>
    </a>
    <a class="voz" href="https://www.linkedin.com/in/adela-vavreckova-2095011a3" target="_blank" rel="noopener">
      <img src="data:image/jpeg;base64,__P_ADELA__" alt="Adela Vavreckova">
      <div><div class="voz-n">Adela Vavreckova</div><div class="voz-c">Product Specialist, Reino Unido</div>
      <div class="voz-a">Fue tostadora principal y compradora de café verde en Londres antes de entrar. Habla el idioma del tostador europeo porque lo fue: la voz ideal para la línea "café por perfil".</div>
      <span class="voz-t vt-off">Puente con el tostador UE</span></div>
    </a>
    <a class="voz" href="https://www.linkedin.com/in/juan-camilo-aristizabal-lopez-comercial" target="_blank" rel="noopener">
      <img src="data:image/jpeg;base64,__P_JUANCA__" alt="Juan Camilo Aristizabal">
      <div><div class="voz-n">Juan Camilo Aristizabal</div><div class="voz-c">Business Development Lead (desde nov 2025)</div>
      <div class="voz-a">Lidera la distribución nacional de la nueva línea de café al consumidor final. Es el vínculo directo entre la estrategia de contenido y el pipeline comercial que se quiere medir.</div>
      <span class="voz-t vt-off">Dueño del funnel comercial</span></div>
    </a>
  </div>
  <p class="note rv">Fuente: perfiles públicos de LinkedIn, extracción propia del 12 de agosto de 2026. La clasificación de actividad editorial se basa en las publicaciones visibles al momento de la extracción.</p>

  <div class="card acc-g rv" style="margin-top:34px;">
    <h4>Lo que este diagnóstico todavía no ve</h4>
    <p>Esta es la vista externa. Las palancas grandes están adentro: los datos de la intranet, las métricas de administrador de cada canal, el CRM comercial y la identidad real de quienes hoy interactúan. La fase 01 integra ambas vistas, y las preguntas de la siguiente sección son el primer paso para hacerlo.</p>
  </div>
 </div>
</section>

<!-- ============ 5. INSUMOS ============ -->
<section id="insumos" class="sec-olive">
 <div class="wrap">
  <div class="eyebrow rv">05 · Insumos</div>
  <h2 class="rv d1">Diez preguntas que<br>afinan la línea base</h2>
  <p class="lead rv d2">Respuestas que convierten este Inception Report v0 en la línea base definitiva de la misión. Ninguna requiere preparación: son datos que el negocio ya tiene. Se responden en la sesión de kickoff.</p>

  <div class="rv d3" style="margin-top:34px;">
    <div class="q"><span class="q-n">01</span><div><div class="q-t">¿Cuántos tostadores clientes activos hay hoy y en qué mercados se concentra la facturación?</div><div class="q-w">Define el denominador del lifetime value y prioriza idiomas y canales de la estrategia.</div></div></div>
    <div class="q"><span class="q-n">02</span><div><div class="q-t">¿Qué falló exactamente con la agencia de community management anterior?</div><div class="q-w">Es el molde de lo que no debemos repetir. Proceso, expectativas, contenido o medición: cada causa cambia el diseño del equipo.</div></div></div>
    <div class="q"><span class="q-n">03</span><div><div class="q-t">¿Quién comunica hoy? ¿Qué personas o proveedores publican, con qué rol y qué autonomía?</div><div class="q-w">Para diseñar la capa de estrategia sin duplicar ni desplazar a quien ya ejecuta.</div></div></div>
    <div class="q"><span class="q-n">04</span><div><div class="q-t">¿Qué datos viven en la intranet y quién puede habilitar acceso de lectura?</div><div class="q-w">Es la materia prima del banco de historias y el candado crítico de la misión (riesgo alto de la sección 03).</div></div></div>
    <div class="q"><span class="q-n">05</span><div><div class="q-t">¿Dónde viven los leads comerciales hoy? ¿Existe CRM y quién da seguimiento a una oportunidad nueva?</div><div class="q-w">Sin esto el funnel no tiene dónde aterrizar. Si no existe, la misión lo monta en versión mínima.</div></div></div>
    <div class="q"><span class="q-n">06</span><div><div class="q-t">¿Cuántas tiendas y espacios comerciales hay, dónde están y qué papel comercial juegan hoy?</div><div class="q-w">Define el alcance del piloto de tiendas dentro del resultado clave 4.</div></div></div>
    <div class="q"><span class="q-n">07</span><div><div class="q-t">¿Qué metas comerciales tiene el año? ¿Cuántos clientes nuevos o qué crecimiento se espera?</div><div class="q-w">Para fijar el valor de N del resultado clave 6 con ancla en el plan real, no en un número inventado.</div></div></div>
    <div class="q"><span class="q-n">08</span><div><div class="q-t">Sobre las voces personales: el diagnóstico mapeó seis perfiles con potencial (dos ya activos y cuatro sin estructura editorial). ¿Cuáles estarían dispuestos, y cuánto esfuerzo adicional puede invertir el CEO en su propio perfil?</div><div class="q-w"><b>Contexto del hallazgo 06:</b> el perfil del CEO rinde 3,6 veces más reacciones y 12,9 veces más comentarios que la página corporativa. La pregunta no es si funciona (ya está demostrado) sino con qué insumos y qué cadencia se sostiene sin quitarle tiempo al negocio. Y una segunda pregunta, sobre Nicole Freydell: ¿cómo se articula este rol con Brand para sumar en lugar de duplicar?</div></div></div>
    <div class="q"><span class="q-n">09</span><div><div class="q-t">¿Existe presupuesto o disposición para el equipo mínimo de apoyo (producción audiovisual y edición)?</div><div class="q-w">Dimensiona la fase 03. Con datos internos y equipo mínimo la misión produce; sin ellos, prioriza distinto.</div></div></div>
    <div class="q"><span class="q-n">10</span><div><div class="q-t">¿Qué historias considera el CEO que Caravela nunca ha sabido contar, y le duele que no se cuenten?</div><div class="q-w">La pregunta menos técnica y la más importante: alinea la misión con la ambición real de quien la confía.</div></div></div>
  </div>
 </div>
</section>

<!-- ============ 6. PASOS ============ -->
<section id="pasos" class="sec-white">
 <div class="wrap">
  <div class="eyebrow rv">06 · Siguiente</div>
  <h2 class="rv d1">Tres movimientos<br>para arrancar</h2>

  <div class="rv d2" style="margin-top:26px;">
    <div class="paso"><div class="paso-n">01</div><div><h3>Sesión de kickoff</h3><p>Entre 60 y 90 minutos con el CEO para validar el rol y la misión, responder las diez preguntas de la sección 05, fijar juntos el valor de N del resultado clave 6 y definir el candado de acceso a los datos internos. De esa sesión sale la versión definitiva de la línea base.</p></div></div>
    <div class="paso"><div class="paso-n">02</div><div><h3>Acuerdo de colaboración</h3><p>El modelo de vinculación y las condiciones económicas se conversan directamente en la sesión de kickoff. El formato de misión está propuesto precisamente para eso: que Caravela compre resultados verificables con reglas claras para ambas partes, dentro del principio de equidad de la casa.</p></div></div>
    <div class="paso"><div class="paso-n">03</div><div><h3>Arranque de la fase 01</h3><p>Con acceso y línea base validados, el diagnóstico profundo arranca la semana siguiente al acuerdo. Primer tablero disponible para el CEO al cierre de la semana 3, y análisis de audiencia real por canal al cierre de la semana 4.</p></div></div>
  </div>

  <div class="quote rv" style="margin-top:46px;">
    <p>La primera misión no es una prueba de contenido: es la prueba de que Caravela puede confiar una misión, medirla sin pedir reportes y decidir con números si se escala.</p>
    <cite>Ese es el rol</cite>
  </div>
 </div>
</section>

<footer>
  <div style="display:flex;align-items:center;gap:14px;"><img src="data:image/png;base64,__LOGO__" alt="Caravela"><span>Growth &amp; Strategic Projects Lead · Propuesta de rol y Misión 1</span></div>
  <span>v2 · Agosto de 2026 · Alejandro Gil Rivera · Incluye Inception Report v0</span>
</footer>

<script>
// progreso + nav
var prog=document.getElementById('prog'), nav=document.getElementById('nav');
var secs=[].slice.call(document.querySelectorAll('section[id]'));
var navlinks=[].slice.call(document.querySelectorAll('.nav-r a'));
function onScroll(){
  var st=window.scrollY||document.documentElement.scrollTop;
  var h=document.documentElement.scrollHeight-window.innerHeight;
  prog.style.width=(h>0?(st/h*100):0)+'%';
  if(st>window.innerHeight*0.72){nav.classList.add('show');}else{nav.classList.remove('show');}
  var cur=null;
  secs.forEach(function(s){ if(s.getBoundingClientRect().top<=180) cur=s.id; });
  navlinks.forEach(function(a){ a.classList.toggle('act', a.getAttribute('href')==='#'+cur); });
}
window.addEventListener('scroll',onScroll,{passive:true}); onScroll();

// reveal
var io=new IntersectionObserver(function(es){
  es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} });
},{threshold:0.12,rootMargin:'0px 0px -8% 0px'});
[].slice.call(document.querySelectorAll('.rv:not(.in),.rvx:not(.in)')).forEach(function(el){io.observe(el);});

// barras
var bio=new IntersectionObserver(function(es){
  es.forEach(function(e){
    if(e.isIntersecting){
      [].slice.call(e.target.querySelectorAll('.bar-fl')).forEach(function(b,i){
        setTimeout(function(){ b.style.width=b.getAttribute('data-w')+'%'; }, i*180);
      });
      bio.unobserve(e.target);
    }
  });
},{threshold:0.4});
var bars=document.getElementById('bars'); if(bars) bio.observe(bars);
</script>
</body>
</html>
"""

out = HTML.replace("__LOGO__", LOGO).replace("__FOTO__", FOTO).replace("__CV__", CV)
for _k, _v in P.items():
    out = out.replace("__P_" + _k.upper() + "__", _v)
open("caravela-growth-lead-propuesta-v2.html", "w", encoding="utf-8").write(out)
print("OK ->", os.path.getsize("caravela-growth-lead-propuesta-v2.html")//1024, "KB")
print("placeholders restantes:", out.count("__LOGO__")+out.count("__FOTO__")+out.count("__CV__"))
