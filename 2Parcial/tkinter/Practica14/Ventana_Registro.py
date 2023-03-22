from tkinter import *


class Ventana_Registro:
        
    def ventana_registro(self):
        ventana=Tk()
        ventana.title("Registro de cuentas")
        ventana.geometry("400x150")
        ventana.resizable(0,0)

        # se crean campos de entrada y de entry de cuenta
        cuenta_txt = Label(ventana, text="Número de cuenta:")
        cuenta_txt.grid(row=0, column=0)
        cuenta_dato = Entry(ventana)
        cuenta_dato.grid(row=0, column=1)

        # se crean los campos de entrada y de entry de nombre
        nombre_txt = Label(ventana, text="Nombre:")
        nombre_txt.grid(row=1, column=0)
        nombre_dato = Entry(ventana)
        nombre_dato.grid(row=1, column=1)

        # creo los campos de entrada y de entry de edad
        edad_txt = Label(ventana, text="Edad:")
        edad_txt.grid(row=2, column=0)
        edad_dato = Entry(ventana)
        edad_dato.grid(row=2, column=1)

        # creo los campos de entrada y de entry de saldo
        saldo_txt = Label(ventana, text="Saldo:")
        saldo_txt.grid(row=3, column=0)
        saldo_dato = Entry(ventana,textvariable=self.saldo_inicial)
        saldo_dato.grid(row=3, column=1)

        # se establece el botón de registro
        boton_registrar = Button(ventana, text="Registrar", command=lambda: [self.registrar(cuenta_dato.get(), nombre_dato.get(), edad_dato.get(), saldo_dato.get()), self.ventana_movimientos.ventana()])
        boton_registrar.grid(row=4, column=1)
        
        ventana.mainloop()
        
        
    def registrar(self, cuenta, nombre, edad, saldo_inicial):
        self.cuenta = cuenta
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo_inicial
        
        return cuenta, nombre, edad, saldo_inicial

            
    
ventana = Ventana_Registro()
ventana.ventana_registro()
