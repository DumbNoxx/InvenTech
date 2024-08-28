import sqlite3
from tkinter import *


def registrar_usuario(usuario, contrasena):
    # Crear el nombre de la base de datos (adapta según tus necesidades)
    nombre_db = f"{usuario}.db"

    # Conectar a la base de datos y crear la tabla de usuarios
    conn = sqlite3.connect(f'/media/dylan/Nuevo vol/pc/Documents/programacion/Python/SIstema_de_inventario/DB/{nombre_db}')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario TEXT UNIQUE,
                        contrasena TEXT
                    )''')

    cursor.execute('''CREATE TABLE productos (
                        nombre CHAR(50),
                        serial INT NOT NULL,
                        usuario_id INT NOT NULL
                    )''')
    # Insertar el nuevo usuario
    cursor.execute('''INSERT INTO usuarios (usuario, contrasena)
                        VALUES (?, ?)''', (usuario, contrasena))

    conn.commit()
    conn.close()

    print(f"Usuario {usuario} registrado exitosamente. Base de datos {nombre_db} creada.")

# ... (código anterior)



# Crear la ventana principal
root = Tk()
root.title("Registro de Usuario")
root.geometry('500x305')

# Campos de entrada
usuario_entry = Entry(root)
contrasena_entry = Entry(root, show="*")

# Botón de registro
def registrar():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()
    registrar_usuario(usuario, contrasena)

registrar_button = Button(root, text="Registrar", command=registrar)

usuario_entry.place(x=150,y=10)
contrasena_entry.place(x=150,y=40)
registrar_button.place(x=150,y=70)

root.mainloop()
