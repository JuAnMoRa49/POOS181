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
            
    def actualizarUsuario(self,id,nom,cor,con):
        conx=self.conexionBD()
        
        if(id=="" or nom=="" or cor=="" or con==""):
            messagebox.showinfo("Aguas", "Formulario incompleto")
            
        else:
            cursor=conx.cursor()
            conH=self.encriptarCon(con)
            datos=(nom,cor,conH,id)
            qrUpdate="update TBRegistrados set Nombre=?, Correo=?, Contra=? where id=?"
            
            cursor.execute(qrUpdate,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Bien","Se ha actualizado el usuario")
            
            
    def encriptarCon(self,con):
        conPlana= con
        conPlana= conPlana.encode() #convertimos con a bytes
        sal= bcrypt.gensalt() #regresa caracteres aleatorios en bytes
        conHa= bcrypt.hashpw(conPlana,sal)#a hash, con parametro contraseña en bytes y la sal
        print(conHa)
        return conHa
    
    
    #mmetodo para buscar usuario
    
    def consultarUsuario(self,id):
        #1.- preparar la conexion
        conx=self.conexionBD()
        
        #2.-verificar si el id contiene algo
        
        if(id==""):
            messagebox.showwarning("Cuidado","Id vacio, escribe algo valido")
            conx.close()
        else:
            try:
                #3.-preparar cursor y el query
                cursor=conx.cursor()
                selectQry="select * from TBRegistrados where id="+id
                
                #4.- ejecutar y guardar la consulta
                cursor.execute(selectQry)
                rsUsuario= cursor.fetchall()
                conx.close()
                
                return rsUsuario
                
            except sqlite3.OperationalError:
                print("Error Consulta")
                
                
    #metodo para conocer los usuarios registrados
    
    def VerUsuarios(self):
        conx=self.conexionBD()
        self.cursor=conx.cursor()
        
        self.cursor.execute("select * from TBRegistrados")
        usuarios=self.cursor.fetchall()
        return usuarios