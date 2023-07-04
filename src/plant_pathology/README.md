# Contenido

En este repositorio vamos a:

  1. Desplegar un repositorio REST API con una llamada POST a traves de FastAPI
  
  2. Utilizar un modelo previamente creado en formato pickle
  
  3. Construir una API con FastAPI
  
  4. Desplegar la API usando un contendor de Docker


# Requisitos

 * Python 3.6+

 * Librerías `numpy`, `scikit-learn`, `fastapi`, `uvicorn` y `requests`

 * [Docker](https://docs.docker.com/get-docker/) 

# Instrucciones

```
git clone https://github.com/byjimmymoto/MLDS6project.git
cd src/plant_pathology
docker build -t api_test .
docker run -d --name api_docker -p 8000:80 api_test
```

# Ejercutar FastAPI

`uvicorn main:app --reload`

# Referencias

 * [Introducción a Docker](https://docs.docker.com/get-started/)
 * [FastAPI. Deployment](https://fastapi.tiangolo.com/deployment/)
 * [FastAPI. Imágenes de Docker oficiales](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)