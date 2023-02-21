
#1.- importar la clase
from Personaje import *

#2.- Instanciar un objeto
Heroe=Personaje()

#3.- Acceder a sus atributos
print("Atributos del personaje")
print("El personaje pretenece a la raza: " , Heroe.especie)
print("El personaje se llama: " , Heroe.nombre)
print("El personaje mide: " , str(Heroe.altura) , " metros")

#4.- Acceder a los metodos
print("Metodos del personaje")
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(68)
