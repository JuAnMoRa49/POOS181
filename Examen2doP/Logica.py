
from tkinter import messagebox
import string
import random


class Gene:
    
    def __init__(self):
        self.__gena =""
        
    
    def generacion(self,nomb,prim,segu,anon,anoc,carr,num):
        
        nomb=nomb[0].upper()
        prim=prim[0:2].upper()
        segu=segu[0:2].upper()
        anon=anon[0:2]
        anoc=anoc[0:2]
        carr=carr[0:3].upper()
        num=random.randint(0,9)
        
        self._gena = "".join([nomb,prim,segu,anon,anoc,carr,str(num)])