# 🚀 Primer Proyecto Flask – Lógica Básica
Este es un proyecto básico en **Flask (Python)** enfocado en aprender **lógica de programación aplicada a la web**, usando rutas, formularios y validaciones simples.
El proyecto solicita un nombre y un saludo, valida si el nombre está permitido y muestra una respuesta en pantalla.
---
## 📋 Requisitos
Antes de empezar, asegúrate de tener instalado:
* Python **3.10 o superior**
* Git
* Visual Studio Code
* Navegador web (Chrome, Edge, Firefox, etc.)
Para verificar Python:
```bash
python --version
```
---

## 📁 Estructura del proyecto
```
flaskprimerproyecto/
│
├─ app.py
├─ README.md
├─ static/
│   └─ css/
│       └─ estilos.css
└─ templates/
    └─ saludo.html
```
---
## ⬇️ Clonar el repositorio
Desde la terminal (o Git Bash):
```bash
git clone https://github.com/hdce1819/flaskprimerproyecto.git
cd flaskprimerproyecto
```
Abrir el proyecto en VS Code:
```bash
code .
```
---
## 🧪 Crear entorno virtual (recomendado)
```bash
python -m venv venv
```
Activar el entorno:
### Windows
```bash
venv\Scripts\activate
```
### macOS / Linux
```bash
source venv/bin/activate
```
---
## 📦 Instalar dependencias
Instalar Flask:
```bash
pip install flask
```
(Opcional) Guardar dependencias:
```bash
pip freeze > requirements.txt
```
---
## ▶️ Ejecutar el proyecto
Desde la carpeta del proyecto:
```bash
python app.py
```
Abrir en el navegador:
```
http://127.0.0.1:5000
```
---
## 🧠 Lógica del proyecto
* Se reciben datos desde un formulario HTML
* Se valida el nombre contra una lista permitida:
  * `dany`
  * `hesiquio`
  * `esteban`
* Si el nombre está permitido, se muestra el saludo
* Si no, se muestra: **"No te conozco"**
Toda la lógica está separada del HTML y se maneja en funciones Python.
---
## 🛠 Tecnologías usadas
* Python
* Flask
* HTML
* CSS
* Git & GitHub
---
## 📌 Objetivo del proyecto
Este proyecto está diseñado para:
* Practicar **lógica de programación**
* Entender cómo Flask conecta backend y frontend
* Aprender estructura básica de proyectos web en Python
* Usar Git y GitHub desde consola
---
## 👤 Autor
**Héctor Espinosa**
Proyecto educativo para aprendizaje de programación y desarrollo web.
---
Si quieres, en el siguiente paso podemos:
* agregar `requirements.txt`
* mejorar el README con capturas
* explicar cómo hacer cambios y subir nuevos commits
* o volver directo a lógica de programación

Buen movimiento documentar el proyecto. Eso ya es mentalidad de desarrollador.
