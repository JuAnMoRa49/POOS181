
from tkinter import *
from tkinter import ttk
import tkinter as tk


#1.- se realiza la importacion de clase para que se conozcan
from controladorBD import *

#2.-creamos un objeto de la clase Controlador BD

#(nombre del objeto) = (clase importada)
controlador = controladorBD()

#3.-Funcion para el boton de guardar usuario
def ejecutaInsert():
    #se ingresan los datos obtenidos desde aqui
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

def ejecutaUpdate():
    controlador.actualizarUsuario(varIdAct.get(),varNomAct.get(),varCorAct.get(),varConAct.get())

#4.-Funcion para el boton de busqueda
def ejecutaSelectU():
    usuario= controlador.consultarUsuario(varBus.get())
    
    for usu in usuario:
        cadena= str(usu[0]) + " " + usu[1] + " " + usu[2]+ " " + str(usu[3])
    
    if(usuario):
        return (cadena)
    else:
        messagebox.showinfo("No existe","El usuario no se encontro")

def deleteUsuario():
    controlador.EliminarUsuario(varIdEli.get())


cade=str(ejecutaSelectU)

Ventana=Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("500x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill="both", expand="yes")

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)
pestana5= ttk.Frame(panel)

#Pestaña 1, es para el registro de usuarios

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


#Pestaña 2, es para la consulta de un usuario

titulo2=Label(pestana2, text="Buscar Usuarios",fg="black", font=("Modern",18)).pack()

varBus=tk.StringVar()
etqBus=Label(pestana2,text="Identificador: ").pack()
txtBus=Entry(pestana2,textvariable=varBus).pack()

butBuscar=Button(pestana2,text="Buscar",command=ejecutaSelectU).pack()


#pestaña 3, para consultar todos los usuarios

titulo3=Label(pestana3, text="Consultar Usuarios",fg="black", font=("Modern",18)).grid(column=0,row=0)

def leer():
    usuarios=controlador.VerUsuarios()
    for usuari in usuarios:
        tree.insert("", 0, text=usuari[0], values=(usuari[1],usuari[2],usuari[3],usuari[4]))
        
tree=ttk.Treeview(pestana3,columns=("n0", "n1", "n2","n3"))
tree.heading("n0",text="ID")
tree.heading("n1",text="Nombre")
tree.heading("n2",text="Correo")
tree.heading("n3",text="Contraseña")


tree.grid(column=0,row=1,padx=10, pady=10)


def limpiar():
    tree.delete(*tree.get_children())
    for i in tree.get_children():
        tree.delete(i)
        
btnLeer=Button(pestana3,text="Ver Usuarios",command=leer).grid(column=1,row=3,padx=10, pady=10)
btnLimp=Button(pestana3,text="Limpiar",command=limpiar).grid(column=2,row=3,padx=10, pady=10)

#pestaña 4, para actualizar un usuario

titulo4=Label(pestana4, text="Registro de Usuarios",fg="black", font=("Modern",18)).pack()

varIdAct=tk.StringVar()
etqIdAct=Label(pestana4,text="Identificador: ").pack()
txtIdAct=Entry(pestana4,textvariable=varIdAct).pack()

varNomAct=tk.StringVar()
etqNomAct=Label(pestana4,text="Nombre: ").pack()
txtNomAct=Entry(pestana4,textvariable=varNomAct).pack()

varCorAct=tk.StringVar()
etqCorAct=Label(pestana4,text="Correo: ").pack()
txtCorAct=Entry(pestana4,textvariable=varCorAct).pack()

varConAct=tk.StringVar()
etqConAct=Label(pestana4,text="Contraseña: ").pack()
txtConAct=Entry(pestana4,textvariable=varConAct).pack()

butGuardar=Button(pestana4,text="Actualizar Usuario",command=ejecutaUpdate).pack()

    
#pestaña 5, para eliminar un usuario

titulo5=Label(pestana5, text="Eliminar Usuarios",fg="black", font=("Modern",18)).pack()


varIdEli=tk.StringVar()
etqIdEli=Label(pestana5,text="Identificador: ").pack()
txtIdEli=Entry(pestana5,textvariable=varIdEli).pack()

butEli=Button(pestana5,text="Eliminar",command=deleteUsuario).pack()


#definicion de las pestañas

panel.add(pestana1,text="Formulario usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuario")
panel.add(pestana4,text="Actualizar Usuario")
panel.add(pestana5,text="Eliminar Usuario")

Ventana.mainloop()