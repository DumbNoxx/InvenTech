import tkinter as tk

ventana = tk.Tk()
ventana.geometry('600x350')
ventana.title('InvenTech')


texto_bienvenida = tk.Label(ventana,text='Bienvenido a InvenTech')
texto_bienvenida.place(x=190,y=5,relwidth=0.35,relheight=0.10)

menu = tk.Label(ventana,text='Menu')
menu.place(x=190,y=50,relwidth=0.35,relheight=0.07)


boton_calculadora = tk.Button(ventana,text='Calculadora')
boton_calculadora.place(x=190,y=90,relwidth=0.35,relheight=0.10)

boton_agregar_producto = tk.Button(ventana,text='Agregar producto')
boton_agregar_producto.place(x=190,y=140,relwidth=0.35,relheight=0.10)


boton_buscar_producto = tk.Button(ventana,text='Buscar producto')
boton_buscar_producto.place(x=190,y=190,relwidth=0.35,relheight=0.10)

boton_salir = tk.Button(ventana,text='Salir')
boton_salir.place(x=190,y=240,relwidth=0.35,relheight=0.10)


ventana.mainloop()