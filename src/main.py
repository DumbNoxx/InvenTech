import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry('600x350')
ventana.title('InvenTech')


texto_bienvenida = tk.Label(ventana,text='Bienvenido a InvenTech')
texto_bienvenida.place(x=190,y=5,relwidth=0.35,relheight=0.10)

menu = tk.Label(ventana,text='Menu')
menu.place(x=190,y=50,relwidth=0.35,relheight=0.07)


def calcular():
	window = tk.Tk()
	window.geometry('300x250')
	window.title('Calculadora')

	numero_label_1 = tk.Label(window,text='Introduce un numero')
	numero_label_1.place(x=30,y=10,relwidth=0.90,relheight=0.10)

	numero_entrada_1 = tk.Entry(window)
	numero_entrada_1.place(x=120,y=39,relwidth=0.25,relheight=0.10)

	numero_label_2 = tk.Label(window,text='Introduce otro numero')
	numero_label_2.place(x=30,y=60,relwidth=0.90,relheight=0.10)

	numero_entrada_2 = tk.Entry(window)
	numero_entrada_2.place(x=120,y=80,relwidth=0.25,relheight=0.09)

	numero_resultado_label = tk.Label(window,text='Resultado')
	numero_resultado_label.place(x=20,y=100,relwidth=0.90,relheight=0.10)

	numero_resultado = tk.Entry(window)
	numero_resultado.place(x=120,y=120,relwidth=0.25,relheight=0.09)

	def suma():
		numero1 = numero_entrada_1.get()
		numero2 = numero_entrada_2.get()

		r = int(numero1) + int(numero2)
		numero_resultado.delete(0,'end')
		numero_resultado.insert(0,r)


	boton_suma = tk.Button(window,text='Sumar',command=suma)
	boton_suma.place(x=10,y=180,relwidth=0.30,relheight=0.09)



	def resta():
		numero1 = numero_entrada_1.get()
		numero2 = numero_entrada_2.get()

		r = int(numero1) - int(numero2)
		numero_resultado.delete(0,'end')
		numero_resultado.insert(0,r)


	boton_resta = tk.Button(window,text='Restar',command=resta)
	boton_resta.place(x=200,y=180,relwidth=0.30,relheight=0.09)


	def multiplica():
		numero1 = numero_entrada_1.get()
		numero2 = numero_entrada_2.get()

		r = int(numero1) * int(numero2)
		numero_resultado.delete(0,'end')
		numero_resultado.insert(0,r)


	boton_multiplicacion = tk.Button(window,text='Multiplicar',command=multiplica)
	boton_multiplicacion.place(x=10,y=220,relwidth=0.30,relheight=0.09)

	def division():
		numero1 = numero_entrada_1.get()
		numero2 = numero_entrada_2.get()

		r = float(numero1) / float(numero2)
		numero_resultado.delete(0,'end')
		numero_resultado.insert(0,r)


	boton_suma = tk.Button(window,text='Dividir',command=division)
	boton_suma.place(x=200,y=220,relwidth=0.30,relheight=0.09)

	def salir_ventana_calculadora():
		resultado = messagebox.askquestion("Salir", 'Quieres salir de la calculadora?', icon='question', default='no')

		if resultado == 'yes':
			window.destroy()

	boton_salir = tk.Button(window,text='Salir',command=salir_ventana_calculadora)
	boton_salir.place(x=105,y=200,relwidth=0.30,relheight=0.09)


boton_calculadora = tk.Button(ventana,text='Calculadora',command=calcular)
boton_calculadora.place(x=190,y=90,relwidth=0.35,relheight=0.10)

boton_agregar_producto = tk.Button(ventana,text='Agregar producto')
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