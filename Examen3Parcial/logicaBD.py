from tkinter import messagebox
import sqlite3

class logicaBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
    
        try:
            conexion = sqlite3.connect("/Users/juanmontoya/Desktop/UPQ/5 cuatri/POO/Parcial 1/Git/POOS181/Examen3Parcial/BDImportaciones.db")
            print("Conectado a la BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar a la BD")
            
            
            
    def guardarProducto(self,Mercancia,Pais):
        
        #1.-se usa la conexion pasada
        conx=self.conexionBD()
        
        #2.-se validan los parametors, para que no haya vacios
        
        if(Mercancia=="" or Pais==""):
            messagebox.showinfo("Aguas", "Formulario incompleto")
            
        else:
            
            #3.-preparamos los datos 
            #cursor es el que ejecuta los movimientos a la base de datos
            cursor=conx.cursor()
            datos=(Mercancia,Pais)
            qrInsert="insert into TB_Europa(Mercancia, Pais) values(?,?)"
            
            #4.-ejecuta Insert y cerramos Conexion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Bien","Se ha guardado el usuario")
            
            
    def EliminarProducto(self):
        conx=self.conexionBD()
        self.cursor=conx.cursor()
        
        self.cursor.execute("delete * from TB_Europa")
        
        conx.commit()
        conx.close()
        messagebox.showinfo("Bien","Se ha eliminado el usuario")
        