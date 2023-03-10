
from tkinter import messagebox
import string
import random

class Gene:
    def __init__(self):
        self.__code = "" 
    
    def generacion(self,lon,may,esp):
        if(lon==0):
            lon=8
        if (may==True and esp==True):
                self._code="".join(random.choice(string.ascii_letters+string.punctuation)for x in range (lon))
            #junta los caracteres y selecciona random entre mayusculas, minusculas y caracteres especiales 
        elif (may==True and esp==False):
                self._code="".join(random.choice(string.ascii_letters)for x in range (lon))
            #junta los caracteres y selecciona random entre mayusculas y minusculas
        elif (may==False and esp==True):
                self._code="".join(random.choice(string.punctuation+string.ascii_lowercase)for x in range (lon))
            #junta los cacracteres y selecciona random entre minusculas y caracteres especiales
        else:
                self._code="".join(random.choice(string.ascii_lowercase)for x in range (lon))
        messagebox.showinfo("La contreseña es: ",self._code)
        