
from tkinter import messagebox
import sqlite3

class logicaBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/Usuario/Desktop/POO/Parcial 1/Examen3Parcial/BDImportaciones.db")
            #conexion = sqlite3.connect("/Users/juanmontoya/Desktop/UPQ/5 cuatri/POO/Parcial 1/Git/POOS181/Examen3Parcial/BDImportaciones.db")
            print("Conectado a la BD")
            
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar a la BD")
            return None
            
    def guardarMercancia(self, Mercancia, Pais):
        conx = self.conexionBD()
        if conx is not None:
            if Mercancia == "" or Pais == "":
                messagebox.showinfo("Aguas", "Formulario incompleto")
            else:
                self.cursor = conx.cursor()
                datos = (Mercancia, Pais)
                qrInsert = "INSERT INTO TB_Europa(Mercancia,Pais) VALUES (?, ?)"
                self.cursor.execute(qrInsert, datos)
                conx.commit()
                conx.close()
                messagebox.showinfo("Bien", "Se ha guardado la mercancia y el pais")
        else:
            messagebox.showerror("Error", "No se pudo conectar a la BD")

            
    def EliminarProducto(self,id):
        conx=self.conexionBD()
        self.cursor=conx.cursor()

        self.cursor.execute("delete * from TB_Europa")
        
        conx.commit()
        conx.close()
        messagebox.showinfo("Bien","Se ha eliminado la mercancia")
        
        
    def consultaPais(self):
        conx=self.conexionBD()
        cursor=conx.cursor()
        
        self.cursor.execute("select * from TB_Europa where Pais=?")
        
        for i in self.cursor:
            self.tree.insert("",0,text=i[0],values=(i[1],i[2]))
        
        conx.commit()
        conx.close()