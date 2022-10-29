from figura import *



class Triangulo(Figura):

    def __init__(self, nombre, color, base, altura):
        self.__base = base
        self.__altura = altura
        super().__init__(nombre, color)

    def calcularArea(self):
        area = (self.__base * self.__altura)/2
        return area

    def mostrarFigura(self):
        super().mostrarFigura()
        print("Base: ", self.__base)
        print("Altura: ", self.__altura)
