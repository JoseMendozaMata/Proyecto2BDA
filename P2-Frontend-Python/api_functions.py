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

def register_administrador(email, password):
    data = {
        "usuario": email,
        "clave": password,
        "rol": "Admin"
    }

    response = requests.post(api_url+"Users", json=data)
    return response

def solicit_trip(usr_id, trip_data):
    
    print("url ", api_url+"flights/"+usr_id)
    response = requests.post(api_url+"flights/"+usr_id, json=trip_data)
    return response

def delete_trip(trip_id, usr_id):
    data = {
        "id_colaborador": usr_id,
        "id_vuelo": trip_id
    }
    response = requests.delete(api_url+"flights/"+trip_id, json=data)
    return response

def get_trip(usr_id):
    response = requests.get(api_url+"flights/getCollaboratorFlights/"+usr_id)
    return response
def update_trip(trip_id, trip_data):
    response = requests.patch(api_url+"flights/"+trip_id, json=trip_data)
    return response

def get_pending_trips(user_id):
    response = requests.get(api_url+"flights/getPendingFlights/"+user_id)
    return response

def approve_flight(flight_id, user_id):
    response = requests.post(api_url+"flights/approveFlight/"+flight_id+"/"+user_id)
    return response

def reject_flight(flight_id, user_id):
    response = requests.post(api_url+"flights/rejectFlight/"+flight_id+"/"+user_id)
    return response

def get_flights_by_month(user_id ,month, year):
    response = requests.get(api_url+"flights/getProgrammedFlights/"+user_id+"/"+month+"/"+year)
    return response

# international flights are sorted by trimester
def get_international_flights(user_id, trimester, year):
    response = requests.get(api_url+"flights/getInternationalFlights/"+user_id+"/"+trimester+"/"+year)
    return response

def get_flights_by_destination(user_id, destination):
    response = requests.get(api_url+"flights/getDestinyFlights/"+user_id+"/"+destination)
    return response