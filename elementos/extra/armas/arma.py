from abc import ABC, abstractmethod

from elementos.extra.armas.tipoArma import TipoArma


class Arma(ABC):
    """
    Representa un arma del juego
    """
    def __init__(self, nombre: str, tipo: TipoArma, dueño: 'Personaje'):
        """
        Crea un arma con un nombre, daño, tipo, dueño y balas

        Parámetros:
        nombre: str -- nombre del arma
        daño: float -- daño del arma
        tipo: TipoArma -- tipo del arma
        dueño: Personaje -- personaje dueño del arma
        """

        self._nombre: str = nombre
        self._tipo: TipoArma = tipo
        self._dueño: 'Personaje' = dueño
        self._daño: float = None # Depende del tipo de arma que se instancie (subclase)
        self._nivel: int = 1

    def get_nombre(self) -> str:
        """
        Devuelve el nombre del arma

        Returns:
        str -- nombre del arma
        """
        return self._nombre

    def get_daño(self) -> float:
        """
        Devuelve el daño del arma

        Returns:
        float -- daño del arma
        """
        return self._daño

    def get_tipo(self) -> TipoArma:
        """
        Devuelve el tipo del arma

        Returns:
        TipoArma -- tipo del arma
        """
        return self._tipo

    def get_dueño(self) -> 'Personaje':
        """
        Devuelve el dueño del arma

        Returns:
        Personaje -- personaje dueño del arma
        """
        return self._dueño

    def get_nivel(self) -> int:
        """
        Devuelve el nivel del arma

        Returns:
        Nivel -- valor del nivel del arma
        """
        return self._nivel

    def __str__(self):
        return f"Arma: {self.get_nombre()} - Daño: {self.get_daño()} - Tipo: {self.get_tipo()} - Nivel: {self.get_nivel()}"

    @abstractmethod
    def usar(self, objetivo: 'Personaje') -> bool:
        """
        Usa el arma contra un objetivo
        CADA ARMA SE USA DE UNA MANERA DIFERENTE

        Parámetros:
        objetivo: Personaje -- personaje objetivo
        """
        pass

    @abstractmethod
    def mejorar(self):
        """
        Mejora el arma
        CADA ARMA SE MEJORA DE UNA MANERA DIFERENTE
        """
        pass