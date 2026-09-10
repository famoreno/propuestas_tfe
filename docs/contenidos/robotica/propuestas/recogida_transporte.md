# Sistema de recogida, transporte y entrega de paquetes con robot móvil

## Descripción

El objetivo general de este proyecto es el desarrollo e integración de un sistema completo de transporte e intralogística de última milla utilizando una plataforma robótica móvil autónoma preexistente. El robot debe desplazarse de forma autónoma hasta una ubicación de recogida, recibir un paquete dentro de un compartimento dotado de un mecanismo de cierre electromecánico, transportarlo esquivando obstáculos hasta el punto de entrega especificado y permitir la apertura controlada del compartimento tras la autenticación del destinatario (mediante lectura de código QR, reconocimiento facial o comandos de voz).

## Objetivos

- Configuración e implementación de la navegación autónoma en la base móvil (localización con Nav2/ROS2).
- Integración mecatrónica del compartimento de carga y su sistema de bloqueo/desbloqueo electrónico.
- Desarrollo de la arquitectura de comunicación mediante protocolo MQTT para la asignación y monitorización de misiones.
- Implementación del módulo de autenticación del usuario destinatario (visión artificial para QR/caras y/o interacción por habla).
- Validación experimental del ciclo completo de recogida, transporte y entrega en un entorno controlado de laboratorio.

## Grados

- GIERM, GIEI y GITI.

## Conocimientos previos

ROS2 (Robot Operating System 2), programación en Python y/o C++, navegación autónoma de robots móviles, gestión de códigos QR, protocolos de comunicación (MQTT), conocimientos básicos de visión artificial y sistemas de reconocimiento facial/de habla.

## Software

ROS2 (Humble/Jazzy), OpenCV / OpenCV-Python, Mosquitto MQTT Broker, librerías de IA/reconocimiento (e.g., `face_recognition`, Whisper/Vosk), Sistema Operativo Linux (Ubuntu 22.04/24.04 LTS).

## Hardware

Plataforma robótica móvil preexistente (con LiDAR y encoders), compartimento con cerradura/actuador electromecánico, controlador de cerradura (ESP32 / Arduino / Raspberry Pi), cámara RGB / RGB-D, micrófono y altavoz.
