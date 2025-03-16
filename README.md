# Taller 3. NLP - Servicio Web de Traducción con Flask y Hugging Face
##### Nombre: Vinicio Salcedo

## Requisitos Previos

Antes de ejecutar `app.py`, se debe tener instaladas las siguientes dependencias:

- Python >=3.9
- Las librerías listadas en `requirements.txt`

Se puede instalar las dependencias ejecutando:
```bash
pip install -r requirements.txt
```

## Ejecución Local

Para ejecutar la aplicación, se puede abrir una terminal y navegar al directorio donde se encuentra `app.py`. Luego, ejecutar el siguiente comando:
```bash
python app.py
```

### Uso

Una vez que la aplicación esté en funcionamiento, se puede acceder a ella a través de un navegador web. La URL por defecto es `http://
localhost:8080/`. Dentro del cual se puede visualizar un formulario para ingresar texto y el botón para traducirlo.

![alt text](image.png)

Finalmente se debe ingresar el texto en el campo de texto y hacer clic en el botón "Traducir". La traducción se mostrará en la parte inferior de la página.

![alt text](image-1.png)

## Ejecución en la nube

### Google Cloud Run

- Para asegurar la instalación en Google cloud primero se debe subir el código a un repositorio de GitHub. 

    El repositorio de GitHub se puede encontrar en el siguiente enlace: [GitHub](https://github.com/VinicioStalin-27/vsp_translator.git)

- Se va a realizar una instalación en Docker, así que se necesita un archivo Dockerfile dentro del repositorio.


- Luego se debe ingresar a Google Cloud y seleccionar la opción de Cloud Run / Deploy Container / Service.
![alt text](image-3.png)

- Como se va a usar Github, es necesario seleccionar la opción de Continous Deployment y seleccionar el repositorio.
![alt text](image-4.png)

- Luego debemos poner el nombre del servicio, la región, el puerto 8080 y memoria suficiente para el servicio.
![alt text](image-5.png)

- Finalmente se debe hacer clic en Crear y esperar a que se despliegue el servicio.
![alt text](image-7.png)

- Una vez que el servicio esté desplegado, se puede acceder a él a través de la URL proporcionada por Google Cloud [URL](https://vsp-translator-975558047330.us-central1.run.app/).
![alt text](image-8.png)


