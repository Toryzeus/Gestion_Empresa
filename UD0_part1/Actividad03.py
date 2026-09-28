"""
Partint d’un context en què volem emmagatzemar un usuari i la seua contrasenya. Fes un exemple
que explica com es faria:
● Utilitzant una llista.
● Utilitzant un diccionari.
En omplir-se, les contrasenyes han de passar-se a un format Hash (per exemple SHA
https://recursospython.com/guias-y-manuales/hashlib-md5-sha/ ). L’exemple ha d’omplir la llista
amb 5 usuaris/contrasenya i fer dues consultes.
"""



"""UTILIZANDO UNA LISTA"""
def listaCifrada():
    """Importamos hashlib para poder cifrar las contraseñas."""
    import hashlib
    """Creamos dos listas
    Una para guardar los nombres de usuario."""
    listaUsuarios=[]
    """Otra para guardar las contraseñas cifradas."""
    listaContra=[]
    """Repetimos el proceso 5 veces para introducir
    5 usuarios y sus respectivas contraseñas."""
    for i in range(5):
        """Pedimos el nombre de usuario."""
        ususario=input("Introduce  tu nombre de usuario: ")
        """Añadimos el usuario a la lista de usuarios."""
        listaUsuarios.append(ususario)
        """Pedimos la contraseña."""
        contra=input("Introduce la contraseña: ")
        """Convertimos la contraseña a bytes con encode() y después la ciframos utilizando SHA-1.
        hexdigest() convierte el resultado en texto hexadecimal."""
        contraCifrada=hashlib.sha1(contra.encode()).hexdigest()
        """Mostramos la contraseña cifrada."""
        print(contraCifrada)
        """Guardamos la contraseña cifrada en la lista."""
        listaContra.append(contraCifrada)

    """Realizamos 2 consultas para buscar las contraseñas cifradas de diferentes usuarios."""
    for i in range(2):
        """Preguntamos qué usuario queremos consultar."""
        print("¿De que usuario le gustaria ver la contraseña cifrada?")
        """Mostramos todos los usuarios disponibles."""
        print(listaUsuarios)
        """Pedimos el usuario que queremos buscar."""
        ususario=input()
        """.index() busca la posición que ocupa el usuario dentro de la lista de usuarios."""
        numUsuario=listaUsuarios.index(ususario)
        """Utilizamos la posición encontrada para acceder # a la contraseña correspondiente en listaContra."""
        print("La contraseña cigrada del usuario ", ususario," es: ",listaContra[numUsuario])

"""UTILIZANDO UN DICCIONARIO"""
def diccionarioCifrada():
    """Importamos hashlib para poder cifrar las contraseñas."""
    import hashlib
    """Creamos un diccionario vacío. 
    El usuario será la clave y la contraseña cifrada será el valor."""
    listaUsuarios={}
    """Repetimos el proceso 5 veces para introducir 5 usuarios y sus contraseñas."""
    for i in range(5):
        """Pedimos el nombre de usuario."""
        ususario=input("Introduce  tu nombre de usuario: ")
        """Pedimos la contraseña."""
        contra=input("Introduce la contraseña: ")
        """Convertimos la contraseña a bytes y la ciframos utilizando SHA-1."""
        contraCifrada = hashlib.sha1(contra.encode()).hexdigest()
        """Guardamos en el diccionario: clave = usuario valor = contraseña cifrada"""
        listaUsuarios[ususario]=contraCifrada

    """Realizamos 2 consultas."""
    for i in range(2):
        """Preguntamos qué usuario queremos consultar."""
        print("¿De que usuario le gustaria ver la contraseña cifrada?")
        """Mostramos las claves del diccionario, es decir, los nombres de los usuarios."""
        print(listaUsuarios.keys())
        """Pedimos el usuario que queremos consultar."""
        ususario=input()
        """Recorremos todos los elementos del diccionario.
        "u" representa el usuario y "c" la contraseña cifrada."""
        for u, c in listaUsuarios.items():
            """Comprobamos si el usuario que hemos introducido coincide con alguno de los usuarios del diccionario."""
            if u == ususario:
                """Si coincide, mostramos la contraseña cifrada."""
                print("La contraseña cigrada del usuario ", ususario," es: ",c)

"""MENÚ PRINCIPAL
Pedimos al usuario que seleccione una opción.
1 -> Utilizar listas.
2 -> Utilizar diccionarios.
int() convierte el valor introducido por teclado de texto a número entero."""
opcion=int(input("¿Que opcion desea?\n1-Listas\n2-Diccionarios\n"))
"""Si el usuario selecciona 1, llamamos a la función listaCifrada()."""
if(opcion==1):
    listaCifrada()
    """Si selecciona 2, llamamos a la función diccionarioCifrada()."""
elif(opcion==2):
    diccionarioCifrada()
    """Si introduce cualquier otro número, mostramos un mensaje de error."""
else:
    print("Opcion no valida")