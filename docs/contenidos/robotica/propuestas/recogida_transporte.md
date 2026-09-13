---
title: Robot móvil autónomo para servicios de intralogística y entrega inteligente
order: 1
type: TFG
status: disponible
keywords:
  - ROS 2
  - Programación
  - Navegación
  - Visión artificial
  - MQTT
  - Arduino
summary: Robot móvil autónomo capaz de recoger, transportar y entregar paquetes de forma segura tras autenticar al destinatario.
---

# {{ title }} {.project-title}

{{ project_header() }}

## Descripción

El objetivo general de este proyecto es el desarrollo e integración de un sistema completo de transporte e intralogística de última milla utilizando una plataforma robótica móvil autónoma preexistente. El robot debe desplazarse de forma autónoma hasta una ubicación de recogida, recibir un paquete dentro de un compartimento dotado de un mecanismo de cierre electromecánico, transportarlo esquivando obstáculos hasta el punto de entrega especificado y permitir la apertura controlada del compartimento tras la autenticación del destinatario (mediante lectura de código QR, reconocimiento facial o comandos de voz).

## Objetivos

- Configuración e implementación de la navegación autónoma en la base móvil (localización con Nav2/ROS2).
- Integración mecatrónica del compartimento de carga y su sistema de bloqueo/desbloqueo electrónico.
- Desarrollo de la arquitectura de comunicación mediante protocolo MQTT para la asignación y monitorización de misiones.
- Implementación del módulo de autenticación del usuario destinatario (visión artificial para QR/caras y/o interacción por habla).
- Validación experimental del ciclo completo de recogida, transporte y entrega en un entorno controlado de laboratorio.

## Titulaciones recomendadas

- Grado en Ingeniería Electrónica, Robótica y Mecatrónica (GIERM).
- Grado en Ingeniería Electrónica Industrial (GIEI).
- Grado en Ingeniería en Tecnologías Industriales (GITI).

## Conocimientos recomendados

Se valorarán conocimientos en:

- ROS 2;
- programación en Python y/o C++;
- navegación autónoma de robots móviles;
- gestión de códigos QR;
- protocolos de comunicación (MQTT);
- visión artificial;
- reconocimiento facial y/o de habla.

## Software

`Ubuntu Linux` `ROS 2` `OpenCV` `Mosquitto MQTT Broker` `Whisper` `face_recognition`

## Hardware

- Plataforma robótica móvil preexistente (con LiDAR y encoders)
- Compartimento con cerradura/actuador electromecánico
- Controlador de cerradura (ESP32 / Arduino / Raspberry Pi)
- Cámara RGB / RGB-D
- Micrófono y altavoz.

<div class="project-contact" markdown>

### ¿Te interesa?

Si tienes interés en este trabajo, contáctame por <a href="mailto:famoreno@uma.es?Subject=Interés%20en%20TFE">correo electrónico</a> para comentar el proyecto y valorar su adecuación a tu perfil.

</div>
