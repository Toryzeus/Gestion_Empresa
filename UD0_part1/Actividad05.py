"""
Posa un exemple de com passar diversos paràmetres des de consola a un programa Python 3.
Posa un exemple de com fer “sobrecàrrega de funcions” (funcions que poden rebre diversos
números de paràmetres), incloent-hi el cas de què el nombre de paràmetres no siga definit.
"""
import sys

"""SOBRECARGA CON PARÁMETROS DEFINIDOS"""
"""Creamos una función que recibe dos parámetros.
El parámetro "b" tiene un valor por defecto de 0.
Esto permite llamar a la función con uno o dos parámetros."""
def sumar(a,b=0): #se establece b con un valor por defecto
    return a+b

"""FUNCIÓN CON UN NÚMERO NO DEFINIDO DE PARÁMETROS"""
"""Utilizamos *numeros para poder recibir cualquier cantidadde parámetros.
Los parámetros que recibe la función se almacenan dentrode "numeros" como una tupla."""
def sumaNoDefinida(*numeros):
    resultado=0 # Empezamos el resultado en 0.

    """Recorremos todos los números recibidos."""
    for numero in numeros:
        """Vamos acumulando cada número en resultado."""
        resultado=numero+numero
    """Devolvemos el resultado final."""
    return resultado

"""Podemos llamar a la función pasando solamente un parámetro.
Como no indicamos "b", se utiliza el valor por defecto: 0."""
print(sumar(10)) # Resultado: 10

"""También podemos pasar los dos parámetros."""
print(sumar(15,5))# Resultado: 20

"""Podemos pasar tantos números como queramos."""
print(sumaNoDefinida(5,9,25,60))

"""PARÁMETROS PASADOS DESDE LA CONSOLA
sys.argv funciona como una lista que contiene los elementos escritos en la consola cuando ejecutamos el programa.
Por ejemplo, si ejecutamos:python3 Actividad05.py Angel 33 Español
tendremos:
sys.argv[0] -> Actividad05.py
sys.argv[1] -> Angel
sys.argv[2] -> 33
sys.argv[3] -> Español
Por eso empezamos a utilizar los datos que hemos escrito nosotros desde sys.argv[1]."""
print("Nombre",sys.argv[1])#Angel[1]
print("Edad",sys.argv[2])#33
print("Nacionalidad",sys.argv[3])#Español






