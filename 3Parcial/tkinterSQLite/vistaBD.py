
from tkinter import *
from tkinter import ttk
import tkinter as tk

#1.- se realiza la importacion de clase para que se conozcan
from controladorBD import *

#2.-creamos un objeto de la clase Controlador BD

#(nombre del objeto) = (clase importada)
controlador = controladorBD()

#3.-Funcion para el boton
def ejecutaInsert():
    #se ingresan los datos obtenidos desde aqui
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())


Ventana=Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("500x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill="both", expand="yes")

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)

titulo=Label(pestana1, text="Registro de Usuarios",fg="black", font=("Modern",18)).pack()

varNom=tk.StringVar()
etqNom=Label(pestana1,text="Nombre: ").pack()
txtNom=Entry(pestana1,textvariable=varNom).pack()

varCor=tk.StringVar()
etqCor=Label(pestana1,text="Correo: ").pack()
txtCor=Entry(pestana1,textvariable=varCor).pack()

varCon=tk.StringVar()
etqCon=Label(pestana1,text="Contraseña: ").pack()
txtCon=Entry(pestana1,textvariable=varCon).pack()


butGuardar=Button(pestana1,text="Guardar Usuario",command=ejecutaInsert).pack()



panel.add(pestana1,text="Formulario usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuario")
panel.add(pestana4,text="Actualizar Usuario")

Ventana.mainloop()