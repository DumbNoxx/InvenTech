import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry('600x350')
ventana.title('InvenTech')


texto_bienvenida = tk.Label(ventana,text='Bienvenido a InvenTech')
texto_bienvenida.place(x=190,y=5,relwidth=0.35,relheight=0.10)

menu = tk.Label(ventana,text='Menu')
menu.place(x=190,y=50,relwidth=0.35,relheight=0.07)
lista = []



def calcular():
	window = tk.Tk()
	window.geometry('300x250')
	window.title('Calculadora')


	pantalla = tk.Entry(window,bg='green',fg='lightblue')
	pantalla.place(x=65,y=20,relwidth=0.66,relheight=0.12)

	def igual():
		n = pantalla.get()

		r = int(n) + 1

		pantalla.delete(0,'end')
		pantalla.insert(0,r)

	boton_igual = tk.Button(window,text='=',command=igual)
	boton_igual.place(x=210,y=130,relwidth=0.16,relheight=0.10)


	def dividir():
		n = '/'
		pantalla.insert(100,n)

	boton_dividir = tk.Button(window,text='/',command=dividir)
	boton_dividir.place(x=210,y=100,relwidth=0.16,relheight=0.10)

	def multiplicar():
		n = 'x'
		pantalla.insert(100,n)

	boton_multiplicar = tk.Button(window,text='x',command=multiplicar)
	boton_multiplicar.place(x=210,y=70,relwidth=0.16,relheight=0.10)

	def restar():
		n = '-'
		pantalla.insert(100,n)

	boton_restar = tk.Button(window,text='-',command=restar)
	boton_restar.place(x=170,y=70,relwidth=0.16,relheight=0.10)

	def sumar():
		n = '+'
		pantalla.insert(100,n)

	boton_sumar = tk.Button(window,text='+',command=sumar)
	boton_sumar.place(x=130,y=70,relwidth=0.16,relheight=0.10)

	def c():
		pantalla.delete(0,'end')

	boton_borrar = tk.Button(window,text='C',command=c)
	boton_borrar.place(x=90,y=70,relwidth=0.16,relheight=0.10)

	def nueve():
		n = 9
		pantalla.insert(100,n)

	boton_nueve = tk.Button(window,text='9',command=nueve)
	boton_nueve.place(x=170,y=100,relwidth=0.16,relheight=0.10)

	def ocho():
		n = 8
		pantalla.insert(100,n)

	boton_ocho = tk.Button(window,text='8',command=ocho)
	boton_ocho.place(x=130,y=100,relwidth=0.16,relheight=0.10)

	def siete():
		n = 7
		pantalla.insert(100,n)

	boton_siete = tk.Button(window,text='7',command=siete)
	boton_siete.place(x=90,y=100,relwidth=0.16,relheight=0.10)

	def seis():
		n = 6
		pantalla.insert(100,n)

	boton_seis = tk.Button(window,text='6',command=seis)
	boton_seis.place(x=170,y=130,relwidth=0.16,relheight=0.10)

	def cinco():
		n = 5
		pantalla.insert(100,n)

	boton_cinco = tk.Button(window,text='5',command=cinco)
	boton_cinco.place(x=130,y=130,relwidth=0.16,relheight=0.10)

	def cuatro():
		n = 4
		pantalla.insert(100,n)

	boton_cuatro = tk.Button(window,text='4',command=cuatro)
	boton_cuatro.place(x=90,y=130,relwidth=0.16,relheight=0.10)


	def tres():
		n = 3
		pantalla.insert(100,n)

	boton_tres = tk.Button(window,text='3',command=tres)
	boton_tres.place(x=170,y=160,relwidth=0.16,relheight=0.10)

	def dos():
		n = 2
		pantalla.insert(100,n)

	boton_dos = tk.Button(window,text='2',command=dos)
	boton_dos.place(x=130,y=160,relwidth=0.16,relheight=0.10)


	def uno():
		n = 1
		pantalla.insert(100,n)

	boton_uno = tk.Button(window,text='1',command=uno)
	boton_uno.place(x=90,y=160,relwidth=0.16,relheight=0.10)

	def salir_ventana_calculadora():
		resultado = messagebox.askquestion("Salir", 'Quieres salir de la calculadora?', icon='question', default='no')

		if resultado == 'yes':
			window.destroy()

	boton_salir = tk.Button(window,text='Salir',command=salir_ventana_calculadora)
	boton_salir.place(x=105,y=200,relwidth=0.30,relheight=0.09)


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
