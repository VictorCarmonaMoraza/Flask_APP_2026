from flask import Flask

#Creacion de instancia de Flask
app = Flask(__name__)

#Creacion de una ruta
@app.route('/')
def hello():
    return 'Hola Mundo'
