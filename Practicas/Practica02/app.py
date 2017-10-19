# -*- coding: utf-8 -*-

from flask import Flask
from flask import Response,request
from flask import send_file
from mandelbrot import renderizaMandelbrot
import random


app = Flask(__name__)

@app.route('/')                         # decorador, varia los parametros
def hello_world():                      # I/O de la función
    return '¡Hola Mundo!'


#Parte 1 practica
@app.route('/imagen')
def obten_imagen():
    return send_file("./static/dado.png",mimetype="image/png")

#Parte 2 practica
@app.route('/user/<usuario>')
def saluda_usuario(usuario):
    return "Hola " + usuario + " !"

#Parte 3 practica
@app.route('/mandelbrot', methods=['GET', 'POST'])
def genera_mandelbrot():
    if request.method == 'POST':

        x1 = request.form['x1']
        y1 = request.form['y1']
        x2 = request.form['x2']
        y2 = request.form['y2']
        ancho = request.form['ancho']

        iteraciones = 1000
        nombreFicheroPNG = "./static/mandel.png"

        renderizaMandelbrot(float(x1), float(y1), float(x2), float(y2), int(ancho), int(iteraciones), nombreFicheroPNG)

        return send_file("./static/mandel.png",mimetype="image/png")

    else:

        return '''
            <form action="/mandelbrot" method="post">
                <p>X1: <input type="text" name="x1"/></p>
                <p>Y1: <input type="text" name="y1"/></p>
                <p>X2: <input type="text" name="x2"/></p>
                <p>Y2: <input type="text" name="y2"/></p>
                <p>Ancho: <input type="text" name="ancho"/></p>
                <p><input type="submit" value="Enviar datos"/></p>
            </form>
        '''



#Para nota 2
@app.route('/svg')
def genera_svg():
    sol = '''
    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">
            '''

    selection = random.randint(0,3)

    if selection == 0 :
        sol = sol + '''<rect x="50" y="50" width="150" height="50" style="fill:#ff0000" />'''
    elif selection == 1:
        sol = sol + '''<circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />'''
    elif selection == 2:
        sol = sol + '''<ellipse cx="200" cy="80" rx="100" ry="50" style="fill:yellow;stroke:purple;stroke-width:2" />'''
    elif selection == 3:
        sol = sol + '''<polygon points="200,10 250,190 160,210" style="fill:lime;stroke:purple;stroke-width:1" />'''
           
    sol = sol + "</svg>"
    return sol

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
