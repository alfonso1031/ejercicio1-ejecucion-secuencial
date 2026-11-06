# Ejercicio 1: Ejecución secuencial

Este ejemplo muestra la preparación cotidiana de un desayuno. Primero se prepara
el café, después se tuesta el pan y al final se cocinan los huevos. Cada tarea
empieza cuando termina la anterior.

## Requisitos

- Docker
- Docker Compose v2 (incluido en Docker Desktop)

## Ejecutar con Docker Compose

Desde la carpeta raíz del repositorio, ejecuta:

    docker compose up --build

Verás cada tarea comenzar y terminar en orden. Al acabar, Compose detendrá el
contenedor. El tiempo total es aproximadamente seis segundos.

## Archivos

- main.py: ejecuta las tres tareas una detrás de otra.
- Dockerfile: construye la imagen de Python.
- compose.yaml: permite iniciar el ejemplo con Docker Compose.
