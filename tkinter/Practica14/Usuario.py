
from tkinter import *
from Operaciones import *

#1.- Se realiza la ventana
ventana= Tk()
#se hace instancia de la ventana
ventana.title("Practica 14 : Banco")
#se establece el titulo de la ventana
ventana.geometry("500x250")
#se establece el tamaño de la ventana
ventana.config(bg="white")
#se establece el color de la ventana

titulo=Label(ventana, text=(" Banco "))
titulo.grid(row=1, column=2)

txtcuen=Label(ventana, text="Numero de cuenta:")
txtcuen.grid(row=2, column=1)
cue=StringVar()
ingcuen=Entry(ventana,textvariable=cue)
ingcuen.grid(row=2, column=2)

txttit=Label(ventana, text="Titular:")
txttit.grid(row=3, column=1)
tit=StringVar()
ingtit=Entry(ventana,textvariable=tit)
ingtit.grid(row=3, column=2)

txtedad=Label(ventana, text="Edad:")
txtedad.grid(row=4, column=1)
edad=StringVar()
ingedad=Entry(ventana, textvariable=edad)
ingedad.grid(row=4, column=2)

txtsaldo=Label(ventana, text="Saldo")
txtsaldo.grid(row=5,column=1)
saldo=IntVar()
ingsaldo=Entry(ventana, textvariable=saldo)
ingsaldo.grid(row=5,column=2)


nextbut=Button(ventana,bg="white",fg="black",text="Operaciones",command=lambda:Operaciones.sumsaldo())
nextbut.grid(row=8,column=2)


def Proceso():
    
    Ope=Operaciones()
    
    ventanaps= Tk()
    ventanaps.title("Procesos de banco")
    ventanaps.geometry("500x250")
    ventanaps.config(bg="white")

    ingsaltext=Label(ventanaps, text="Cantidad a ingresar:")
    ingsaltext.grid(row=6,column=1)
    ing=IntVar()
    ingsalnum=Entry(ventanaps,textvariable=ing)
    ingsalnum.grid(row=6, column=2)
    
    ingbut=Button(ventanaps, text="Ingresar")


    retsaltext=Label(ventanaps, text="Cantidad a ingresar:")
    retsaltext.grid(row=7,column=1)
    ret=IntVar()
    retsalnum=Entry(ventanaps,textvariable=ret)
    retsalnum.grid(row=7,column=2)

ventana.mainloop()
#se solicita que la ventana se ejecute
#mainloop se debe de dejaar siempre al final del código
