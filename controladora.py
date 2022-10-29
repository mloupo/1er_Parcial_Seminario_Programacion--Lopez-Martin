from figura import *
from circulo import *
from cuadrado import *
from triangulo import *

class controladora():
        
    def __init__(self):
        self.listaFiguras=[]
        
    def agregarFigura(self):
        print("\nSeleccione tipo de figura: ")
        print("\t1. Cuadrilatero")
        print("\t2. Triangulo")
        print("\t3. Circulo")
        opcion = int(input("Opcion: "))
        if opcion == 1:
            nombre = (input("Ingrese nombre: "))
            color = (input("Ingrese color: "))
            base = int(input("Ingrese base: "))
            altura = int(input("Ingrese altura: "))
            unCuadrado = Cuadrado(nombre, color, base, altura)
            return unCuadrado

        elif opcion == 2:
            nombre = (input("Ingrese nombre: "))
            color = (input("Ingrese color: "))
            base = int(input("Ingrese base: "))
            altura = int(input("Ingrese altura: "))
            unTriangulo = Triangulo(nombre, color, base, altura)
            return unTriangulo
        elif opcion == 3:

            nombre = (input("Ingrese nombre: "))
            color = (input("Ingrese color: "))
            radio = int(input("Ingrese radio: "))           
            unCirculo = Circulo(nombre, color, radio)
            return unCirculo
        else:
            print("La opcion no existe")

    def borraListado(self):
        self.listaFiguras.clear()
    
    def mostrarListaFiguras(self):
        print("Mostrar listado Figuras\n")
        if len(self.listaFiguras) > 0:
            for i in self.listaFiguras:
                i.mostrarFigura()
                print("------------------------")
            input("Pulsa una tecla para continuar..")
        else:
            print("La lista de figuras esta vacia")    
            
    def calcularAreaFiguras(self):
        for figura in self.listaFiguras:               
            print("El area de", figura.getNombre() ,"es :", figura.calcularArea())
        input("Pulsa una tecla para continuar..")
        print("------------------------")
