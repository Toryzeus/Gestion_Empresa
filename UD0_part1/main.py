from Car import Car
import random

"""Lista de colores disponibles"""
colores=["red","white","black","pink","blue"]

"""Creamos una lista de objetos"""
coches=[]

"""Pedimos el número de coches"""
n=int(input("¿Cuantos coches quieres? "))

"""Calculamos cuantos coches debemos imprimir
Si n es menor que 10, imprimimos n.
Si n es mayor o igual a 10, imprimimos 10"""
cantidad=min(n,10)

"""Creamos los objetos"""

for i in range(1,n+1):
    """La matricula sera consecutiva"""
    matricula=i

    """Elegimos el color aleatorio del coche"""
    color=random.choice(colores)

    """Creamos el objeto Car"""
    coche=Car(matricula,color)

    """Añadimos el coche a la lista"""
    coches.append(coche)

"""Imprimimos los coches"""
for i in range(cantidad):
    print("Coche Nº",i+1)
    coches[i].imprimir()

"""Cambiamos el color de un coche"""
numeroCoche=int(input("¿A que coche desea cambiarle el color? "))
coches[numeroCoche-1].cambiarColor(random.choice(colores))
print("Color cambiado")
print("Ahora el coche Nº",numeroCoche,"es")
coches[numeroCoche-1].imprimir()

"""Comprobamos si la matricula del coche es par"""
numeroCoche=int(input("¿A que coche desea saber si su matricula es par? "))
print(coches[numeroCoche-1].comprobarMatricula())