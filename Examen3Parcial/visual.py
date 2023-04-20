

from tkinter import *
from tkinter import ttk
import tkinter as tk

from logicaBD import *

logica = logicaBD()


def InsertarProducto():
    logica.guardarProducto(varProducto.get(),varPais.get())
    

def deleteUsuario():
    logica.EliminarProducto(varEliProducto.get())
    

def ejecutaSelectU():
    usuario= logica.consultarUsuario(varBus.get())
    
    for usu in usuario:
        cadena= str(usu[0]) + " " + usu[1] + " " + usu[2]+ " " + str(usu[3])
    
    if(usuario):
        return (cadena)
    else:
        messagebox.showinfo("No existe","El usuario no se encontro")


Ventana=Tk()
Ventana.title("Examen 3 parcial")
Ventana.geometry("500x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill="both", expand="yes")

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)


#Pestaña 1, es para el registro de Mercancia y Pais

titulo=Label(pestana1, text="Registro de Producto",fg="black").pack()

varProducto=tk.StringVar()
etqProducto=Label(pestana1,text="Producto: ").pack()
txtProducto=Entry(pestana1,textvariable=varProducto).pack()

varPais=tk.StringVar()
etqPais=Label(pestana1,text="Pais: ").pack()
txtPais=Entry(pestana1,textvariable=varPais).pack()

butGuardar=Button(pestana1,text="Guardar Usuario",command=InsertarProducto).pack()

#Pestaña 2, es para eliminar los datos por el id

titulo=Label(pestana2, text="Registro de Producto",fg="black").pack()

varEliProducto=tk.StringVar()
etqEliProducto=Label(pestana2,text="Id a Eliminar: ").pack()
txtEliProducto=Entry(pestana2,textvariable=varEliProducto).pack()

butGuardar=Button(pestana2,text="Guardar Usuario",command=InsertarProducto).pack()



#Pestaña 3, es para la consulta de un usuario

titulo2=Label(pestana3, text="Buscar Usuarios",fg="black").pack()

varBus=tk.StringVar()
etqBus=Label(pestana3,text="Identificador: ").pack()
txtBus=Entry(pestana3,textvariable=varBus).pack()

butBuscar=Button(pestana3,text="Buscar",command=ejecutaSelectU).pack()


#definicion de las pestañas

panel.add(pestana1,text="Formulario usuarios")
panel.add(pestana2,text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuario")


Ventana.mainloop()