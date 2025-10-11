from elementos.extra.armas.arma import Arma
from elementos.extra.armas.tipoArma import TipoArma


class ArmaCorta(Arma):
    """
    Representa un arma de corta distancia
    """

    def __init__(self, nombre: str, dueño: 'Personaje', numero_estocadas: int):
        """
        Crea un arma de corta distancia

        Parámetros:
        nombre: str -- nombre del arma
        daño: float -- daño del arma
        dueño: Personaje -- personaje dueño del arma
        numero_estocada: int -- número de estocadas por uso
        """
        super().__init__(nombre, TipoArma.CORTA_DISTANCIA, dueño)
        self._daño = 10  # Ocultación
        self._numero_estocadas = numero_estocadas # Nuevo atributo sobre la clase Arma

    def get_numero_estocadas(self) -> int:
        """
        Devuelve el número de estocadas del arma

        Returns:
        int -- número de estocadas
        """
        return self._numero_estocadas

    def usar(self, objetivo: 'Personaje') -> bool:
        """
        Ataca con el arma a un objetivo

        Parámetros:
        objetivo: Personaje -- personaje objetivo

        Returns:
        bool -- True si el ataque se ha realizado con éxito, False en caso contrario
        """
        print(f"{self.get_dueño().get_nombre()} ataca con {self.get_numero_estocadas()} estocadas a {objetivo.get_nombre()} con {self.get_nombre()}")

        for _ in range(self.get_numero_estocadas()):
            objetivo.recibir_daño(self.get_daño())

        return True

    def mejorar(self):
        """
        Mejora el arma
        """
        self._daño += 5
        self._numero_estocadas += 1
        self._nivel += 1
        print(f"{self.get_nombre()} ha sido mejorada a nivel {self.get_nivel()}")

    def __str__(self):  # Sobreescritura de método (extensión)
        """
        Devuelve una representación en forma de cadena del arma
        """
        return super().__str__() + f" - Estocadas: {self.get_numero_estocadas()}"