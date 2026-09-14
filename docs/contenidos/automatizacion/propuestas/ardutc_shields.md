---
title: Diseño y construcción de shields de Arduino para su uso en prácticas con ArduTC
order: 3
type: TFG
status: disponible
keywords:
  - Automatización
  - Arduino/Shield
  - ArduTC
  - TwinCAT 3
summary: Desarrollo de un conjunto de shields de Arduino para realización de prácticas de automatización con ArduTC.
---

# {{ title }} {.project-title}

{{ project_header() }}

## Descripción

La realización de prácticas docentes con PLC en la ingeniería supone un desafío en los centros educativos debido al alto coste, el espacio ocupado y el mantenimiento de los equipos necesarios para llevarlas a cabo. Esto aboca al alumnado a tomar turnos para
realizar ejercicios de automatización o, si esto no es posible, al uso de simuladores, reduciendo considerablemente la experiencia práctica.

ArduTC nace como un intento de democratización del *hardware* para automatización, desarrollando un sistema de muy bajo coste que convierte una placa de desarrollo de Arduino UNO en una interfaz entre TwinCAT, el *software* comercial de programación de PLC de Beckhoff, y elementos básicos de automatización como LEDs, pulsadores, sensores analógicos y servomotores, sustituyendo en última instancia a un PLC comercial.

ArduTC se comunica de manera transparente con un programa TwinCAT que se ejecuta en un PC mediante el protocolo ADS, aplicando los cambios en las variables del programa
a los pines analógicos y digitales de una placa Arduino y viceversa.

Esto convierte a ArduTC en un dispositivo ideal para la realización de prácticas a bajo coste, proporcionando diferentes montajes que implementan sistemas de automatización útiles para la consolidación de conocimientos clave en asignaturas del departamento.

Ejemplos de estos montajes son: semáforos, puertas de aparcamiento, calefactores, etc.

## Objetivos

- Especificación y diseño de un catálogo de montajes de prácticas.
- Diseño y fabricación de *shields* Arduino en PCB con los montajes.
- Implementación de código en TwinCAT para el control de los montajes.
- Documentación de las prácticas.

## Titulaciones recomendadas

- Grado en Ingeniería Electrónica, Robótica y Mecatrónica (GIERM).
- **Grado en Ingeniería Electrónica Industrial (GIEI).**
- Grado en Ingeniería en Tecnologías Industriales (GITI).

## Conocimientos recomendados

Se valorarán conocimientos en:

- automatización;
- diseño de PCBs;
- programación de PLCs en TwinCAT 3;

## Software

`ArduTC` `TwinCAT 3` `KiCad`

## Hardware

- Placa ArduTC
- Arduino Shield
- Componentes electrónicos
- PC

<div class="project-contact" markdown>

### ¿Te interesa?

Si tienes interés en este trabajo, contáctame por <a href="mailto:famoreno@uma.es?Subject=Interés%20en%20TFE">correo electrónico</a> para comentar el proyecto y valorar su adecuación a tu perfil.

</div>