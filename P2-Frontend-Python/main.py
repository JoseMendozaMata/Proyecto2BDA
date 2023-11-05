import tkinter as tk
from tkinter import ttk, messagebox
import api_functions
import json

global_user = "admin"
global_password = "testing"
global_id = "id"
form_data_list = []
def collaborator_screen():
    canvas.delete("all")
    for widget in canvas.winfo_children():
        widget.destroy()
    canvas.create_text(400, 100, text=f"Welcome,!", font=("Helvetica", 16))

    # Create 4 buttons
    ttk.Button(canvas, text="Nueva solicitud", command=collaborator_new_flight).place(x=300, y=150)
    ttk.Button(canvas, text="Ver historial", command=collaborator_history).place(x=300, y=200)
    ttk.Button(canvas, text="Back to login", command=main_screen).place(x=300, y=250)
def collaborator_new_flight():
    def submit_form():
        nombre_completo = entry_nombre_completo.get()
        puesto = entry_puesto.get()
        departamento = entry_departamento.get()
        tipo_de_viaje = entry_tipo_de_viaje.get()
        pais_destino = entry_pais_destino.get()
        motivo = entry_motivo.get()
        fecha_inicio = entry_fecha_inicio.get()
        fecha_fin = entry_fecha_fin.get()
        aerolinea = entry_aerolinea.get()
        precio = entry_precio.get()
        alojamiento = entry_alojamiento.get()
        transporte = entry_transporte.get()
        hora_ida = entry_hora_inicio.get()
        hora_vuelta = entry_hora_fin.get()

        
        form_data = {
                    "nombre": nombre_completo,
                    "puesto": puesto,
                    "departamento": departamento,
                    "internacional": False,
                    "pais": pais_destino,
                    "motivo": motivo,
                    "fechas": {"fecha_ida" : fecha_inicio,
                            "hora_ida" : hora_ida,
                            "fecha_vuelta": fecha_fin,
                            "hora_vuelta" : hora_vuelta
                            },
                    "details":{
                                "nombre_aerolinea": aerolinea,
                                "precio": 500},

                    "alojamiento": alojamiento,
                    "requiere_transporte": False,
                    "estado":"Pendiente"
                    
                    
                }
        response = api_functions.solicit_trip(global_id,form_data)
        print("trip form res",response)
        print("trip form number",response.status_code)
        print("trip form text", response.text)
        global form_data_list
        #form_data_list.append(form_data)
        print(form_data_list)

    new_window = tk.Toplevel()
    new_window.title("Travel Form")

    # Create and position form fields and labels
    ttk.Label(new_window, text="Nombre Completo:").grid(row=0, column=0)
    entry_nombre_completo = ttk.Entry(new_window)
    entry_nombre_completo.grid(row=0, column=1)

    ttk.Label(new_window, text="Puesto:").grid(row=1, column=0)
    entry_puesto = ttk.Entry(new_window)
    entry_puesto.grid(row=1, column=1)

    ttk.Label(new_window, text="Departamento:").grid(row=2, column=0)
    entry_departamento = ttk.Entry(new_window)
    entry_departamento.grid(row=2, column=1)

    ttk.Label(new_window, text="Tipo de Viaje:").grid(row=3, column=0)
    entry_tipo_de_viaje = ttk.Entry(new_window)
    entry_tipo_de_viaje.grid(row=3, column=1)

    ttk.Label(new_window, text="Pais Destino:").grid(row=4, column=0)
    entry_pais_destino = ttk.Entry(new_window)
    entry_pais_destino.grid(row=4, column=1)

    ttk.Label(new_window, text="Motivo:").grid(row=5, column=0)
    entry_motivo = ttk.Entry(new_window)
    entry_motivo.grid(row=5, column=1)

    ttk.Label(new_window, text="Fecha de Inicio:").grid(row=6, column=0)
    entry_fecha_inicio = ttk.Entry(new_window)
    entry_fecha_inicio.grid(row=6, column=1)

    ttk.Label(new_window, text="Hora de Inicio:").grid(row=7, column=0)
    entry_hora_inicio = ttk.Entry(new_window)
    entry_hora_inicio.grid(row=7, column=1)

    ttk.Label(new_window, text="Fecha de Fin:").grid(row=8, column=0)
    entry_fecha_fin = ttk.Entry(new_window)
    entry_fecha_fin.grid(row=8, column=1)

    ttk.Label(new_window, text="Hora de Fin:").grid(row=9, column=0)
    entry_hora_fin = ttk.Entry(new_window)
    entry_hora_fin.grid(row=9, column=1)

    ttk.Label(new_window, text="Aerolínea:").grid(row=10, column=0)
    entry_aerolinea = ttk.Entry(new_window)
    entry_aerolinea.grid(row=10, column=1)

    ttk.Label(new_window, text="Precio:").grid(row=11, column=0)
    entry_precio = ttk.Entry(new_window)
    entry_precio.grid(row=11, column=1)

    ttk.Label(new_window, text="Alojamiento:").grid(row=12, column=0)
    entry_alojamiento = ttk.Entry(new_window)
    entry_alojamiento.grid(row=12, column=1)

    ttk.Label(new_window, text="Transporte:").grid(row=13, column=0)
    entry_transporte = ttk.Entry(new_window)
    entry_transporte.grid(row=13, column=1)

    # Create and position the Submit button
    submit_button = ttk.Button(new_window, text="Submit", command=submit_form)
    submit_button.grid(row=14, column=0, columnspan=2)
def collaborator_history():
    global form_data_list
    def display_form_data():
        selected_item = form_data_listbox.curselection()
        if selected_item:
            index = selected_item[0]
            form_data = form_data_list[index]
            show_form_data_window(form_data, index)

    def show_form_data_window(form_data, index):
        new_window = tk.Toplevel()
        new_window.title("Edit Form")

        # Create and position form fields and labels
        ttk.Label(new_window, text="Nombre Completo:").grid(row=0, column=0)
        entry_nombre_completo = ttk.Entry(new_window)
        entry_nombre_completo.insert(0,form_data['nombre'])
        entry_nombre_completo.grid(row=0, column=1)

        ttk.Label(new_window, text="Puesto:").grid(row=1, column=0)
        entry_puesto = ttk.Entry(new_window)
        entry_puesto.insert(0,form_data['puesto'])
        entry_puesto.grid(row=1, column=1)

        ttk.Label(new_window, text="Departamento:").grid(row=2, column=0)
        entry_departamento = ttk.Entry(new_window)
        entry_departamento.insert(0,form_data['departamento'])
        entry_departamento.grid(row=2, column=1)

        ttk.Label(new_window, text="Tipo de Viaje:").grid(row=3, column=0)
        entry_tipo_de_viaje = ttk.Entry(new_window)
        entry_tipo_de_viaje.insert(0,form_data['internacional'])
        entry_tipo_de_viaje.grid(row=3, column=1)

        ttk.Label(new_window, text="Pais Destino:").grid(row=4, column=0)
        entry_pais_destino = ttk.Entry(new_window)
        entry_pais_destino.insert(0,form_data['pais'])
        entry_pais_destino.grid(row=4, column=1)

        ttk.Label(new_window, text="Motivo:").grid(row=5, column=0)
        entry_motivo = ttk.Entry(new_window)
        entry_motivo.insert(0,form_data['motivo'])
        entry_motivo.grid(row=5, column=1)

        ttk.Label(new_window, text="Fecha de Inicio:").grid(row=6, column=0)
        entry_fecha_inicio = ttk.Entry(new_window)
        entry_fecha_inicio.insert(0,form_data['fechas']['fecha_ida'])
        entry_fecha_inicio.grid(row=6, column=1)

        ttk.Label(new_window, text="Hora de Inicio:").grid(row=7, column=0)
        entry_hora_inicio = ttk.Entry(new_window)
        entry_hora_inicio.insert(0,form_data['fechas']['hora_ida'])
        entry_hora_inicio.grid(row=7, column=1)

        ttk.Label(new_window, text="Fecha de Fin:").grid(row=8, column=0)
        entry_fecha_fin = ttk.Entry(new_window)
        entry_fecha_fin.insert(0,form_data['fechas']['fecha_vuelta'])
        entry_fecha_fin.grid(row=8, column=1)

        ttk.Label(new_window, text="Hora de Fin:").grid(row=9, column=0)
        entry_hora_fin = ttk.Entry(new_window)
        entry_hora_fin.insert(0,form_data['fechas']['hora_vuelta'])
        entry_hora_fin.grid(row=9, column=1)

        ttk.Label(new_window, text="Aerolínea:").grid(row=10, column=0)
        entry_aerolinea = ttk.Entry(new_window)
        entry_aerolinea.insert(0,form_data['details']['nombre_aerolinea'])
        entry_aerolinea.grid(row=10, column=1)

        ttk.Label(new_window, text="Precio:").grid(row=11, column=0)
        entry_precio = ttk.Entry(new_window)
        entry_precio.insert(0,form_data['details']['precio'])
        entry_precio.grid(row=11, column=1)

        ttk.Label(new_window, text="Alojamiento:").grid(row=12, column=0)
        entry_alojamiento = ttk.Entry(new_window)
        entry_alojamiento.insert(0,form_data['alojamiento'])
        entry_alojamiento.grid(row=12, column=1)

        ttk.Label(new_window, text="Transporte:").grid(row=13, column=0)
        entry_transporte = ttk.Entry(new_window)
        entry_transporte.insert(0,form_data['requiere_transporte'])
        entry_transporte.grid(row=13, column=1)

        # Create and position the Submit button
        submit_button = ttk.Button(new_window, text="Update", command= lambda :update_form(form_data['_id']))
        submit_button.grid(row=14, column=0, columnspan=2)
        def update_form(id_vuelo):
                nombre_completo = entry_nombre_completo.get()
                puesto = entry_puesto.get()
                departamento = entry_departamento.get()
                tipo_de_viaje = entry_tipo_de_viaje.get()
                pais_destino = entry_pais_destino.get()
                motivo = entry_motivo.get()
                fecha_inicio = entry_fecha_inicio.get()
                fecha_fin = entry_fecha_fin.get()
                aerolinea = entry_aerolinea.get()
                precio = entry_precio.get()
                alojamiento = entry_alojamiento.get()
                transporte = entry_transporte.get()
                hora_ida = entry_hora_inicio.get()
                hora_vuelta = entry_hora_fin.get()

                
                form_data = {
                            "id_colaborador" : global_id,
                            "id_vuelo": id_vuelo,
                            "nombre": nombre_completo,
                            "puesto": puesto,
                            "departamento": departamento,
                            "internacional": False,
                            "pais": pais_destino,
                            "motivo": motivo,
                            "fechas": {"fecha_ida" : fecha_inicio,
                                    "hora_ida" : hora_ida,
                                    "fecha_vuelta": fecha_fin,
                                    "hora_vuelta" : hora_vuelta
                                    },
                            "details":{
                                        "nombre_aerolinea": aerolinea,
                                        "precio": 500},

                            "alojamiento": alojamiento,
                            "requiere_transporte": False,
                            "estado":"Pendiente"
                            
                            
                        }
                response = api_functions.solicit_trip(global_id,form_data)
                print("trip form res",response)
                print("trip form number",response.status_code)
                print("trip form text", response.text)
                
                #form_data_list.append(form_data)
                api_functions.update_trip(id_vuelo, form_data)
                
    def delete_form_data(index):
        global form_data_list
        form_data_list.pop(index)
        refresh_form_data_listbox()

    def refresh_form_data_listbox():
        form_data_listbox.delete(0, tk.END)  # Clear the Listbox

        # Populate the Listbox with the updated form data entries
        for i, form_data in enumerate(form_data_list):
            form_data_listbox.insert(tk.END, f"Entry {i + 1}")

    new_window = tk.Toplevel()
    new_window.title("Form Data Viewer")

    # Create a Listbox to display the stored form data
    global form_data_listbox
    form_data_listbox = tk.Listbox(new_window)
    form_data_listbox.pack()
    form_data_listbox.config(width=100) 



    # Populate the Listbox with form data entries
    response = api_functions.get_trip(global_id)
    print("REPSUESTA", response.text)
    form_data_list = json.loads(response.text)
    for i, form_data in enumerate(form_data_list):
        form_data_listbox.insert(tk.END, f"Entry {form_data['_id']}: Viaje a {form_data['pais']} el {form_data['fechas']['fecha_ida']}")

    # Create a button to display the selected form data
    display_button = ttk.Button(new_window, text="Display Selected Form Data", command=display_form_data)
    display_button.pack()

    

# Function to change the canvas content
def login_screen(user_type):
    canvas.delete("all")
    for widget in canvas.winfo_children():
        widget.destroy()
    canvas.create_text(400, 100, text=f"Login as {user_type}", font=("Helvetica", 16))
    
    # Create and position the username and password entry fields
    ttk.Label(canvas, text="Username:").place(x=300, y=150)
    entry_username = ttk.Entry(canvas)
    entry_username.place(x=400, y=150)
    
    ttk.Label(canvas, text="Password:").place(x=300, y=200)
    entry_password = ttk.Entry(canvas, show="*")  # Hide the password
    entry_password.place(x=400, y=200)

    if user_type == "Collaborator":
        ttk.Button(canvas, text="Register", command=lambda: register_collaborator(entry_username.get(), entry_password.get())).place(x=300, y=250)
    elif user_type == "Admin":
        ttk.Button(canvas, text="Register", command=lambda: register_admin(entry_username.get(), entry_password.get())).place(x=300, y=250)

    ttk.Button(canvas, text="Login", command=lambda: login(user_type, entry_username.get(), entry_password.get())).place(x=400, y=300)

# Function to close the application
def close_application():
    root.destroy()

# Placeholder function for login logic
def login(user_type, username, password):
    # You can add your authentication logic here
    if user_type == "Collaborator":
        # Authentication logic for collaborators
        response = api_functions.login_collaborator(username,password)
        print(response.status_code)
        if(response.status_code == 200):
            print(response.text)
            global global_user, global_password, global_id
            global_user = username
            global_password = password
            global_id = response.text.replace('"', '')
            messagebox.showinfo("Su id de usuario es",global_id)
            collaborator_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    elif user_type == "Admin":
        # Authentication logic for admins
        if username == 'admin' and password == 'password':
            messagebox.showinfo("Login Success", "Admin Login Successful")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

# Placeholder function for registration logic for collaborators
def register_collaborator(username, password):
    #add api logic
    
    response=api_functions.register_collaborator(username,password)
    print(response)
    global global_user, global_password
    global_user = username
    global_password = password
    messagebox.showinfo("Register", response.text)
    collaborator_screen()

# Placeholder function for registration logic for admins
def register_admin(username, password):
    #add api logic
    
    print(global_password, global_user)
    #messagebox.showinfo("Register", "Admin Registration Feature Coming Soon")
def main_screen():
    # Initial content on the canvas
    canvas.delete("all")
    for widget in canvas.winfo_children():
        widget.destroy()
    canvas.create_text(400, 100, text="Welcome to the Application", font=("Helvetica", 16))
    print("user: "+global_user)
    print("password: "+global_password)
    print("userid: "+global_id)
    ttk.Button(canvas, text="Login as Collaborator", command=lambda: login_screen("Collaborator")).place(x=10, y=150)
    ttk.Button(canvas, text="Login as Admin", command=lambda: login_screen("Admin")).place(x=10, y=200)
    ttk.Button(canvas, text="Exit", command=close_application).place(x=750, y=550)


# Create the main window
root = tk.Tk()
root.title("Welcome to the Application")

# Set the main window to fullscreen
#root.attributes("-fullscreen", True)

# Create a canvas for dynamic content
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()


main_screen()
# Start the main loop for the main window
root.mainloop()
