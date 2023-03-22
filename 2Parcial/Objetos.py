
#1.- importar la clase
from Personaje import *

#2.- Instanciar un objeto
Heroe=Personaje()

#3.- Acceder a sus atributos
print("Ingresa atributos del personaje cuando se solicite")
especie = input(str("Ingresa la especie del personaje "))
nombre = input(str("Ingresa el nombre del personaje "))
altura = input("Ingresa la altura del personaje en metros ")
cargador = input(int("Ingresa la cantidad de municiones del personaje "))
print("")
print("Ingrese los atributos del villano cuando se solicite")
especieV = input(str("Ingrese la especie del villano "))
nombreV = input(str("Ingrese el nombre del villano "))
alturaV = input("Ingresa la altura del villano en metros ")

#4.-se crean los objetos

Heroe = Personaje(especie,nombre,altura)
villano = Personaje(especieV,nombreV,alturaV)

#5.-se acceden a metodos y atributos de los personajes

print('Los datos del heroe son: ')
print('El heroe es un '+Heroe.getEspecie()+' de nombre '+Heroe.getNombre()+' y mide '+str(Heroe.getAltura())+' metros')
print('')
print('')
print('Los datos del enemigo son: ')
print('El enemigo es un '+villano.getEspecie()+' de nombre '+villano.getNombre()+' y mide '+str(villano.getAltura())+' metros')


#6.- se llaman los metodos de cada objeto

Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(10)

