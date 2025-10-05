from elementos.personajes.personaje import Personaje

# Clase mago heredando de Personaje, sobreescribiendo el método atacar()
class Mago(Personaje):
    """
    Representa a un personaje de tipo mago.
    """

    # Sobeescribimos el método atacar() para refinarlo. Este método se ejecutará para el tipo Mago.
    # Los atributos y demás métodos se siguen heredando igual
    def atacar(self, hechizo: str):
        """
        Ataca al enemigo con hechizo.

        Parámetros:
        hechizo: str -- hechizo a utilizar
        """
        super().atacar(hechizo=hechizo)  # llamamos al método de la clase padre (reutilización)
        print("Recuerda, el valor no es saber cuando quitar una vida, sino cuando perdonarla.")  # extensión, añadimos funcionalidad extra al método
