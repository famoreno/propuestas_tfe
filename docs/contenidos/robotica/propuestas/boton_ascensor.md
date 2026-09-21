---
title: Sistema de interacción con ascensores mediante visión artificial para robot móvil autónomo.
order: 2
type: TFG
status: solicitado # paula mancilla
keywords:
  - ROS 2
  - Programación
  - Navegación
  - Visión artificial
  - OCR
summary: Desarrollo de un sistema de visión artificial y manipulación para reconocer y pulsar botones de ascensor para un robot móvil autónomo.
---

# {{ title }} {.project-title}

{{ project_header() }}

## Descripción

Este trabajo plantea la resolución del problema de accesibilidad multi-piso mediante robótica móvil autónoma.

La propuesta consiste en equipar un robot móvil con un brazo robótico de bajo peso y un efector final flexible, diseñado e impreso en 3D, capaz de interactuar físicamente con los paneles de botones de un ascensor.

El robot deberá ser capaz de:

- aproximarse al panel de botones;
- reconocer los botones y sus etiquetas mediante visión artificial y OCR;
- ejecutar la pulsación precisa del botón de llamada o de piso;
- acceder al ascensor;
- seleccionar la planta de destino;
- salir autónomamente al llegar al piso indicado.

## Objetivos

- Integración física y cinemática de un manipulador robótico ligero sobre la plataforma robótica móvil.
- Diseño 3D y fabricación mediante impresión aditiva, utilizando TPU u otro material flexible, de un efector final optimizado para la pulsación de botones.
- Desarrollo de un sistema de visión artificial dotado de OCR para la detección, localización 3D y lectura de números en paneles de botones.
- Planificación de trayectorias del brazo robótico mediante **MoveIt 2** para realizar de forma segura las maniobras de aproximación y contacto.

## Titulaciones recomendadas

- Grado en Ingeniería Electrónica, Robótica y Mecatrónica (GIERM).
- Grado en Ingeniería Electrónica Industrial (GIEI).
- Grado en Ingeniería en Tecnologías Industriales (GITI).

## Conocimientos recomendados

Se valorarán conocimientos en:

- ROS 2;
- programación en C++ y/o Python;
- navegación de robots móviles;
- visión artificial y OCR;
- cinemática y control de brazos robóticos;
- diseño 3D asistido por ordenador (CAD);
- modelado para impresión 3D con materiales flexibles.

## Software

`ROS 2` `OpenCV` `Tesseract OCR / EasyOCR` `FreeCAD / SolidWorks` `PrusaSlicer / Cura`

## Hardware

- Plataforma robótica móvil preexistente.
- Brazo robótico ligero Interbotix.
- Cámara montada en el brazo, estándar o RGB-D.
- Efector final flexible impreso en TPU.
- Impresora 3D FDM.

<div class="project-contact" markdown>

### ¿Te interesa?

Si tienes interés en este trabajo, contáctame por <a href="mailto:famoreno@uma.es?Subject=Interés%20en%20TFE">correo electrónico</a> para comentar el proyecto y valorar su adecuación a tu perfil.

</div>
