
from tkinter import Tk, Frame, Button, messagebox

class ventana:
    
    root = Tk()
    #1.- Se realiza la ventana
    ventana= Tk()
    #se hace instancia de la ventana
    ventana.title("Practica 12 : Login")
    #se establece el titulo de la ventana
    ventana.geometry("600x400")
    #se establece el tamaño de la ventana


    #2.- Se realizan las secciones
    se1= Frame(ventana, bg="#FFDDDD")
    #se establece la primera seccion dentro de la ventana
    se1.pack(expand=True, fill= "width")
    #se establece la primera seccion con pack, para expandirse en ambas direcciones

    se2= Frame(ventana, bg="#FFFDDD")
    #se establece la primera seccion dentro de la ventana
    se2.pack(expand=True, fill= "both")
    #se establece la primera seccion con pack, para expandirse en ambas direcciones
    
    #3.- Se definen las ventanas
    def mensajeError():
        messagebox.showinfo("Aviso","Tu registro no es correcto")

    ventana.mainloop()
    #se solicita que la ventana se ejecute
    #mainloop se debe de dejaar siempre al final del código
