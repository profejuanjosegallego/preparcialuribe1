#Algoritmo 1: Crea una lista de 5 ingenieros (1 ingeniero es un diccionario)
def crear_lista_ingenieros(cantidaIngenieros):
    ingenieros=[]
    for _ in range(cantidaIngenieros):
        nuevoIngeniero={}
        nuevoIngeniero["id"]=int(input("id: "))
        nuevoIngeniero["nombres"]=input("nombres: ")
        ingenieros.append(nuevoIngeniero)
    return ingenieros 

#Funcion para crear una lista de 20 o N mediciones forma aleatoria