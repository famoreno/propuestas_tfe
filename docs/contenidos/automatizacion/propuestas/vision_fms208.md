---
title: Sistema de inventariado visual de bajo coste para el almacén de la estación FMS-208
order: 4
type: TFG
status: disponible
keywords:
  - Automatización
  - Visión artificial
  - Python
  - ADS
  - FMS-208
summary: Desarrollo de un sistema de visión artificial de bajo coste para identificar el estado del almacén de la estación FMS-208 y comunicarlo al PLC mediante ADS.
---

# {{ title }} {.project-title}

{{ project_header() }}

## Descripción

Los programas de control de la estación FMS-208 del [sistema modular de fabricación flexible SMC FMS-200](../../../pdf/FMS_200_Descripcion_Funcional.pdf){:target="_blank"} asumen un almacén vacío al iniciarse, ya que ésta no dispone de mecanismos para identificar el estado del mismo.

Los controladores PLC de las estaciones (de marca Beckhoff) no son especialmente amigables con sistemas de procesamiento de imágenes, ya que están diseñados con objetivos distintos. Existen sistemas industriales comerciales que permiten el acceso de los PLCs a cámaras para el análisis de imágenes, pero presentan tres dificultades: (i) están basados en máquinas de estados, lo que dificulta su uso, (ii) consumen muchos recursos del controlador, poniendo en peligro la ejecución determinista del programa de control y (iii) tiene un coste elevado, habitualmente.

La inspección visual del almacén de la estación FMS-208 puede realizarse de manera externa con un PC de propósito general y una webcam de bajo coste, comunicando el resultado al PLC de control mediante el protocolo ADS, nativo de Beckhoff. De esta manera, se puede derivar la carga computacional al PC cuando se requiera y recibir la información del estado cuando el procesamiento se haya completado.

Este TFG propone realizar un sistema de inspección visual de bajo coste basado en scripts de Python y comunicación ADS.

## Objetivos

- Instalación de un sistema de inspección visual de bajo coste, basado en una webcam y un PC, en la estación FMS-208.
- Implementación en Python de un programa de visión artificial para identificar el estado del almacén.
- Desarrollo de la comunicación mediante ADS entre el programa Python y el PLC Beckhoff que controla la estación FMS-208.
- Integración de la imagen de la cámara y del resultado de la inspección en el HMI del programa de control.
- Documentación del programa realizado.

## Titulaciones recomendadas

- **Grado en Ingeniería Electrónica, Robótica y Mecatrónica (GIERM).**
- Grado en Ingeniería Electrónica Industrial (GIEI).
- Grado en Ingeniería en Tecnologías Industriales (GITI).

## Conocimientos recomendados

Se valorarán conocimientos en:

- automatización;
- programación en Python;
- programación de PLCs en TwinCAT 3;
- visión artificial;
- inteligencia artificial;

## Software

`Python` `OpenCV` `pyads` `TwinCAT 3` `Visual Studio Code`

## Hardware

- FMS-208
- PLC Beckhoff de la estación
- Webcam de bajo coste
- Sistema de iluminación uniforme
- PC de propósito general

<div class="project-contact" markdown>

### ¿Te interesa?

Si tienes interés en este trabajo, contáctame por <a href="mailto:famoreno@uma.es?Subject=Interés%20en%20TFE">correo electrónico</a> para comentar el proyecto y valorar su adecuación a tu perfil.

</div>
