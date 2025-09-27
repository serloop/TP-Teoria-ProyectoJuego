class Objeto:
    
    def __init__(self, nombre: str, descripcion: str):
        """
        Crea un objeto con un nombre y una descripción

        Parámetros:
        nombre: str -- nombre del objeto
        descripcion: str -- descripción
        """
        self._nombre: str = nombre
        self._descripcion: str = descripcion

    def usar_objeto(self) -> None:
        print(f"Se ha usado el objeto {self._nombre}")

    def __str__(self):
        """
        Devuelve el objeto en formato string
        """
        return f"{self._nombre}: {self._descripcion}"