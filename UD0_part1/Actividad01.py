import copy

#Clonar una llista.
print("1-Clonar una llista.")
#Metodo “shallow copy”
print("Metodo “shallow copy”")

lista=["azul","rojo","amarillo"]
print(lista)
lista_Clonada=lista
print(lista_Clonada)
print("ID de la lista principal",id(lista))
print("ID de la lista clonada",id(lista_Clonada))
lista[0]="verde"
print(lista)
#print(lista_Clonada)
print()
#Metodo “deep copy”
print("Metodo “deep copy”")
lista=["azul","rojo","amarillo"]
print(lista)
lista_Clonada=copy.copy(lista)
print(lista_Clonada)
print("ID de la lista principal",id(lista))
print("ID de la lista clonada",id(lista_Clonada))
lista[0]="verde"
print(lista)
print(lista_Clonada)
print()

#¿Quina és la diferència en Python entre “shallow copy” i “deep copy”?
print("1.1-¿Quina és la diferència en Python entre “shallow copy” i “deep copy”?")
print("El “shallow copy” crea un reflejo, si se modifica cualquiera elemento dentro del contenedor el cambio\nse percibira en ambas copias, en cambio el metodo “deep copy” crea una copia totalmente idependiente,\nsi cambiamos un elemento de un contenedor solo se modificara en ese contenedor")
print()

#Afegir un element a una llista.
print("2-Afegir un element a una llista.")
# usando append
print(lista)
lista.append("rubi")
print(lista)
#otro metodo es concatenando con +
lista=lista+lista_Clonada
print(lista)
lista=lista+["zafiro"]
print(lista)
print()

#Llevar un element a una llista.
print("3-Llevar un element a una llista.")
#Se puede borrar el ultimo de la lista
print(lista)
lista.pop()
print(lista)
#o una posicion en especifico
lista.pop(5)
print(lista)
print()

#Crear una nova llista amb els 4 últims elements d’una llista
print("4-Crear una nova llista amb els 4 últims elements d’una llista")
lista_Nueva=[]
for i in range(2,len(lista)):
    lista_Nueva.append(lista[i])
print(lista_Nueva)
print()

#Convertir les paraules d’una cadena (separades per espai) a una llista.
print("6-Convertir les paraules d’una cadena (separades per espai) a una llista.")
cadena="Hola Oscar ¿Que tal?"
lista_Cadena=cadena.split()
print(lista_Cadena)
print()

#Comentaris amb una línia.
print("7-Comentaris amb una línia.")
#Para los comentarios de una linea se usa el #
print("Para los comentarios de una linea se usa el # al principio de la linea")
print()
#Comentaris multilínia.
print("8-Comentaris multilínia.")
"""
Para comentario multilinea se tiene que cerrar el comentario entre comillas triples
"""
print("Para comentario multilinea se tiene que cerrar el comentario entre comillas triples")

print(lista_Cadena.index("Oscar"))