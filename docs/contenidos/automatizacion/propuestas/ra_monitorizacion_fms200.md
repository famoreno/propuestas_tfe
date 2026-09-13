---
title: Realidad Aumentada para monitorización de datos de estaciones FMS-200 en dispositivos móviles
order: 2
type: TFG
status: disponible
keywords:
  - Realidad aumentada
  - FMS-200
  - Monitorización
  - MQTT
  - Visión artificial
summary: Desarrollo de una aplicación de realidad aumentada para visualizar información de las estaciones FMS-200 desde dispositivos móviles.
---

# {{ title }} {.project-title}

{{ project_header() }}

## Descripción

El proyecto aborda la creación de un sistema de supervisión en planta basado en Realidad Aumentada (RA) para dispositivos móviles (smartphones o tablets Android). La aplicación permitirá a los operadores o estudiantes apuntar con la cámara hacia una estación FMS-200 y visualizar, superpuestos en la imagen real, paneles interactivos con información telemétrica en tiempo real (estados de actuadores, sensores, contadores, alarmas y variables internas del PLC). El flujo de datos se estructurará mediante publicaciones MQTT desde TwinCAT 3 hacia la aplicación móvil.

## Objetivos

- Configuración del módulo de comunicación MQTT en TwinCAT 3 para la publicación periódica del estado de la estación.
- Desarrollo de la aplicación móvil nativa Android o en motor con soporte AR (ARCore / Unity AR Foundation).
- Integración de algoritmos de visión artificial / marcadores para el reconocimiento y posicionamiento espacial 3D sobre la estación FMS-200.
- Diseño de una interfaz HMI inmersiva e intuitiva para la representación de datos de telemetría en tiempo real.
- Evaluación de latencias, consumo de recursos y precisión del seguimiento visual en el entorno de taller/laboratorio.

## Titulaciones recomendadas

- Grado en Ingeniería Electrónica, Robótica y Mecatrónica (GIERM).
- Grado en Ingeniería Electrónica Industrial (GIEI).
- Grado en Ingeniería en Tecnologías Industriales (GITI).

## Conocimientos recomendados

Se valorarán conocimientos en:

- visión artificial y fundamentos de realidad aumentada (ARCore / AR Foundation);
- comunicaciones mediante el protocolo MQTT;
- programación de PLCs en TwinCAT 3;
- desarrollo de aplicaciones móviles (Android con Kotlin/Java o C# en Unity).

## Software

`Android Studio / Unity` `ARCore / AR Foundation` `OpenCV` `Mosquitto MQTT` `TwinCAT 3`

## Hardware

- Dispositivo móvil o tableta Android compatible con ARCore y cámara HD.
- Estaciones del sistema SMC FMS-200.
- PLC Beckhoff con interfaz Ethernet.
- Punto de acceso o router Wi-Fi.

<div class="project-contact" markdown>

### ¿Te interesa?

Si tienes interés en este trabajo, contáctame por <a href="mailto:famoreno@uma.es?Subject=Interés%20en%20TFE">correo electrónico</a> para comentar el proyecto y valorar su adecuación a tu perfil.

</div>
