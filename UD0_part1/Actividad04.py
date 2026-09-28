

"""OPERADOR "is"""


"""None se utiliza para indicar que una variable no tieneningún valor."""
nombre = None

""" is None comprueba si la variable contiene el valor None.
En este caso, como nombre es None, se ejecuta el if."""
if nombre is None:
    print("nombre vacio")



"""OPERADOR "is" CON LISTAS"""


"""Creamos una lista y la guardamos en la variable a."""
a = [1, 2, 3]

"""b apunta al mismo objeto que "a"."""
b = a

"""c es una lista nueva e independiente.
Aunque tenga los mismos valores que "a", es otro objeto."""
c = [1, 2, 3]

"""True porque "a" y "b" hacen referencia al mismo objeto."""
print(a is b)

"""False porque "a" y "c" son objetos diferentes, aunque tengan exactamente los mismos valores."""
print(a is c)



"""OPERADOR not"""


"""not sirve para negar o invertir una condición.
Si una condición es True, "not" la convierte en False.
Si es False, "not" la convierte en True."""

numero2 = 20

"""Comprobamos si numero2 NO es mayor o igual que 18.
20 >= 18 es True.
not True es False, por lo que el mensaje no se muestra."""
if not numero2 >= 18:
    print("es menor de 18 años")


"""También podemos utilizar "not" para negar una comparación."""

usuari = "angel"

"""Comprobamos que el usuario NO sea igual a "admin".
"angel" == "admin" es False.
not False es True, por lo que se ejecuta el print."""
if not usuari == "admin":
    print("No és el administrador")



"""OPERADOR in"""


"""in sirve para comprobar si un elemento se encuentra
dentro de una lista, cadena de texto u otra colección."""

lista = ["Angel", "Paco", "Lucas"]

"""Comprobamos si "Angel" está dentro de la lista.
Como "Angel" sí está, la condición es True."""
if "Angel" in lista:
    print("Angel esta en la lista")


"""También podemos utilizar "in" con una cadena de texto."""

paraula = "Python"

"""Comprobamos si la letra "P" está dentro de la palabra.
Como "P" está en "Python", devuelve True."""
print("P" in paraula)

"""Comprobamos si la letra "z" está dentro de la palabra.
Como "z" no está en "Python", devuelve False."""
print("z" in paraula)
