from elementos.personajes.personaje import Personaje

# Clase Hobbit, heredando de personaje pero particularmente, los hobbits no atacan
class Hobbit(Personaje):
    """
    Representa a un personaje de tipo hobbit.
    """

    # Sobreescribimos el método atacar() para un comportamiento particular. Ahora en esta subclase se ejecuta este método sin parámetros.
    # Los atributos y demás métodos se siguen heredando igual
    def atacar(self):
        """
        Aunque se lo indiques, los hobbits son seres tranquilos que no atacan
        """
        print("Los hobbits no atacan")