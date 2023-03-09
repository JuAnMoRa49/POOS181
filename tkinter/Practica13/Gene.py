
from tkinter import messagebox
from Ventana import *
import string

class code:
    
    lon=long.get()
    mayus=may.get()
    especial=esp.get()
    
    def generacion():
        if(lon!=0):
            lon=8
        else:
            if (may == "1"):
                may= string.ascii_letters
                #ascii_letters es para mayusculas o minusculas
            if (esp == "1"):
                esp= string.punctuation
                #puntuaction es para simbolos especiales
            for n in range (lon):
                car= random(may)
                car= random(esp)
            
            