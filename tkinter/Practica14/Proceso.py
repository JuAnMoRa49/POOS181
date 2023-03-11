from tkinter import *
from Operaciones import *
from Usuario import *


class Proceso:
        
    def ventanaps():
        
        Oper=Operaciones()
        
        ventanaps= Tk()
        ventanaps.title("Procesos de banco")
        ventanaps.geometry("500x250")
        ventanaps.config(bg="white")

        ingsaltext=Label(ventanaps, text="Cantidad a ingresar:")
        ingsaltext.grid(row=6,column=1)
        ing=IntVar()
        ingsalnum=Entry(ventanaps,textvariable=ing)
        ingsalnum.grid(row=6, column=2)
        
        ingbut=Button(ventanaps, text="Ingresar", command= lambda:Oper.deposito(ing.get()))
        ingbut.grid(row=6, column=3)
        
        retsaltext=Label(ventanaps, text="Cantidad a ingresar:")
        retsaltext.grid(row=7,column=1)
        ret=IntVar()
        retsalnum=Entry(ventanaps,textvariable=ret)
        retsalnum.grid(row=7,column=2)
        
        retbut=Button(ventanaps, text="Retirar", command= lambda:Oper.retiro(ret.get()))
        retbut.grid(row=7, column=3)
