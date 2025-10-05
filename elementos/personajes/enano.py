from elementos.personajes.personaje import Personaje
from elementos.extra.mascota import Mascota
from elementos.personajes.raza import Raza

# Clase enano heredando de Personaje, ocultando el atributo dinero
class Enano(Personaje):
    """
    Representa a un personaje de tipo enano
    """

    # Los enanos pueden tener un nombre, un equipo y una mascota.
    def __init__(self, equipo: str = None, nombre=None, mascota: Mascota = None):
        """
        Constructor de la clase Enano

        Parámetros:
        equipo: str -- equipo al que pertenece el enano
        nombre: str -- nombre del enano
        mascota: Mascota -- mascota del enano
        """
        # Llamamos al constructor de la clase padre, pasándole los parámetros necesarios
        # Observa como aquí pasamos la raza y que son siempre aliados.
        super().__init__(raza=Raza.ENANO, aliado=True, equipo=equipo, nombre=nombre, mascota=mascota)
        # Recuerda que tendremos dinero, un inventario de objetos, amigos, mascota, arma, etc.
        self._dinero = 1000  # como buenos comerciantes, los enanos podría iniciarse con 1000 monedas (ocultación del atributo del padre con el mismo nombre)
