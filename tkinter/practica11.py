
from tkinter import Tk, Frame, Button

#1.-Creación de ventana

ventana= Tk()
#se hace instancia de la ventana
ventana.title("Practica 11: 3 Frames")
#se establece el titulo de la ventana
ventana.geometry("600x400")
#se establece el tamaño de la ventana

#2.-Definimos las secciones de la ventana

seccion1= Frame(ventana, bg="#C1E287")
#se establece la primera seccion dentro de la ventana
seccion1.pack(expand=True, fill= "both")
#se establece la primera seccion con pack, para expandirse en ambas direcciones

seccion2= Frame(ventana, bg="#87E2D8")
seccion2.pack(expand=True, fill="both")

seccion3= Frame(ventana, bg="#D387E2")
seccion3.pack(expand=True, fill="both")

#3.-Botoes

botonAzul=Button(seccion1, text="boton azul", fg="blue")
#se establece el boton azul en la seccion 1, con texto y color azul del texto
botonAzul.place(x=60, y=60)
#se establece la posicion del boton azul

botonAmarillo=Button(seccion2, text="boton amarillo", fg="#9BA31B")
#se establece el color amarillo con caracteristicas similares al azul
botonAmarillo.grid(row=0, column=0)
#se establece su posicion con grid, con filas y columnas
botonNegro=Button(seccion2, text="boton negro", fg="black")
#similar al pasado
botonNegro.grid(row=1, column=1)
#similar al pasado

botonVerde=Button(seccion3, text="boton verde", fg="#95E287")
#se establece el boton verde con caracteristicas similares al primero
botonVerde.pack()
#se usa pack para centrarlo y que se adapte a la ventana


ventana.mainloop()
#se solicita que la ventana se ejecute
#mainloop se debe de dejaar siempre al final del código