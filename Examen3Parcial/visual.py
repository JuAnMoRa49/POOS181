
from tkinter import *
from tkinter import ttk
import tkinter as tk

from logicaBD import *

logica = logicaBD()


def InsertarProducto():
    logica.guardarMercancia(varProducto.get(),varPais.get())
    

def eliminaTodo():
    logica.EliminarProducto(varEliProducto.get())
    
    
def consultaPais():
    logica.consultaPais(varBusPais.get())



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

butGuardar=Button(pestana1,text="Guardar Producto",command=InsertarProducto).pack()

#Pestaña 2, es para eliminar los datos por el id

titulo=Label(pestana2, text="Eliminar mercancia",fg="black").pack()

varEliProducto=tk.StringVar()
etqEliProducto=Label(pestana2,text="Id a Eliminar: ").pack()
txtEliProducto=Entry(pestana2,textvariable=varEliProducto).pack()

butEliminar=Button(pestana2,text="Eliminar",command=eliminaTodo).pack()



#Pestaña 3, es para la consulta por pais

titulo=Label(pestana3, text="Consulta",fg="black").pack()
varBusPais=tk.StringVar()
etqBusPais=Label(pestana3,text="Pais: ").pack()
txtBusPais=Entry(pestana3,textvariable=varBusPais).pack()

btBuscar=Button(pestana3,text="Buscar").pack()


#definicion de las pestañas

panel.add(pestana1,text="Insertar Producto")
panel.add(pestana2,text="Eliminar Producto")
panel.add(pestana3,text="Consultar Pais")


Ventana.mainloop()