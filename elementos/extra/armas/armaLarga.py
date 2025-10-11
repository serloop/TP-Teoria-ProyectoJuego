from elementos.extra.armas.arma import Arma
from elementos.extra.armas.tipoArma import TipoArma

class ArmaLarga(Arma):
    """
    Representa un arma de larga distancia
    """

    def __init__(self, nombre: str, dueño: 'Personaje'):
        """
        Crea un arma de larga distancia

        Parámetros:
        nombre: str -- nombre del arma
        dueño: Personaje -- personaje dueño del arma
        """
        super().__init__(nombre,TipoArma.LARGA_DISTANCIA, dueño)
        self._daño = 30     # Ocultación

    def usar(self, objetivo: 'Personaje') -> bool:
        """
        Ataca con el arma a un objetivo

        Parámetros:
        objetivo: Personaje -- personaje objetivo

        Returns:
        bool -- True si el ataque se ha realizado con éxito, False en caso contrario
        """
        print(f"{self.get_dueño().get_nombre()} ataca a {objetivo.get_nombre()} con {self.get_nombre()}")
        objetivo.recibir_daño(self._daño)
        return True

    def mejorar(self):
        """
        Mejora el arma
        """
        self._daño += 10
        self._nivel += 1
        print(f"{self._nombre} ha sido mejorada a nivel {self._nivel}")