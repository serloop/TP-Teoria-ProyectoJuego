from elementos.personajes.personaje import Personaje
from elementos.personajes.raza import Raza

# Clase ent heredando de personaje, ocultando todos los atributos pues no los necesita
class Ent(Personaje):
    """
    Representa a un personaje de tipo Ent (árbol viviente)
    """

    # No heredamos los atributos de la clase padre, no los necesitamos.
    # El personaje de tipo Ent sólo necesita un nombre.
    # Por ejemplo, no tiene dinero, ni es aliado ni pertenece a un equipo.
    # Tampoco tendrá listado de amigos ni inventario de objetos, ni arma.
    def __init__(self, nombre: str):
        """
        Constructor de la clase Ent

        Parámetros:
        nombre: str -- nombre del ent
        """
        self._nombre = nombre
        self._tipo = Raza.ENT  # Ocultación de atributos, no se heredan de la clase padre

    # IMPORTANTE: El resto de métodos y funcionalidades de la clase padre se heredan igualmente
    # Las funcionalidades relacionadas con los atributos que hemos ocultado pueden fallar (no existen).
    # Por ejemplo, no se puede dar monedas, ni quitar monedas, ni comprobar si tiene dinero.
    # Habría que sobreescribirlos en esta clase y devolver que no es posible:

    # Por ejemplo, sobreescritura:
    def añadir_moneda(self) -> bool:
        """
        Intenta añadir una moneda al Ent (no se puede hacer)
        """
        print("Los Ents no saben lo que es el dinero")
        return False

    # ¿Debería ser realmente la clase Ent una subclase Personaje si no se va a beneficiar de todo lo que tiene un personaje?
    # ¿Es un Ent realmente una particularización de un personaje?