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
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
    else:
        # Fórmula para mujeres
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)
    
    # Calculando IMC (Índice de Masa Corporal)
    altura_metros = altura / 100
    imc = peso / (altura_metros ** 2)
    
    # Categorías de IMC
    if imc < 18.5:
        estado_peso = "Bajo peso"
        recomendacion = "Debes aumentar de peso. Consume más calorías y realiza entrenamiento de fuerza."
    elif 18.5 <= imc < 24.9:
        estado_peso = "Peso normal"
        recomendacion = "Mantén tu dieta y actividad física actual."
    elif 25 <= imc < 29.9:
        estado_peso = "Sobrepeso"
        recomendacion = "Debes bajar de peso. Reduce calorías y aumenta actividad física."
    else:
        estado_peso = "Obesidad"
        recomendacion = "Consulta a un profesional de la salud para un plan de pérdida de peso."
    
    # Calorías diarias recomendadas (nivel de actividad moderada)
    calorias_diarias = tmb * 1.55
    
    return {
        'tmb': round(tmb, 2),
        'calorias_diarias': round(calorias_diarias, 2),
        'imc': round(imc, 2),
        'estado_peso': estado_peso,
        'recomendacion': recomendacion
    }

def registrar_peso(peso):
    """
    Registra el peso en un archivo CSV.
    
    Args:
        peso (float): Peso a registrar
    
    Returns:
        bool: True si se registró correctamente
    """
    try:
        # Intentar cargar el CSV existente
        try:
            df = pd.read_csv('datos/registro_peso.csv')
        except FileNotFoundError:
            # Si no existe, crear uno nuevo
            df = pd.DataFrame(columns=['Fecha', 'Peso'])
        
        # Añadir nuevo registro con fecha actual
        nuevo_registro = pd.DataFrame({
            'Fecha': [pd.Timestamp.now().strftime('%Y-%m-%d')],
            'Peso': [peso]
        })
        
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