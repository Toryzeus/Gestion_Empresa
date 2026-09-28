"""
Crea un llistat en el qual cada element d’eixa llista siga una llista amb dos valors: mida i pes.
Utilitzant https://docs.python.org/3/howto/sorting.html i las “key functions”, fer que aquesta llista
s’ordene per major altura i en cas d’igualtat, per menor pes.
Explica en comentaris que és realment la “key function”. Pista: en l’ajuda diuen
“The value of the key parameter should be a function (or other callable) that takes a single
argument and returns a key to use for sorting purposes. This technique is fast because the key
function is called exactly once for each input record.”.
"""



"""
KEY FUNCTION


La "key function" es una función que recibe UN elemento de la lista y devuelve el valor que se utilizará para
decidir cómo ordenar ese elemento.
Por ejemplo, si recibe:
[180, 75]
devuelve:
(-180, 75)
La función se ejecuta una vez para cada elemento de la lista.
Utilizamos -altura porque queremos ordenar la altura de MAYOR a MENOR.
Utilizamos peso sin modificar porque queremos ordenar
el peso de MENOR a MAYOR cuando las alturas sean iguales.
"""
def funcionKey(lista):
    altura=lista[0]
    peso=lista[1]
    return (-altura,peso)

"""
Creamos una lista en la que cada elemento es otra listacon dos valores:[altura, peso]
La altura está expresada en centímetros y el peso en kilogramos.
"""
lista=[[180, 75],
    [170, 80],
    [180, 70],
    [165, 60],
    [190, 90],
    [170, 70],
    [180, 80]]

"""Ordenamos la lista utilizando nuestra key function."""
lista.sort(key=funcionKey)

"""# Mostramos la lista ordenada."""
print(lista)