class Figura():
    def __init__(self,nombre, color):
        self.__nombre = nombre
        self.__color=color    
    
    def calcularArea(self):
        print("")
            
    def mostrarFigura(self):
        print("Nombre: ", self.__nombre)
        print("color: ", self.__color)
       
    def setNombre(self, nombre):
        self.setNombre= nombre
        
    def setColor(self,color):
        self.color= color
        
    def getNombre(self):
        return self.__nombre
    
    def getColor(self):
        return self.__color