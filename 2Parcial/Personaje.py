
class Personaje:
    
    #constructor
    def __init__(self,esp,nom,alt):
        self.especie = esp
        self.__nombre = nom
        self.altura = alt
    
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
        print("El arma tiene ahora " , str(cargador) , " balas")
        
    #se declaran getters y setters
    
    def getEspecie(self):
        return self.__especie
    
    def setEspecie(self,esp):
        self.__especie = esp
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nom):
        self.__nombre = nom
    
    def getAltura(self):
        return self.__altura
    
    def setAltura(self,alt):
        self.__altura = alt 