
from tkinter import *
from tkinter import Tk
import tkinter as j
from Gene import *

gena = Gene()

#1.- Se realiza la ventana
ven= Tk()
#se hace instancia de la ventana
ven.title("Practica 13 : Generación contraseña")
#se establece el titulo de la ventana
ven.geometry("500x200")
#se establece el tamaño de la ventana
ven.config(bg="white")
#se establece el color de la ventana

#2.- Se establecen widgets

long=Label(ven,text="Ingresa que longitud deseas", bg="white", fg="black")
long.grid(row=3, column=1)
#se establece el texto que pregunta la longitud que el usuario quiere
lon=IntVar()
longen=Entry(ven,textvariable=lon, bg="white", fg="black")
longen.grid(row=3, column=2)
#se establece donde el ususrio ingresa la cantidad de caracteres que requiere

mayu=BooleanVar()
may=Checkbutton(ven,text="¿Deseas mayusculas?",bg="white", fg="black",variable=mayu)
may.grid(row=4,column=2)
#se establece un checkbutton que pregunta si quiere mayusculas

espe=BooleanVar()
esp=Checkbutton(ven,text= "¿Deseas caracteres especiales?",bg="white", fg="black", variable=espe)
esp.grid(row=5,column=2)
#se establece un checkbutton que pregunta si quiere caracteres especiales

veri=Button(ven, text="Realizar", bg="white", fg="black",command=lambda:gena.generacion(lon.get(),mayu.get(),espe.get()))
veri.grid(row=6, column=2)

ven.mainloop()
#se solicita que la ventana se ejecute
#mainloop se debe de dejaar siempre al final del código
