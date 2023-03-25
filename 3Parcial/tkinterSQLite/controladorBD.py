from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    

    #metodo para generar la conexion y comprobarla
    def conexionBD(self):
        
        try:
            conexion = sqlite3.connect("/Users/juanmontoya/Desktop/UPQ/5 cuatri/POO/Parcial 1/Git/POOS181/3Parcial/tkinterSQLite/DBUsuarios.db")
            print("Conectado a la BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar a la BD")
        
        
    #metodo para guardar usuarios
    def guardarUsuario(self,nom,cor,con):
        
        #1.-se usa la conexion pasada
        conx=self.conexionBD()
        
        #2.-se validan los parametors, para que no haya vacios
        
        if(nom=="" or cor=="" or con==""):
            messagebox.showinfo("Aguas", "Formulario incompleto")
            
        else:
            
            #3.-preparamos los datos 
            #cursor es el que ejecuta los movimientos a la base de datos
            cursor=conx.cursor()
            conH=self.encriptarCon(con)
            datos=(nom,cor,conH)
            qrInsert="insert into TBRegistrados(Nombre, Correo, Contra) values(?,?,?)"
            
            #4.-ejecuta Insert y cerramos Conexion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Bien","Se ha guardado el usuario")
            
            
    def encriptarCon(self,con):
        conPlana= con
        conPlana= conPlana.encode() #convertimos con a bytes
        sal= bcrypt.gensalt() #regresa caracteres aleatorios en bytes
        conHa= bcrypt.hashpw(conPlana,sal)#a hash, con parametro contraseña en bytes y la sal
        print(conHa)
        return conHa
    