# Realidad Aumentada para monitorización de datos de estaciones FMS-200 en dispositivos móviles

## Descripción

El proyecto aborda la creación de un sistema de supervisión en planta basado en Realidad Aumentada (RA) para dispositivos móviles (smartphones o tablets Android). La aplicación permitirá a los operadores o estudiantes apuntar con la cámara hacia una estación FMS-200 y visualizar, superpuestos en la imagen real, paneles interactivos con información telemétrica en tiempo real (estados de actuadores, sensores, contadores, alarmas y variables internas del PLC). El flujo de datos se estructurará mediante publicaciones MQTT desde TwinCAT 3 hacia la aplicación móvil.

## Objetivos

- Configuración del módulo de comunicación MQTT en TwinCAT 3 para la publicación periódica del estado de la estación.
- Desarrollo de la aplicación móvil nativa Android o en motor con soporte AR (ARCore / Unity AR Foundation).
- Integración de algoritmos de visión artificial / marcadores para el reconocimiento y posicionamiento espacial 3D sobre la estación FMS-200.
- Diseño de una interfaz HMI inmersiva e intuitiva para la representación de datos de telemetría en tiempo real.
- Evaluación de latencias, consumo de recursos y precisión del seguimiento visual en el entorno de taller/laboratorio.

## Grados

- GIERM, GIEI y GITI.

## Conocimientos previos

Visión artificial y fundamentos de Realidad Aumentada (ARCore / AR Foundation), comunicaciones por protocolo MQTT, programación de PLCs en TwinCAT 3, desarrollo de aplicaciones móviles (Android con Kotlin/Java o C# en Unity).

## Software

Android Studio (o Unity con SDK ARCore), OpenCV, Broker MQTT (Mosquitto), Beckhoff TwinCAT 3 (módulo TF6701 MQTT / ADS).

## Hardware

Dispositivo móvil / Tablet Android compatible con ARCore y cámara HD, estaciones del sistema SMC FMS-200, PLC Beckhoff con interfaz Ethernet, punto de acceso / router Wi-Fi.
