
class Personaje:
    
    #atributos del personaje
    
    especie = "Humano"
    nombre = "Jhon Cena"
    altura = 1.20
    
    #Metodos Personaje
    
    def correr(self, status):
        if(status):
            print("El personaje " , self.nombre , " está corriendo")
        else:
            print("El personaje " , self.nombre , " se detuvo")
            
    def lanzarGranada(self):
        print("Se lanzo granada ")
        
    def recargarArma(self, municiones):
        cargador = 5
        cargador = cargador + municiones
        print("El arma tiene ahora " , cargador , " balas")
        