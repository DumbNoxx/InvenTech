import tkinter as tk
from tkinter import messagebox
import subprocess

ventana = tk.Tk()
ventana.geometry('600x350')
ventana.title('InvenTech')


texto_bienvenida = tk.Label(ventana,text='Bienvenido a InvenTech')
texto_bienvenida.place(x=190,y=5,relwidth=0.35,relheight=0.10)

menu = tk.Label(ventana,text='Menu')
menu.place(x=190,y=50,relwidth=0.35,relheight=0.07)


def calcular():
	subprocess.run(['python3','/media/dylan/Nuevo vol/pc/Documents/programacion/Python/SIstema_de_inventario/scripts/calculadora.py'])

boton_calculadora = tk.Button(ventana,text='Calculadora',command=calcular)
boton_calculadora.place(x=190,y=90,relwidth=0.35,relheight=0.10)

def agregar_producto():
	window = tk.Tk()
	window.geometry('400x300')
	window.title('Agregar Producto')


	serial_label = tk.Label(window,text='Serial Del Producto')
	serial_label.place(x=20,y=10,relwidth=0.90,relheight=0.20)


	serial_entrada = tk.Entry(window)
	serial_entrada.place(x=120,y=60,relwidth=0.40,relheight=0.09)

	
	
	def agregar_serial_producto():
		serial1 = int(serial_entrada.get())

		for i in len(lista):
			lista.append(serial1)

		temporal = tk.Label(window,text=f'Producto {lista} agregado')
		temporal.place(x=10,y=150,relwidth=0.90,relheight=0.09)
		temporal.after(600,temporal.destroy)



	boton_enviar = tk.Button(window,text='Agregar Producto',command=agregar_serial_producto)
	boton_enviar.place(x=120,y=90,relwidth=0.40,relheight=0.09)

	def mostrar_lista():
		for i in range(2):
			temporal = tk.Label(window,text=f'{lista}')
			temporal.place(x=10,y=150,relwidth=0.90,relheight=0.09)
			temporal.after(600,temporal.destroy)
	boton_mostrar = tk.Button(window,text='Mostrar lista',command=mostrar_lista)
	boton_mostrar.place(x=120,y=180,relwidth=0.40,relheight=0.09)


	def salir_ventana_agregar_producto():
		resultado = messagebox.askquestion('Salir','Quieres salir de la ventana de Agregar Producto?',icon='question',default='no')

		if resultado == 'yes':
			window.destroy()


	boton_salir = tk.Button(window,text='Salir',command=salir_ventana_agregar_producto)
	boton_salir.place(x=120,y=120,relwidth=0.40,relheight=0.09)


boton_agregar_producto = tk.Button(ventana,text='Agregar producto',command=agregar_producto)
boton_agregar_producto.place(x=190,y=140,relwidth=0.35,relheight=0.10)


boton_buscar_producto = tk.Button(ventana,text='Buscar producto')
boton_buscar_producto.place(x=190,y=190,relwidth=0.35,relheight=0.10)



def leave():
    resultado = messagebox.askquestion("Salir", 'Quieres salir de InvenTech?', icon='question', default='no')

    if resultado == 'yes':
        ventana.quit()


boton_salir = tk.Button(ventana,text='Salir',command=leave)
boton_salir.place(x=190,y=240,relwidth=0.35,relheight=0.10)






copyrigth1 = tk.Label(ventana,text='Nox Corporations © 2024')
copyrigth1.place(x=420,y=270,relwidth=0.30,relheight=0.20)



ventana.mainloop()
