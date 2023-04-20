from tkinter import messagebox
import sqlite3

class logicaBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("/Users/juanmontoya/Desktop/UPQ/5 cuatri/POO/Examen3Parcial/Examen3Parcial/BDImportaciones.db")
            print("Conectado a la BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar a la BD")
            
            
            
            
    def guardarMercancia(self,Mercancia,Pais):

        conx=self.conexionBD()
        
        if(Mercancia=="" or Pais==""):
            messagebox.showinfo("Aguas", "Formulario incompleto")
            
        else:
            
            #haz que cursor sea un objeto de la clase cursor
            
            cursor=conx.cursor()
            datos=(Mercancia,Pais)
            qrInsert="insert into TB_Europa(Mercancia,Pais) values(?,?)"
            
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Bien","Se ha guardado la mercancia y el pais")
            
            
    def EliminarProducto(self):
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