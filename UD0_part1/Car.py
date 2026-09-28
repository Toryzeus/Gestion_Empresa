"""Defineix la classe Car en Python 3. La classe tindrà com atributs “matrícula” (numèrica) i “color”.
Crea un mètode imprimir, i a més dos mètodes que vulgues.
En segon lloc, fes que el programa demane un número “n” per teclat i es creen “n” instàncies de la
classe, on cada instància:
● Cada “matrícula” tindrà un número consecutiu des d’1 fins a “n”.
● El “color” serà per a cada instància un color aleatori obtingut d’aquest llistat [“red”, “white”,
“black”, “pink”, “blue”]
Finalment, el programa haurà d’imprimir els valors de les 10 primeres instàncies. En cas que “n”
siga menor que 10, només imprimirà “n” instàncies.
"""

"""Definimos la clase Car"""
class Car:
    """Constructor de la clase"""
    def __init__(self,matricula, color):
        """Atributo matrícula"""
        self.matricula = matricula
        """Atributo color"""
        self.color = color

    """Método para imprimir los datos del coche"""
    def imprimir(self):
        print("Matricula: ", self.matricula)
        print("Color: ", self.color)

    """Segundo método: cambiar el color del coche"""
    def cambiarColor(self,nuevoColor):
        self.color = nuevoColor

    """Tercer método: comprobar si la matrícula es par"""
    def comprobarMatricula(self):
        if(self.matricula %2 == 0):
            texto="Matricula par"
        else:
            texto="Matricula impar"
        return texto

