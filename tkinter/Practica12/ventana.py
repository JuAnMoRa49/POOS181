
from tkinter import Tk, Frame, Button, messagebox, Entry,Label
from login import *
import tkinter as juan     

Usuario = Login()

#1.- Se realiza la ventana
ventana= Tk()
#se hace instancia de la ventana
ventana.title("Practica 12 : Login")
#se establece el titulo de la ventana
ventana.geometry("600x400")
#se establece el tamaño de la ventana


#2.- Se realizan las secciones
se1= Frame(ventana, bg="#FFFFFF")
#se establece la primera seccion dentro de la ventana
se1.pack(expand=True, fill= "both")
#se establece la primera seccion con pack, para expandirse en ambas direcciones
se2= Frame(ventana, bg ="#FFFFFF")
se2.pack(expand=True, fill= "both")
    
    
#3.- Se definen los widgets
correoetiqueta=juan.Label(se1, text="Ingresa correo ", bg ="black", fg ="white")
correoetiqueta.place(x=149,y=150)
#se establece la etiqueta de correo con especiicaciones
codeentrada=juan.Label(se1, text="Ingresa contraseña ", bg ="black", fg ="white")
codeentrada.place(x=120,y=175)
#se establece la etiqueta de contraseña con especificaciones

correov=juan.Entry(se1, bg="white", fg="black")
correov.place(x=245,y=148)
#se solicita el correo
codev=juan.Entry(se1, bg="white", fg="black")
codev.place(x=245,y=173)
#se solicita la contraseña


botonverificacion=juan.Button(se2,text="Verificar",bg="black", fg="#000", command=lambda:Usuario.verificacion(correov,codev))
botonverificacion.place(x=250, y=50)
#se establece el boton para verificar
 

ventana.mainloop()
#se solicita que la ventana se ejecute
#mainloop se debe de dejaar siempre al final del código
