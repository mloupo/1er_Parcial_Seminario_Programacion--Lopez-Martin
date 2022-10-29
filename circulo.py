from figura import *
from math import pi as PI

class Circulo(Figura):
    
    def __init__(self, nombre, color, radio):
        self.__radio= radio
        super().__init__(nombre, color)
    
    
    def calcularArea(self):
        area= PI * (self.__radio*self.__radio)
        return area
    
    def mostrarFigura(self):
        super().mostrarFigura()
        print("Radio: ", self.__radio)
       
    def setRadio(self, radio):
        self.__radio= radio
        
    def getRadio(self):
        return self.__radio