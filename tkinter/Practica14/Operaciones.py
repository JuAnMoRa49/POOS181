from Usuario import *
from tkinter import *
from Proceso import *


class Operaciones:

    def __init__(self, usuario):
        self.usuario = usuario

    def deposito(self, monto):
        self.usuario.saldo += monto
        print ("Deposito realizado con exito")

    def retiro(self, monto):
        if self.usuario.saldo >= monto:
            self.usuario.saldo -= monto
            print ("Retiro realizado con exito")
        else:
            print ("Saldo insuficiente")

    def consulta(self):
        print ("Su saldo es: ", self.usuario.saldo)
        