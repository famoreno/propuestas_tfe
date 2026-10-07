---
title: Sistema de evaluación motora mediante visión artificial para el seguimiento de alteraciones del movimiento
order: 1
type: TFG
status: disponible
cotutor: None
keywords:
  - Visión artificial
  - MediaPipe
  - Ingeniería biomédica
  - Análisis de movimiento
  - Parkinson
summary: Desarrollo de un sistema basado en visión artificial para cuantificar parámetros motores y facilitar el seguimiento longitudinal de alteraciones del movimiento.
---

# {{ title }} {.project-title}

{{ project_header() }}

## Descripción

La evaluación de alteraciones motoras asociadas a enfermedades neurodegenerativas se basa habitualmente en pruebas clínicas y en la observación del paciente por parte de personal especializado. El uso de técnicas de visión artificial puede complementar esta evaluación proporcionando medidas cuantitativas y repetibles del movimiento.

Este TFG propone desarrollar un sistema de evaluación motora mediante visión artificial en el que el usuario realice, frente a una cámara, un conjunto de pruebas motoras sencillas, como temblor en reposo, *finger tapping*, apertura y cierre de la mano y movimientos de pronación y supinación.

A partir de las imágenes capturadas, se utilizará **MediaPipe** o librerías similares para realizar el seguimiento de puntos de interés de las manos y extraer las trayectorias necesarias para calcular variables biomecánicas relacionadas con la ejecución de las pruebas. Entre otras, podrán analizarse la frecuencia del temblor, la velocidad de los movimientos, su amplitud, regularidad y las posibles asimetrías entre ambas manos.

El objetivo no es realizar un diagnóstico automático ni sustituir la valoración clínica, sino estudiar el desarrollo de una herramienta de apoyo que permita obtener indicadores cuantitativos y facilitar el seguimiento longitudinal de alteraciones motoras, con especial interés en las asociadas a la enfermedad de Parkinson.

## Objetivos

- Diseño de un protocolo sencillo de adquisición para la realización de distintas pruebas motoras frente a una cámara.
- Implementación de un sistema de seguimiento de manos y puntos de interés mediante librerías de seguimiento por visión artificial.
- Procesamiento de las trayectorias obtenidas para extraer parámetros cuantitativos del movimiento.
- Análisis de variables como frecuencia de temblor, velocidad, amplitud, regularidad y asimetría entre ambas manos.
- Desarrollo de una herramienta para visualizar y almacenar los resultados de las distintas pruebas y permitir su comparación a lo largo del tiempo.
- Evaluación experimental del sistema mediante secuencias de prueba.
- Documentación del sistema desarrollado.

## Titulaciones recomendadas

- **Grado en Ingeniería de la Salud.**
- Grado en Ingeniería Electrónica, Robótica y Mecatrónica (GIERM).

## Conocimientos recomendados

Se valorarán conocimientos en:

- programación en Python;
- visión artificial;
- procesamiento de imágenes;
- procesamiento y análisis de señales;
- fundamentos de biomecánica;
- análisis y representación de datos.

## Software

`Python` `MediaPipe` `OpenCV` `NumPy` `SciPy` `Matplotlib` `Visual Studio Code`

## Hardware

- Cámara RGB o webcam
- PC de propósito general

<div class="project-contact" markdown>

### ¿Te interesa?

Si tienes interés en este trabajo, contáctame por <a href="mailto:famoreno@uma.es?Subject=Interés%20en%20TFE">correo electrónico</a> para comentar el proyecto y valorar su adecuación a tu perfil.

</div>
