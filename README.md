# Nombre del Proyecto: API Rest Academia Virtual [GRV-Academy]

[![Licencia](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Lenguaje](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Framework Backend](https://img.shields.io/badge/Backend-Django%20REST%20Framework-green.svg)](https://www.django-rest-framework.org/)
[![Base de Datos](https://img.shields.io/badge/Database-PostgreSQL-blueviolet.svg)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Containerized-Docker-informational.svg)](https://www.docker.com/)
[![Estado](https://img.shields.io/badge/Status-Development-orange.svg)](https://shields.io/)

> Una API Rest robusta construida con Django y Django REST Framework, diseñada para una plataforma de educación a distancia al estilo Coursera/Udemy, ofreciendo diversos cursos con certificación. **La aplicación está configurada para ejecutarse en contenedores Docker**, utilizando **PostgreSQL como su base de datos principal, elegida por su robustez y fiabilidad.**

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Características Principales](#características-principales)
- [Requisitos Técnicos](#requisitos-técnicos)
- [Instalación](#instalación)
- [Endpoints de la API](#endpoints-de-la-api)
- [Autenticación](#autenticación)
- [Certificados](#certificados)
- [Próximamente: Frontend (Vite + Vue.js)](#próximamente-frontend-vite--vuejs)
- [Contribución](#contribución)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Descripción del Proyecto

Esta API Rest proporciona la base para una plataforma de academia virtual de educación a distancia. Permite a los usuarios explorar cursos, registrarse, acceder al contenido, realizar evaluaciones y obtener certificados al completar los cursos. **La API está desarrollada con Django y Django REST Framework para el backend, asegurando una arquitectura escalable y mantenible. Se ha optado por PostgreSQL como sistema de gestión de base de datos debido a su solidez y características avanzadas.** La configuración del proyecto incluye la **contenerización con Docker**, facilitando la implementación y el desarrollo en diferentes entornos.

## Requisitos Técnicos

Asegúrate de tener instalado lo siguiente para ejecutar esta API en un entorno de desarrollo:

* [Python 3.x](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing/) (se instala con Python)
* [Django](https://www.djangoproject.com/download/) (versión mínima recomendada: 4.x)
* [Django REST Framework](https://www.django-rest-framework.org/) (versión mínima recomendada: 3.x)
* **[PostgreSQL](https://www.postgresql.org/)** (sistema de gestión de base de datos)
* [Redis](https://redis.io/) (opcional, para caché y tareas asíncronas)
* **[Docker](https://www.docker.com/)** y **[Docker Compose](https://docs.docker.com/compose/install/)** (para la contenerización y gestión de servicios)

## Instalación

Sigue estos pasos para configurar la API en tu entorno local:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/tu-repositorio-api.git](https://github.com/tu-usuario/tu-repositorio-api.git)
    cd tu-repositorio-api/backend
    ```

2.  **Configuración con Docker (Recomendado):**
    Si tienes Docker y Docker Compose instalados, puedes levantar la API y su base de datos PostgreSQL con el siguiente comando desde el directorio `backend`:
    ```bash
    docker compose up --build
    ```
    Consulta el archivo `docker-compose.yaml` para más detalles sobre la configuración de los contenedores.

3.  **Configuración Manual (sin Docker):**
    * '''
    * El entorno virtual no es necesario, ya que el archivo dockerfile esta estructurado para no depender de un entorno virtual
      '''
    * **Instala las dependencias:**
      ```bash
      pip install -r requirements.txt
      ```
    * **Configura la base de datos:**
      * Asegúrate de tener PostgreSQL instalado y configurado.
      * Crea una base de datos para tu proyecto.
      * Configura las variables de entorno de la base de datos en el archivo `backend/core/settings.py` o utilizando un archivo `.env` y `django-environ` para conectar con tu instancia de PostgreSQL.
    * **Ejecuta las migraciones:**
      ```bash
      ejecutar desde docker con: docker exec -it django /bin/bash
      python manage.py migrate
      ```
    * **Crea un superusuario (administrador):**
      ```bash
      python manage.py createsuperuser
      ```
    * **Ejecuta el servidor de desarrollo:**
      ```bash
      python manage.py runserver
      ```
      ´´´ 
        La API estará disponible en `http://localhost:8000/`.
      ´´´
la configuracion de salida al navegador será http://localhost:8000
las pruebas con postman serán: http://127.0.0.1:8000  ó http://localhost:/8000
posee una pagina de prueba donde verificar en navegador http://localhost:/8000/test/
## Próximamente: Frontend (Vite + Vue.js)

La interfaz de usuario para esta plataforma de academia virtual está siendo desarrollada utilizando Vite y Vue.js. La información sobre la estructura del frontend, los componentes principales y cómo interactúa con esta API se añadirá a este README en una futura actualización. ¡Mantente atento!

[...] 
