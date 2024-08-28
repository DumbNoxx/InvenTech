import tkinter as tk
from tkinter import messagebox
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()
calculadoras = os.getenv('SCRIPT_CALCULADORA') 

ventana = tk.Tk()
ventana.geometry('600x350')
ventana.title('InvenTech')


texto_bienvenida = tk.Label(ventana,text='Bienvenido a InvenTech')
texto_bienvenida.place(x=190,y=5,relwidth=0.35,relheight=0.10)

menu = tk.Label(ventana,text='Menu')
menu.place(x=190,y=50,relwidth=0.35,relheight=0.07)


def calcular():
	subprocess.run(['python3',calculadoras])

boton_calculadora = tk.Button(ventana,text='Calculadora',command=calcular)
boton_calculadora.place(x=190,y=90,relwidth=0.35,relheight=0.10)

def agregar_producto():
	subprocess.run(['python3','/media/dylan/Nuevo vol/pc/Documents/programacion/Python/SIstema_de_inventario/test/agregar_archivo.py'])

boton_agregar_producto = tk.Button(ventana,text='Agregar producto',command=agregar_producto)
boton_agregar_producto.place(x=190,y=140,relwidth=0.35,relheight=0.10)


boton_buscar_producto = tk.Button(ventana,text='Buscar producto')
boton_buscar_producto.place(x=190,y=190,relwidth=0.35,relheight=0.10)

def crearusuario():
	subprocess.run(['python3','/media/dylan/Nuevo vol/pc/Documents/programacion/Python/SIstema_de_inventario/test/SQLite.py'])

boton_crearUsuario = tk.Button(ventana,text='Crear usuario',command=crearusuario)
boton_crearUsuario.place(x=420,y=10,relwidth=0.35,relheight=0.10)


def leave():
    resultado = messagebox.askquestion("Salir", 'Quieres salir de InvenTech?', icon='question', default='no')

    if resultado == 'yes':
        ventana.quit()


boton_salir = tk.Button(ventana,text='Salir',command=leave)
boton_salir.place(x=190,y=240,relwidth=0.35,relheight=0.10)






copyrigth1 = tk.Label(ventana,text='Nox Corporations © 2024')
copyrigth1.place(x=420,y=270,relwidth=0.30,relheight=0.20)



ventana.mainloop()
