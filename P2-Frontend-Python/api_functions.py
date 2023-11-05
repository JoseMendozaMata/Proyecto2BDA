import requests

# Define the API endpoint URL
api_url = "http://localhost:3000/"

def login_collaborator(email, password):
    data = {
        "usuario": email,
        "clave": password
    }

    response = requests.get(api_url+"Users/login", json=data)
    return response

def register_collaborator(email, password):
    data = {
        "usuario": email,
        "clave": password,
        "rol": "colaborator"
    }

    response = requests.post(api_url+"Users", json=data)
    return response

def solicit_trip(nombre_completo, puesto, departamento, tipo_de_viaje, pais_destino, motivo, fecha_inicio, fecha_fin, aerolinea, precio, alojamiento, transporte):
    data = {
        "nombre_completo": nombre_completo,
        "puesto": puesto,
        "departamento": departamento,
        "tipo_de_viaje": tipo_de_viaje,
        "pais_destino": pais_destino,
        "motivo": motivo,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "aerolinea": aerolinea,
        "precio": precio,
        "alojamiento": alojamiento,
        "transporte": transporte
    }

    response = requests.post(api_url, json=data)
    return response