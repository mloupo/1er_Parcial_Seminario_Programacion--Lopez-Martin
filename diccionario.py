diccionario = {"Martin": "29628346",
               1234: "Romina",
               "Santiago": "458",
               165.5: "Pelota", }



def listaDeLlavesNumericas(diccionario):
    listaKeysNumericas = []
    for llave in diccionario:
        if ((type(llave) == int) or (type(llave) == float)):
            listaKeysNumericas.append(llave)
    return listaKeysNumericas

print(diccionario)
diccionario = listaDeLlavesNumericas(diccionario)
print(diccionario)


otroDiccionario = {"Martin": ["Pera", "Manzana", "Naranja"], "Paola": ["Anana", "Pomelo", "Sandia"],
                   "Santiago": ["Melon", "Pera"]}

def agregueGusto(diccionario, persona, gustoNuevo):
    if persona not in diccionario:
        diccionario[persona] = [gustoNuevo]
    else:
        if gustoNuevo in diccionario[persona]:
            print("El gusto ya existe en la lista")
        else:
            diccionario[persona] = diccionario[persona] + [gustoNuevo]
    return diccionario


print(otroDiccionario)
persona = input("Ingresa nombre: ")
gusto = input("Ingresa gusto: ")
otroDiccionario = agregueGusto(otroDiccionario, persona, gusto)
print(otroDiccionario)




# if persona in diccionario:
#    if diccionario[persona]!=gustoNuevo:
# listaModif = []
# for listaGustos in diccionario.values():
#     for gusto in listaGustos:
#         if gusto == gustoNuevo:
#             print("El gusto existe en la lista de gustos")
#         elif gusto not in listaGustos:
#             listaModif.append(gusto)

# diccionario[listaGustos]=listaModif
# if gustoNuevo in diccionario[persona]:
#     print(gustoNuevo)
# listaModif.append(gusto)



