# Sistema de pulsación de botones para un robot móvil

## Descripción

Este trabajo plantea la resolución del problema de accesibilidad multi-piso mediante robótica móvil autónoma. La propuesta consiste en equipar un robot móvil con un brazo robótico de bajo peso y un efector final flexible (diseñado e impreso en 3D) capaz de interactuar físicamente con los paneles de botones de un ascensor. El robot deberá aproximarse al panel, reconocer los botones y sus etiquetas mediante visión artificial y OCR, ejecutar la pulsación precisa del botón de llamada o de piso, acceder al ascensor, seleccionar la planta de destino y salir autónomamente al llegar al piso indicado.

## Objetivos

- Integración física y cinemática de un manipulador robótico ligero sobre la plataforma robótica móvil.
- Diseño 3D y fabricación mediante impresión aditiva (TPU/material flexible) de un efector final optimizado para la pulsación de botones.
- Desarrollo de un sistema de visión artificial dotado de OCR para la detección, localización 3D y lectura de números en paneles de botones.
- Planificación de trayectorias del brazo robótico (MoveIt2) para la maniobra segura de aproximación y contacto.

## Grados

- GIERM, GIEI y GITI.

## Conocimientos previos

ROS2, programación en C++ / Python, navegación de robots móviles, visión artificial y OCR, cinemática y control de brazos robóticos, diseño 3D asistido por ordenador (CAD) y modelado para impresión flexible.

## Software

ROS2, MoveIt2, Nav2, OpenCV, Tesseract OCR / EasyOCR, software CAD (FreeCAD / SolidWorks), programa de laminado para impresión 3D (PrusaSlicer / Cura).

## Hardware

Plataforma robótica móvil preexistente, brazo robótico de bajo peso Interbotix, cámara montada en el brazo (estándar / RGB-D), efector final flexible impreso en TPU, impresora 3D FDM.
