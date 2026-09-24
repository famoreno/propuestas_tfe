---
title: Gemelos Digitales en Godot de las estaciones del sistema FMS-200
order: 1
type: TFG
status: parcial
keywords:
  - Gemelos digitales
  - Diseño 3D
  - Godot
  - TwinCAT 3
  - ADS
  - FMS-200
summary: Desarrollo de gemelos digitales interactivos de distintas estaciones del sistema didáctico FMS-200.
variants:
  - name: FMS-201
    status: completado
  - name: FMS-202
    status: solicitado # sofia borregon
  - name: FMS-205
    status: disponible
  - name: FMS-206
    status: asignado # eva torres lopez
  - name: FMS-208
    status: disponible
---

# {{ title }} {.project-title}

{{ project_header() }}

## Descripción

Este TFG tiene como finalidad el diseño, desarrollo e implementación de Gemelos Digitales (*Digital Twins*) interactivos en tiempo real para las estaciones del [sistema modular de fabricación flexible SMC FMS-200](../../../pdf/FMS_200_Descripcion_Funcional.pdf){:target="_blank"}. Utilizando el motor gráfico Godot Engine y modelos 3D creados en FreeCAD, se construirá una representación tridimensional cinemática del sistema. El entorno virtual se comunicará bidireccionalmente con el PLC físico mediante Beckhoff TwinCAT 3, permitiendo reflejar el estado real de la planta, simular secuencias de control y realizar validaciones sin riesgo para el equipamiento físico.

## Objetivos

- Modelado y simplificación CAD 3D de los componentes mecánicos de las estaciones FMS-200 utilizando FreeCAD.
- Estructuración de la escena y programación de la lógica de animación cinemática e interactividad en Godot Engine.
- Implementación de la pasarela de comunicación en tiempo real entre Godot y TwinCAT 3 (vía protocolo ADS).
- Sincronización bidireccional de señales de E/S (sensores y actuadores) entre el PLC físico y el modelo 3D.
- Ensayos de validación del Gemelo Digital mediante la ejecución de rutinas completas de automatización.

## Titulaciones recomendadas

- Grado en Ingeniería Electrónica, Robótica y Mecatrónica (GIERM).
- Grado en Ingeniería Electrónica Industrial (GIEI).
- Grado en Ingeniería en Tecnologías Industriales (GITI).

## Conocimientos recomendados

Se valorarán conocimientos en:

- programación estructurada y orientada a objetos (GDScript en Godot o C#);
- programación de PLCs en TwinCAT 3 y lenguajes IEC 61131-3;
- diseño y modelado 3D paramétrico con FreeCAD;
- comunicaciones industriales.

## Software

`Godot Engine` `TwinCAT 3` `FreeCAD / Solidworks` `ADS`

## Hardware

- Estaciones de fabricación flexible SMC FMS-200.
- PLC o controlador industrial Beckhoff (o PC de control compatible).
- Equipo informático para diseño 3D.

<div class="project-contact" markdown>

### ¿Te interesa?

Si tienes interés en este trabajo, contáctame por <a href="mailto:famoreno@uma.es?Subject=Interés%20en%20TFE">correo electrónico</a> para comentar el proyecto y valorar su adecuación a tu perfil.

</div>
