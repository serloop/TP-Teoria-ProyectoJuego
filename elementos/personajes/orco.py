from elementos.extra.mascota import Mascota
from elementos.personajes.personaje import Personaje
from elementos.personajes.raza import Raza

# Clase orco heredando de Personaje, ocultando el atributo dinero
class Orco(Personaje):
    """
    Representa a un personaje de tipo orco
    """

    # Los orcos siempre tienen un jefe, y pueden tener un nombre si tienen suerte.
    def __init__(self, jefe: Personaje, nombre: str = None):
        """
        Constructor de la clase Orco

        Parámetros:
        jefe: Orco -- jefe del orco
        nombre: str -- nombre del orco
        """

        # Llamamos al constructor de la clase padre, pasándole los parámetros necesarios
        # Observa como aquí pasamos la raza y que son siempre enemigos.
        super().__init__(raza=Raza.ORCO, aliado=False, nombre=nombre, equipo="Ejército de Mordor")  # no hay ocultación

        # Un orco sólo puede tener un jefe de tipo Orco
        if isinstance(jefe, Orco) or type(jefe) == Orco:  # ambos son equivalentes en este caso
            self._jefe: Orco = jefe  # atributo propio de la clase Orco
        else:
            print("El jefe de un orco debe ser otro orco")
            self._jefe: Orco = None  # si no es un orco, no tiene jefe

        self._amigos.append(jefe)  # añadimos al jefe como amigo (el listado de amigos vacío se hereda de la clase padre)

        self.set_mascota(Mascota(nombre="Lobo", raza=Raza.HUARGO, nivel=5))  # todos los orcos tiene asociado un Huargo
        # RECUERDA. Tenemos acceso a todos los métodos heredados (públicos y protegidos) de la clase Personaje, como set_mascota()

    # Refinamiento del método mágico str, pues hemos añadidos atributos propios
    def __str__(self) -> str:
        """
        Método mágico para representar el objeto como string
        """
        if self._jefe:
            return f"Orco {self._nombre} de raza {self.raza.name} ({self._equipo}) con jefe {self._jefe.get_nombre()}"
        else:
            return f"Orco {self._nombre} de raza {self.raza.name} ({self._equipo}) sin jefe"

    # Un orco dispara 3 balas a la vez, en lugar de una como el resto
    def disparar(self) -> bool:
        """
        Dispara el arma del orco, si tiene una. Dispara tres balas a la vez.
        """
        # while no se hayan disparado las tres balas y se siga disparando, disparo
        i = 0
        while i < 3 and super().disparar():
            i += 1