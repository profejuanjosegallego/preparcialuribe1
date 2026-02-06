#Algoritmo 1: Crea una lista de 5 ingenieros (in ingeneiro es un diccioanrio)

#creo la lista
lista=[]

for _ in range(1,6):
    
    #creo el diccionario
    diccionario={}
    
    #Poblando el diccionario (Necesito que el id se un entero generado por python de forma aleatoria no negativo)(Necesito que el id sea una cadena alfanumerica)
    diccionario["id"]=int(input("Digita el id del empleado: "))
    #Estas variables deben convertirse en claves o atributos del diccionario
    '''nombres=input("Digita los nombres empleado")
    documento=input("Digita el documento: ")
    correo=input("Digita el correo: ")
    contraseña=input("Digita la contraseña: ")'''

    #Agregar un elemento (Diccionario) a una lista
    lista.append(diccionario)

print(lista)





