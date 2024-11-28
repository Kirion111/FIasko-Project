from flask import Flask, render_template, request, redirect, url_for
from utils import calcular_calorias, registrar_peso, obtener_historial_peso,guardar_resultados_calculadora
import subprocess as sp
import csv
import os
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def login():
    """Login"""
    return render_template('login.html')

@app.route('/index')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    """Página de calculadora de calorías"""
    resultado = None
    
    if request.method == 'POST':
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        edad = int(request.form['edad'])
        sexo = request.form['sexo']
        resultado = calcular_calorias(peso, altura, edad, sexo)
        guardar_resultados_calculadora(resultado)
    
    return render_template('calculadora.html', resultado=resultado)

@app.route('/registro_peso', methods=['GET', 'POST'])
def registro_peso():
    """Página de registro de peso"""
    historial = obtener_historial_peso()
    
    if request.method == 'POST':
        peso = float(request.form['peso'])
        cals = float(request.form['calorias'])
        registrar_peso(peso, cals)
        return render_template('registro_peso.php', historial=historial)
    
    return render_template('registro_peso.php', historial=historial)

if __name__ == '__main__':
    app.run(debug=True) 

@app.route('/crear_rutina', methods=['GET', 'POST'])
def crear_rutina_csv():
    """Gestión de rutinas almacenadas en un archivo CSV."""
    archivo_csv = 'datos/rutinas.csv'

    if request.method == 'POST':
        dia = request.form['dia']
        ejercicio = request.form['ejercicio']
        repeticiones = int(request.form['repeticiones'])
        peso = float(request.form['peso'])

        # Crear el archivo si no existe
        if not os.path.exists(archivo_csv):
            with open(archivo_csv, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Día', 'Ejercicio', 'Repeticiones', 'Peso'])  # Cabeceras

        # Guardar la nueva rutina en el archivo CSV
        with open(archivo_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([dia, ejercicio, repeticiones, peso])

    # Leer las rutinas existentes del archivo CSV
    rutinas = []
    if os.path.exists(archivo_csv):
        with open(archivo_csv, mode='r') as file:
            reader = csv.DictReader(file)
            rutinas = list(reader)

    return render_template('rutina.html', rutinas=rutinas)