from elementos.extra.armas.arma import Arma
from elementos.extra.armas.tipoArma import TipoArma


class ArmaFuego(Arma):
    """
    Representa un arma de fuego
    """

    def __init__(self, nombre: str, dueño: 'Personaje', balas: int):
        """
        Crea un arma de fuego

        Parámetros:
        nombre: str -- nombre del arma
        daño: float -- daño del arma
        dueño: Personaje -- personaje dueño del arma
        balas: int -- número de balas
        """
        super().__init__(nombre, TipoArma.FUEGO, dueño)
        self._daño = 40  # Ocultación
        self._balas = balas  # Nuevo atributo

    def get_balas(self):
        """
        Devuelve el número de balas restantes del arma

        Returns:
        int -- número de balas
        """
        return self._balas

    def usar(self, objetivo: 'Personaje') -> bool:
        """
        Ataca con el arma a un objetivo

        Parámetros:
        objetivo: Personaje -- personaje objetivo

        Returns:
        bool -- True si el ataque se ha realizado con éxito, False en caso contrario
        """
        if self.get_balas() > 0:
            objetivo.recibir_daño(self._daño)
            self._balas -= 1
            return True
        else:
            print("No hay balas")
            return False

    def mejorar(self):
        """
        Mejora el arma
        """
        self._daño += 20
        self._nivel += 1
        print(f"{self.get_nombre()} ha sido mejorada a nivel {self.get_nivel()}")

    def recargar(self, balas: int):
        """
        Recarga el arma con balas

        Parámetros:
        balas: int -- número de balas
        """
        self._balas += balas

    def __str__(self): # Sobreescritura de método (extensión)
        """
        Devuelve una representación en forma de cadena del arma
        """
        return super().__str__() + f" - Balas: {self.get_balas()}"