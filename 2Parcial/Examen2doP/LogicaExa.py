
from tkinter import messagebox
import random


class Gene:
    
    def __init__(self):
        pass
        
        
    def generacion(self,nomb,prim,segu,anon,anoc,carr,num):
        
        nomb=nomb[0].upper()
        prim=prim[0:2].upper()
        segu=segu[0:2].upper()
        anon=anon[0:2]
        anoc=anoc[0:2]
        carr=carr[0:3].upper()
        num=random.randint(0,9)
        
        gena= "".join([nomb,prim,segu,anon,anoc,carr,str(num)])
        
        return  messagebox.showinfo("La matricula es: ", gena)
        