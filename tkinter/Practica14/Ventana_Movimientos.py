from tkinter import Tk, Label, Entry, Button, messagebox

class Ventana_Movimientos:

    
    def ventana(self):
        
        ventana=Tk()
        ventana.title("Movimientos")
        ventana.geometry("500x150")
        ventana.resizable(0,0)
        
        consulta_txt = Label(ventana, text="Consulta de saldo:")
        consulta_txt.grid(row=0, column=0)
        consulta_button = Button(ventana, text="Consultar", command=lambda: self.consulta_saldo())
        consulta_button.grid(row=0, column=1)
        
        aumento_txt = Label(ventana, text="Deposito de saldo:")
        aumento_txt.grid(row=1, column=0)
        aumento_entry = Entry(ventana)
        aumento_entry.grid(row=1, column=1)
        aumento_button = Button(ventana, text="Depositar", command=lambda: self.aumento_saldo(int(aumento_entry.get())))
        aumento_button.grid(row=1, column=2)
        
        disminucion_txt = Label(ventana, text="Retiro de saldo:")
        disminucion_txt.grid(row=2, column=0)
        disminucion_entry = Entry(ventana)
        disminucion_entry.grid(row=2, column=1)
        disminucion_button = Button(ventana, text="Retirar", command=lambda: self.disminucion_saldo(int(disminucion_entry.get())))
        disminucion_button.grid(row=2, column=2)
        
        transferencia_txt = Label(ventana, text="Transferencia de saldo:")
        transferencia_txt.grid(row=3, column=0)
        transferencia_entry = Entry(ventana)
        transferencia_entry.grid(row=3, column=1)
        transferencia_button = Button(ventana, text="Transferir", command=lambda: self.transferencia(int(transferencia_entry.get())))
        transferencia_button.grid(row=3, column=2)
    
        ventana.mainloop()
        
        
    def __init__(self, saldo_inicial):
        self.saldo_inicial = saldo_inicial
        
        
    def consulta_saldo(self):
        saldo = self.saldo_inicial
        messagebox.showinfo("Consulta de saldo", saldo)
            
        
    def aumento_saldo(self, aumento):
        self.aumento = aumento
        self.saldo_inicial += aumento
        messagebox.showinfo(messagebox.showinfo("Deposito éxitoso"), self.saldo_inicial)
        
        return 
    
    def disminucion_saldo(self, disminucion):
        self.disminucion = disminucion
        self.saldo_inicial -= disminucion
        messagebox.showinfo("Retiro éxitoso", self.saldo_inicial)
        return 
        
    
    def transferencia(self, transferencia):
        self.transferencia = transferencia
        self.saldo_inicial -= transferencia
        messagebox.showinfo("Transferencia éxitosa", self.saldo_inicial)
        
        return 
