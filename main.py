from controladora import *


cont = controladora()
Cuad = Cuadrado("Cuad", "Rojo", 2, 4)
Triang = Triangulo("Triang", "verde", 2, 4)
Circ = Circulo("Circ", "azul", 10)
cont.listaFiguras.append(Cuad)
cont.listaFiguras.append(Triang)
cont.listaFiguras.append(Circ)

while True:
    print("\nSeleccione una de las siguientes opciones:")
    print("\t1.- Agregar Figura")
    print("\t2.- Mostrar lista Figuras")
    print("\t3.- Calcular Area Figuras")
    print("\t4.- Eliminar lista de Figura")
    print("\t0.- Salir\n")

    opcion = int(input("Opcion: "))
    if opcion == 1:
        figura = cont.agregarFigura()
        cont.listaFiguras.append(figura)
    elif opcion == 2:
        cont.mostrarListaFiguras()
    elif opcion == 4:
        cont.borraListado()
    elif opcion == 3:
        cont.calcularAreaFiguras()
    elif opcion == 0:
        exit()


  


    
    
    
    
# cuad1= Cuadrado("Caudrado1", "Negro", 2, 4)
# triang1=Triangulo("Triangulo1", "Rojo", 10)
# circ1=Circulo()
# cuad1.mostrarFigura()
# print(cuad1.calcularArea())




