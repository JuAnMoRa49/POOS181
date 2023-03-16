from tkinter import Tk, Label, Entry, Button, messagebox


class Principal:

    ventana=Tk()

    ventana.title("Registro")
    ventana.geometry("400x200")
    ventana.resizable(0,0)
    
    nom_txt = Label(ventana, text="Nombre(s):")
    nom_txt.grid(row=0, column=0)
    nombre=str
    nom_entry = Entry(ventana,textvariable=nombre)
    nom_entry.grid(row=0, column=1)
    
    
    pri_apellido_txt = Label(ventana, text="Primer apellido:")
    pri_apellido_txt.grid(row=1, column=0)
    primer=str
    pri_apellido_entry = Entry(ventana,textvariable=primer)
    pri_apellido_entry.grid(row=1, column=1)
   
    
    seg_apellido_txt = Label(ventana, text="Segundo apellido:")
    seg_apellido_txt.grid(row=2, column=0)
    segundo=str
    seg_apellido_entry = Entry(ventana,segundo)
    seg_apellido_entry.grid(row=2, column=1)
    
    ano_nac_txt = Label(ventana, text="Año de nacimiento:")
    ano_nac_txt.grid(row=3, column=0)
    anonac=str
    ano_nac_entry = Entry(ventana,textvariable=anonac)
    ano_nac_entry.grid(row=3, column=1)
    
    ano_curso_txt = Label(ventana, text="Año cursado:")
    ano_curso_txt.grid(row=4, column=0)
    anocur=str
    ano_curso_entry = Entry(ventana,textvariable=anocur)
    ano_curso_entry.grid(row=4, column=1)
    
    carrera_txt = Label(ventana, text="Carrera cursada:")
    carrera_txt.grid(row=5, column=0)
    carrera=str
    carrera_entry = Entry(ventana,textvariable=carrera)
    carrera_entry.grid(row=5, column=1)
    
    
   
   
    
ejer = Principal()
ejer.ventana.mainloop()