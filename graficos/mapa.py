from graficos.dibujable import IDibujable

class Mapa:
    """
    Mapa del juego que maneja las posiciones de los objetos dibujables en el mapa y realiza el movimiento de los mismos.

    Maneja también las interacciones entre los objetos y el mapa.
    """

    def __init__(self):
        self._elementos: list[IDibujable] = [] # Lista de elementos que implementan la interfaz IDibujable

    def get_elementos(self):
        return self._elementos

    def agregar_elemento(self, elemento: IDibujable):
        """
        Añade un elemento al mapa.

        Parámetros:
        elemento: IDibujable -- elemento a añadir al mapa
        """
        self.get_elementos().append(elemento)  # lista de dibujables
        print(f"Elemento {type(elemento).__name__} añadido al mapa.")

    def dibujar_mapa(self):
        """
        Dibuja todos los elementos en el mapa.
        """
        print("Dibujando el mapa:")
        for elemento in self.get_elementos():
            elemento.dibujar()

    def mover_elemento(self, elemento: IDibujable, nueva_posicion: tuple[int, int]):
        """
        Mueve un elemento a una nueva posición en el mapa.
        Si hay alguien, interactúa con él

        Parámetros:
        elemento: IDibujable -- elemento a mover
        nueva_posicion: tuple[int, int] -- nueva posición del elemento
        """
        if elemento in self.get_elementos():
            # Comprobar si la nueva posición está ocupada
            elemento2: IDibujable = self._comprobar_posicion(nueva_posicion)
            elemento.mover(nueva_posicion)
            if not elemento2:
                print(f"La nueva posición está libre. Movemos a {elemento} a la posición {nueva_posicion}")
            if elemento2:
                print(f"Esta posición también está ocupada por {elemento2}. Interactuamos con él.")
                elemento.interactuar(elemento2)
        else:
            print(f"El elemento {type(elemento).__name__} no se encuentra en el mapa.")

    def _comprobar_posicion(self, posicion: tuple[int, int]) -> IDibujable:
        """
        Devuelve el objeto en la posición dada.

        Parámetros:
        posicion: tuple[int, int] -- posición a comprobar
        """
        # Usamos la estructura for-if-return por facilitar la comprensión del código. Debería ser un while
        for elemento in self.get_elementos():
            if elemento.obtener_posicion() == posicion:
                return elemento
        return None