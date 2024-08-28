from tkinter import *
import sqlite3
root = Tk()
root.title('Agregar Producto')
root.geometry('500x300')


def agregar_producto(usuario_id, nombre, serial):
    nombre_db = f"/media/dylan/Nuevo vol/pc/Documents/programacion/Python/SIstema_de_inventario/DB/Dylana.db"
    conn = sqlite3.connect(nombre_db)
    cursor = conn.cursor()

    # Insertar el nuevo producto
    cursor.execute('''INSERT INTO productos (nombre, serial, usuario_id)
                        VALUES (?, ?, ?)''', (nombre, serial, usuario_id))

    conn.commit()
    conn.close()

    print(f"Producto {nombre} agregado exitosamente.")



def agregar_producto_gui():
    usuario_id = 2 
    nombre = nombre_producto.get()
    serial = serial_producto.get()
    agregar_producto(usuario_id, nombre, serial)
    nombre_producto.delete(0, END)
    serial_producto.delete(0, END)


nombre_producto = Entry(root)
serial_producto = Entry(root)
agregar_boton = Button(root, text="Agregar Producto", command=agregar_producto_gui)


nombre_producto.pack()
serial_producto.pack()
agregar_boton.pack()

root.mainloop()