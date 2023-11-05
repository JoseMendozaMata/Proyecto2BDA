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
        "rol": "Colaborador"
    }

    response = requests.post(api_url+"Users", json=data)
    return response

def solicit_trip(usr_id, trip_data):
    
    print("url ", api_url+"flights/"+usr_id)
    response = requests.post(api_url+"flights/"+usr_id, json=trip_data)
    return response

def delete_trip(usr_id, trip_data):
    response = requests.patch(api_url+"flights/"+usr_id, json=trip_data)
    return response

def get_trip(usr_id):
    response = requests.get(api_url+"flights/getCollaboratorFlights/"+usr_id)
    return response
def update_trip(trip_id, trip_data):
    response = requests.patch(api_url+"flights/"+trip_id, json=trip_data)
    return response
#def delete_trip(id_colaborador, id_vuelo, )