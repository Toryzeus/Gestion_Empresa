"""
En Python 3 els tipus simples passen per valor i els compostos per referència.
Crea un exemple amb 3 funcions que:
● Reva 2 números i torne la suma.
● Reva una llista i modifique eixa mateixa llista (referència) doblant els valors de tots els
elements. No ha de retornar res.
● Reva una llista i torne una còpia de la llista mateixa llista (referència) doblant els valors de
tots els elements. La llista original no hi ha de modificar-se.
"""

"""Importamos el módulo copy.
Lo utilizaremos para crear una copia de una lista."""
import copy

"""FUNCIÓN SUMA

Esta función recibe dos números: a y b."""
def suma(a,b):
    """Devuelve el resultado de sumar los dos números."""
    return (a+b)

"""FUNCIÓN PARA MODIFICAR UNA LISTA"""

"""Esta función recibe una lista."""
def mutiplica_Lista(lista):
    """Recorremos todos los elementos de la lista.
    len(lista) nos indica cuántos elementos tiene."""
    for i in range(len(lista)):
        """Multiplicamos cada elemento por 10.
        Como estamos modificando directamente la lista que hemos recibido, también se modifica la lista
        original que utilizamos fuera de la función."""
        lista[i]=10*lista[i]
        """No utilizamos return porque la función modifica directamente la lista original."""

"""FUNCIÓN PARA COPIAR UNA LISTA"""

"""Esta función recibe una lista y devuelve una copia modificada de ella."""
def copiar_Lista(lista):
    """# Creamos una lista vacía."""
    lista_Copiada=[]
    """copy.copy() crea una copia de la lista original.
    De esta forma podemos modificar la copia sin modificar la lista original."""
    lista_Copiada=copy.copy(lista)
    for i in range(len(lista)):
        lista_Copiada[i]=lista_Copiada[i]*10

    return lista_Copiada

#Reva 2 números i torne la suma.
print("1-Reva 2 números i torne la suma.")
resultado=suma(2,3)
print("El resultado de la suma 2 + 3 es ",resultado)
print()

#Reva una llista i modifique eixa mateixa llista (referència) doblant els valors de tots elselements. No ha de retornar res.
print("2-Reva una llista i modifique eixa mateixa llista (referència) doblant els valors de tots elselements. No ha de retornar res.")
lista=[1,2,3,4,5,6]
mutiplica_Lista(lista)
print(lista)
print()

#Reva una llista i torne una còpia de la llista mateixa llista (referència) doblant els valors de tots els elements. La llista original no hi ha de modificar-se.
print("3-Reva una llista i torne una còpia de la llista mateixa llista (referència) doblant els valors de tots els elements. La llista original no hi ha de modificar-se.")
lista_Copiada=copiar_Lista(lista)
print(lista_Copiada)
print(lista)
