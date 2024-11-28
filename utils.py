import pandas as pd
import math

def calcular_calorias(peso, altura, edad, sexo='masculino'):
    """
    Calcula las calorías necesarias basadas en el peso, altura, edad y sexo.
    
    Args:
        peso (float): Peso en kilogramos
        altura (float): Altura en centímetros
        edad (int): Edad en años
        sexo (str): 'masculino' o 'femenino'
    
    Returns:
        dict: Diccionario con información de calorías y recomendaciones
    """
    # Fórmula de Harris-Benedict para calcular metabolismo basal
    if sexo == 'masculino':
        # Fórmula para hombres
        tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
    else:
        # Fórmula para mujeres
        tmb = (10 * peso) + (6.25 * altura) - (5 * edad) - 161
    
    # Calculando IMC (Índice de Masa Corporal)
    altura_metros = altura / 100
    imc = peso / (altura_metros ** 2)
    
    # Categorías de IMC
    if imc < 18.5:
        estado_peso = "Bajo peso"
        recomendacion = "Superhabit Calorico. Consume más calorías (+300kcal) y realiza entrenamiento de fuerza."
    elif 18.5 <= imc < 24.9:
        estado_peso = "Peso normal"
        recomendacion = "Mantenimiento. Mantén tu dieta y actividad física actual."
    elif 25 <= imc < 29.9:
        estado_peso = "Sobrepeso"
        recomendacion = "Déficit Calorico. Reduce calorías (-300kcal) y aumenta actividad física."
    else:
        estado_peso = "Obesidad"
        recomendacion = "Déficit calorico. Reduce calorías (-500kcal) y consulta a un profesional de la salud para un plan de pérdida de peso."
    
    # Calorías diarias recomendadas (nivel de actividad moderada)
    calorias_diarias = tmb * 1.55
    
    return {
        'tmb': round(tmb, 2),
        'calorias_diarias': round(calorias_diarias, 2),
        'imc': round(imc, 2),
        'estado_peso': estado_peso,
        'recomendacion': recomendacion,
        'peso': peso,
        'altura': altura,
        'genero': sexo,
        'edad': edad,
    }

def registrar_peso(peso, cals):
    """
    Registra el peso en un archivo CSV.
    
    Args:
        peso (float): Peso a registrar
    
    Returns:
        bool: True si se registró correctamente
    """
    try:
        # Añadir nuevo registro con fecha actual
        nuevo_registro = pd.DataFrame({
            'Fecha': [pd.Timestamp.now().strftime('%Y-%m-%d')],
            'Peso': [peso],
            'calorias_diarias': [cals]
        })
        # Intentar cargar el CSV existente
        try:
            df = pd.read_csv('datos/registro_peso.csv')
        except FileNotFoundError:
            # Si no existe, crear uno nuevo
            df = pd.DataFrame(columns=['Calorias Diarias','Fecha', 'Peso'])
        
        df = pd.concat([df, nuevo_registro], ignore_index=True)
        
        # Guardar el DataFrame
        df.to_csv('datos/registro_peso.csv', index=False)
        return True
    except Exception as e:
        print(f"Error al registrar peso: {e}")
        return False

def obtener_historial_peso():
    """
    Obtiene el historial de peso registrado.
    
    Returns:
        list: Lista de registros de peso
    """
    try:
        df = pd.read_csv('datos/registro_peso.csv')
        return df.to_dict('records')
    except FileNotFoundError:
        return []


def guardar_resultados_calculadora(resultado):
    """
    Sobrescribe los resultados de la calculadora en un archivo CSV con campos personalizados.
    Si el archivo no existe, lo crea automáticamente.
    
    Args:
        resultado (dict): Diccionario con los resultados calculados.
    """
    try:
        # Crear un DataFrame con los campos especificados
        nuevo_registro = pd.DataFrame({
            'Calorías Recomendadas': [resultado['calorias_diarias']],
            'Peso Actual': [resultado['peso']],
            'Altura': [resultado['altura']],
            'Género': [resultado['genero']],
            'Edad': [resultado['edad']],
            'Plan Alimenticio': [resultado['recomendacion']],
            'TMB': [resultado['tmb']],
            'IMC': [resultado['imc']],
            'Estado de Peso': [resultado['estado_peso']]
        })

        # Sobrescribir el archivo CSV, creándolo si no existe
        columnas = [
            'Calorías Recomendadas', 
            'Peso Actual', 
            'Altura', 
            'Género', 
            'Edad', 
            'Plan Alimenticio', 
            'TMB', 
            'IMC', 
            'Estado de Peso'
        ]
        try:
            # Intentar leer el archivo para validar su existencia
            _ = pd.read_csv('datos/resultados_calculadora.csv')
        except FileNotFoundError:
            # Crear un archivo vacío con las columnas requeridas si no existe
            pd.DataFrame(columns=columnas).to_csv('datos/resultados_calculadora.csv', index=False)

        # Sobrescribir los datos con el nuevo registro
        nuevo_registro.to_csv('datos/resultados_calculadora.csv', index=False)
    except Exception as e:
        print(f"Error al guardar los resultados: {e}")
