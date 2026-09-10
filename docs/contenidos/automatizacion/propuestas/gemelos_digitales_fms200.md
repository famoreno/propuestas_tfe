# Gemelos Digitales en Godot de las estaciones del sistema FMS-200

## Descripción

Este TFG tiene como finalidad el diseño, desarrollo e implementación de Gemelos Digitales (*Digital Twins*) interactivos en tiempo real para las estaciones del [sistema modular de fabricación flexible SMC FMS-200](../../../pdf/FMS_200_Descripcion_Funcional.pdf). Utilizando el motor gráfico Godot Engine y modelos 3D creados en FreeCAD, se construirá una representación tridimensional cinemática del sistema. El entorno virtual se comunicará bidireccionalmente con el PLC físico mediante Beckhoff TwinCAT 3, permitiendo reflejar el estado real de la planta, simular secuencias de control y realizar validaciones sin riesgo para el equipamiento físico.

## Objetivos

- Modelado y simplificación CAD 3D de los componentes mecánicos de las estaciones FMS-200 utilizando FreeCAD.
- Estructuración de la escena y programación de la lógica de animación cinemática e interactividad en Godot Engine.
- Implementación de la pasarela de comunicación en tiempo real entre Godot y TwinCAT 3 (vía protocolo ADS).
- Sincronización bidireccional de señales de E/S (sensores y actuadores) entre el PLC físico y el modelo 3D.
- Ensayos de validación del Gemelo Digital mediante la ejecución de rutinas completas de automatización.

## Grados

- GIERM, GIEI y GITI.

## Conocimientos previos

Programación estructurada / orientada a objetos (GDScript en Godot o C#), programación de PLCs en TwinCAT 3 (lenguajes IEC 61131-3), diseño y modelado 3D paramétrico con FreeCAD, fundamentos de comunicaciones industriales.

## Software

Godot Engine (v4.x), Beckhoff TwinCAT 3, FreeCAD (y/o Blender para optimización de mallas), conectores de comunicación ADS.

## Hardware

Estaciones de fabricación flexible SMC FMS-200, PLC / Controlador industrial Beckhoff (o PC de control compatible), equipo informático para diseño 3D.
