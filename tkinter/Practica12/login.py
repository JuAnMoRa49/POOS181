from tkinter import messagebox

class Login:
    
    def __init__(self):
        self.__correo = "juanmora"
        self.__code = "1234"
        
    
    def verificacion(self,correov,codev):
        if (correov==self.__correo) and (codev==self.__code):
            messagebox.showinfo("Bienvenido ", "Tienes acceso")
        else:
            messagebox.showinfo("Aviso ", "Acceso no concedido")
            
    