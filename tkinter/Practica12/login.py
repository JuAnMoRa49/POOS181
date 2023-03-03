
from ventana import *

class login:
    
    def rcorreo():
        correo=input(str("Correo: "))
    
    def rcode():
        code=input(str("Contraseña: "))
    
    def vcorreo():
        if (correo!="juanmora"):
            print("Es incorrecto")
            
    def vcode():
        if (code!="juanmora"):
            print("Es incorrecto")