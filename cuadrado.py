from figura import *
class Cuadrado(Figura):
    def __init__(self, nombre, color, base, altura):
        self.__base=base
        self.__altura = altura
        super().__init__(nombre, color)   
        
  
    def mostrarFigura(self):
        super().mostrarFigura()        
        print("Base: ", self.__base)
        print("Altura: ", self.__altura)
        
    def calcularArea(self):
        area = self.__base * self.__altura
        return area

    def setBase(self, base):
        self.__base= base
       
    def setAltura(self, altura):
        self.__altura= altura
    
    def getBase(self):
        return self.__base
    
    def getAltura(self):
        return self._altura