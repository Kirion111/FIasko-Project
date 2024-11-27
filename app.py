from flask import Flask, render_template, request, redirect, url_for
from utils import calcular_calorias, registrar_peso, obtener_historial_peso

app = Flask(__name__)

@app.route('/')
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
    
    return render_template('calculadora.html', resultado=resultado)

@app.route('/registro_peso', methods=['GET', 'POST'])
def registro_peso():
    """Página de registro de peso"""
    historial = obtener_historial_peso()
    
    if request.method == 'POST':
        peso = float(request.form['peso'])
        registrar_peso(peso)
        return redirect(url_for('registro_peso'))
    
    return render_template('registro_peso.html', historial=historial)

if __name__ == '__main__':
    app.run(debug=True) 