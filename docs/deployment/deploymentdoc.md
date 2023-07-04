# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** el modelo se llama 'plant_pathology.pkl'
- **Plataforma de despliegue:** Por medio de un servicio REST API a traves de la plataforma FastAPI de python.
- **Requisitos técnicos:** El primer requisito pero que no es obligatorio es a nivel de hardware y tiene que ver con la GPU, el despliegue de la imagen de docker utiliza la libreria CUDA para poder ejecutar el modelo por GPU para optimizar sus consultas. Un ejemplo es si el modelo es llamado desde CPU con una imagen de 300*300 pixeles, su analisis dura aproximadamente 8 a 40 segundos. Si se realiza este llamado desde GPU se demora entre 10 y 900 milisegundos
- **Requisitos de seguridad:** No aplica para el proyecto. Pero en futura versiones se utilizara llamados por json web token y authenticacion
- **Diagrama de arquitectura:**El diagrama de la arquitectura se muestra en la siguiente imagen
![Validation](images/arquitectura.png)

## Código de despliegue

- **Archivo principal:** El archivo principal es el archivo dockerfile que crea una imagen de docker e importa el modelo para su uso a traves de FastAPI
- **Rutas de acceso a los archivos:**  en la ruta src se encuentra una carpeta llamada plant_pathology donde se encuentra los archivos README.md y Dockerfile, tambien dos carpetas, una llamada model con el archivo plant_pathology.pkl y otra carpeta llamada app con el archivo main.py que contiene el despliegue de fastAPI
- **Variables de entorno:** No se utiliza para este despliegue variables de entorno aparte de las detalladas en el archivo README.md

## Documentación del despliegue

- **Instrucciones de instalación:** Se debe clonar el repositorio y luego desde la carpeta src/plant_pathology ejecutar como lo explica el archivo README.md
- **Instrucciones de configuración:** Para poder probar el repositorio es necesario tener instalado docker y python 3.6+, ademas de Librerías numpy, scikit-learn, fastapi, uvicorn y requests.
- **Instrucciones de uso:** Para realizar el despliegue para la prueba se debe realizar
git clone https://github.com/byjimmymoto/MLDS6project.git
cd src/plant_pathology
docker build -t api_test .
docker run -d --name api_docker -p 8000:80 api_test

- **Instrucciones de mantenimiento:**  en caso de falla se debe utilizar el siguiente comando ingresando a la imagen docker
uvicorn main:app --reload