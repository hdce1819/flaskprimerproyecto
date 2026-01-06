"""
#version 1
def saludar(nombre):
    if nombre == "dany" or nombre == "hesiquio" or nombre == "esteban":
        mensaje = input(nombre.capitalize() + " pon un saludo: ")
        return mensaje.capitalize() + " " + nombre.capitalize()
    else:
        return "No te conozco"
"""
"""
def saludar(nombre):
    nombres_permitidos = ["dany", "hesiquio", "esteban"]
    if nombre in nombres_permitidos:
        nombre_mostrar = nombre.capitalize()
        mensaje = input(nombre_mostrar + " pon un saludo: ")
        return mensaje.capitalize() + " " + nombre_mostrar
    else:
        return "No te conozco"

texto = input("Nombre: ")
resultado = saludar(texto.lower())
print(resultado)
"""
from flask import Flask, render_template, request

app = Flask(__name__)

def saludar(nombre, mensaje):
    nombres_permitidos = ["dany", "hesiquio", "esteban"]

    if nombre in nombres_permitidos:
        nombre_mostrar = nombre.capitalize()
        return mensaje.capitalize() + " " + nombre_mostrar
    else:
        return "No te conozco"

@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = ""

    if request.method == "POST":
        nombre = request.form["nombre"].lower()
        mensaje = request.form["mensaje"]
        resultado = saludar(nombre, mensaje)

    return render_template("saludo.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
