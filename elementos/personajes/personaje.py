import random

from elementos.errores.errores import ArmaError, ArmaVaciaError
from elementos.extra.armas.armaCorta import ArmaCorta
from elementos.extra.armas.armaFuego import ArmaFuego
from elementos.extra.armas.armaLarga import ArmaLarga
from elementos.personajes.raza import Raza
from elementos.extra.mision import Mision
from elementos.extra.armas.arma import Arma, TipoArma
from elementos.extra.objeto import Objeto
from graficos.dibujable import IDibujable


class Personaje(IDibujable):
    """
    Representa a un personaje del juego
    """

    numero_personajes: int = 0

    @classmethod
    def get_numero_personajes(cls)->int:
        """
        Devuelve el número de personajes creados

        Returns:
        int -- número de personajes creados hasta ahora
        """
        return cls.numero_personajes

    @staticmethod
    def describir_razas():
        """
        Muestra las razas de personaje disponibles
        """
        print("Existen las siguientes razas:")
        for raza in Raza:
            print(raza.name)

    # Constructor explícito sobrecargado
    def __init__(self, raza: Raza, aliado: bool = None, equipo: str = None, nombre=None, mascota: 'Mascota' = None):
        """
        Constructor de la clase Personaje. Sobrecargado para permitir diferentes formas de creación

        Parámetros:
        raza: Raza -- raza del personaje
        aliado: bool -- indica si el personaje es aliado o enemigo
        equipo: str -- equipo al que pertenece el personaje
        nombre: str -- nombre del personaje
        """
        self.raza: Raza  = raza  # publico, puede ser accedido desde fuera de la clase
        self._aliado: bool = aliado
        self._equipo: str = equipo
        self._dinero: int = 0
        self._nombre: str = nombre
        self.__id_base_datos: int = random.randint(0, 99999) # privado para gestionarlo de manera segura solo desde esta clase

        # Relaciones con otras clases
        self._mascota: 'Mascota' = None
        self.set_mascota(mascota) # si tenemos el método set_mascota, podemos usarlo en el constructor
        self._arma: Arma = None # sólo se puede tener un arma si se la fabrica para él mismo (composición)

        self._amigos: list['Personaje'] = []  # lista de amigos (asociación)
        self._inventario: list['Objeto'] = []  # lista de objetos que porta consigo el personaje (agregación), no se puede tener objetos al principio

        Personaje.numero_personajes += 1

        self.__guardar_datos() # llamada a un método privado (no se puede acceder desde fuera de la clase)

        self._vida = 100 # vida del personaje

        self._x = 0  # posición x en el mapa (atributo que necesitamos para método de interfaz)
        self._y = 0  # posición y en el mapa (atributo que necesitamos para método de interfaz)

    # Método mágico para representar el objeto como string
    def __str__(self) -> str:
        """
        Representación del personaje como cadena de texto

        Returns:
        str -- cadena de texto con la representación del personaje
        """
        return f"Personaje {self._nombre} de raza {self.raza.name} ({self._equipo})"

    # Método sobrecargado
    def atacar(self, energia: float = None, hechizo: str = None, fuerza: float = None):
        """
        Ataca al enemigo con energía, o hechizo o fuerza (sobrecarga). Si no se especifica nada, no se puede atacar

        Parámetros:
        energia: float -- cantidad de energía a utilizar
        hechizo: str -- hechizo a utilizar
        fuerza: float -- fuerza a utilizar
        """

        assert (energia and not hechizo and not fuerza) or (hechizo and not energia and not fuerza) or (fuerza and not energia and not hechizo), "Sólo se puede atacar con un tipo de ataque"

        if energia:
            print(f"Atacando con {energia} julios de energía")
        elif hechizo:
            print(f"Atacando con el hechizo {hechizo}")
        elif fuerza:
            print(f"Atacando con {fuerza} newton de fuerza")
        else:
            print("No puedo atacar!")

    
    # Métodos get y set necesarios hasta ahora

    def get_nombre(self) -> str:
        """
        Devuelve el nombre del personaje

        Returns:
        str -- nombre del personaje
        """
        return self._nombre

    def get_mascota(self) -> 'Mascota':
        """
        Devuelve la mascota del personaje

        Returns:
        Mascota -- mascota del personaje
        """
        return self._mascota

    def get_arma(self) -> 'Arma':
        return self._arma

    def get_amigos(self) -> list['Personaje']:
        return self._amigos

    def get_inventario(self) -> list['Objeto']:
        return self._inventario

    def get_raza(self) -> Raza:
        """
        Devuelve la raza del personaje

        Returns:
        Raza -- raza del personaje
        """
        return self.raza

    def _get_dinero(self) -> int: # sólo se puede acceder al dinero desde dentro de la clase/subclases
        """
        Devuelve el dinero del personaje

        Returns:
        int -- dinero del personaje
        """
        return self._dinero

    def _set_dinero(self, dinero: int): # sólo se puede modificar el dinero desde dentro de la clase/subclases
        """
        Establece el dinero del personaje

        Parámetros:
        dinero: int -- dinero del personaje
        """
        self._dinero = dinero

    def get_vida(self):
        """
        Devuelve la vida del personaje

        Returns:
        int -- vida del personaje
        """
        return self._vida

    def __get_id_base_datos(self) -> int: # sólo se puede acceder al id de la base de datos desde dentro de la clase
        """
        Devuelve el id de la base de datos del personaje
        """
        return self.__id_base_datos

    def set_mascota(self, mascota: 'Mascota'):
        """
        Añade una mascota al personaje (RELACIÓN DE AGREGACIÓN)
        """
        if mascota:
            self._mascota = mascota
            mascota.add_dueño(self) # añadimos al personaje como dueño de la mascota (BIDIRECCIONALIDAD)
            print(f"¡Bienvenido, {self._mascota.get_nombre()}!")

    # Otros métodos de instancia
    def __guardar_datos(self):
        """
        Guarda los datos del personaje en la base de datos
        """ 
        # print(f"Guardando datos con id = {self.__get_id_base_datos()}")
        pass

    def añadir_moneda(self): # solo pueden añadirme monedas de uno en uno
        """
        Añade una moneda al personaje (sólo se puede añadir una moneda a la vez)
        """
        self._set_dinero(self._dinero+1)    # sólo YO me añado realmente monedas
        

    def tiene_dinero(self) -> bool: # solo pueden saber externamente si tengo dinero o no (pero no la cantidad)
        """
        Comprueba si el personaje tiene dinero

        Returns:
        bool -- True si tiene dinero, False en caso contrario
        """
        return self._get_dinero() > 0

    def dar_moneda(self, otro_personaje: 'Personaje') -> bool:              # si permito que un personaje pueda dar moneda a otro
        """
        El personaje se quita una moneda para dársela a otro personaje. Si no tiene monedas, no se puede dar.

        Parámetros:
        otro_personaje: Personaje -- personaje al que se le da la moneda

        Returns:
        bool -- True si se ha podido dar la moneda, False en caso contrario
        """
        if self.tiene_dinero():
            self._quitar_moneda()            # sólo YO me quito realmente monedas
            otro_personaje.añadir_moneda()    # sólo el otro se añade realmente monedas
            return True
        return False

    def _quitar_moneda(self) -> bool:               # no quiero que ninguna clase externa pueda directamente quitar dinero
        """
        Quita una moneda al personaje. Si no tiene monedas, no se puede quitar.

        Returns:
        bool -- True si se ha podido quitar la moneda, False en caso contrario
        """
        if self.tiene_dinero():
            self._set_dinero(self._get_dinero()-1)
            return True
        return False
        
    def realizar_mision(self, mision: Mision):
        """
        Simula la realización de una misión (RELACIÓN DE USO). 

        Parámetros:
        mision: Mision -- misión a realizar
        """
        print(f"Realizando misión: {str(mision)}")

    def usar_objeto(self, objeto: Objeto):
        """
        Usa un objeto no incorporado al inventario.
        Parámetros:
        objeto: Objeto -- objeto a usar
        """
        objeto.usar_objeto()

    def añadir_amigo(self, amigo: 'Personaje') -> bool:
        """
        Añade un amigo al personaje (RELACIÓN DE ASOCIACIÓN)

        Parámetros:
        amigo: Personaje -- amigo a añadir

        Returns:
        bool -- True si se ha añadido el amigo, False en caso
        """
        if amigo not in self.get_amigos():
            self.get_amigos().append(amigo)
            amigo.añadir_amigo(self)  # bidireccionalidad
            return True
        return False

    def recoger_objeto(self, objeto: Objeto):
        """
        Añade un objeto al inventario del personaje (RELACIÓN DE AGREGACIÓN)

        Parámetros:
        objeto: Objeto -- objeto a añadir al inventario
        """
        print(f"Recogiendo objeto: {str(objeto)}")
        self.get_inventario().append(objeto)

    def fabricar_arma(self, nombre: str, tipo: TipoArma):
        """
        Crea un arma para el personaje. Sólo se puede tener un arma.
        Se indica el nombre y tipo de arma a crear. El daño se genera aleatoriamente entre 0 y 100.

        Parámetros:
        nombre: str -- nombre del arma
        tipo: TipoArma -- tipo del arma
        """
        print(f"Fabricando arma: {nombre}")

        if tipo == TipoArma.CORTA_DISTANCIA:
            self._arma = ArmaCorta(nombre=nombre, dueño=self, numero_estocadas=3)
        elif tipo == TipoArma.LARGA_DISTANCIA:
            self._arma = ArmaLarga(nombre=nombre, dueño=self)
        elif tipo == TipoArma.FUEGO:
            self._arma = ArmaFuego(nombre=nombre, dueño=self, balas=random.randint(1, 10))
        else:
            raise ArmaError("PERSONAJE: Tipo de arma no válido")
            return False # Se ejecutaría?

        print(f"Arma creada: {self.get_arma()}")
        return True

    def alimentar_mascota(self):
        """
        Alimenta a la mascota del personaje si no tiene energía

        Returns:
        bool -- True si ha alimentado a la mascota, False en caso contrario
        """
        if self.get_mascota() and not self.get_mascota().tiene_energia(): # no necesito saber su energia, sólo si tiene  (delego esa comprobación)
            self.get_mascota().alimentar() # no necesito saber cómo lo hace, sólo que lo hace (delego esa funcionalidad)

    # Eliminamos el método "disparar" y creamos nuevos métodos para interactuar con las armas

    def usar_arma(self, objetivo: 'Personaje') -> bool:
        """
        Usa el arma del personaje.

        Returns:
        bool -- True si ha podido usarla, False en caso contrario
        """
        if self.get_arma():
            try:
                return self.get_arma().usar(objetivo=objetivo)  # delegación
            except ArmaVaciaError as error_arma_vacia:  # Importante el orden, primero subclases
                print(f"PERSONAJE: {error_arma_vacia}")
                raise error_arma_vacia
            except ArmaError as error:
                print(f"{self.get_nombre()} no puede usar el arma, aunque tenga balas")
                raise error  # si quiero seguir lanzando error
        else:
            raise ArmaError("No tengo arma!")

    def mejorar_arma(self):
        """
        Mejora el arma del personaje
        """
        if self._arma:
            self.get_arma().mejorar()  # delegación + polimorfismo


    def recibir_daño(self, daño: int):
        """
        Recibe daño en la vida

        Parámetros:
        daño: int -- daño a recibir
        """
        if self.get_vida() == 0:
            print(f"{self._nombre} ya está muerto")

        else:
            self._vida -= daño
            if self.get_vida() <= 0:
                self._vida = 0
                print(f"{self.get_nombre()} ha recibido {daño} puntos de daño y ha muerto")
            else:
                print(f"{self.get_nombre()} ha recibido {daño} puntos de daño. Vida restante: {self.get_vida()}")

    ######## Métodos de la interfaz IDibujable ########### [POR LO TANTO, TODAS LAS SUBCLASES TAMBIÉN]
    def dibujar(self):
        """
        Dibuja el personaje en el mapa
        """
        print(f"Dibujando personaje {self.get_nombre()} en la posición ({self._x}, {self._y})")

    def obtener_posicion(self) -> tuple[int, int]:
        """
        Devuelve la posición del personaje en el mapa

        Returns:
        tuple[int, int] -- posición x, y
        """
        return self._x, self._y

    def mover(self, nueva_posicion: tuple[int, int]):
        """
        Mueve el personaje a una nueva posición en el mapa

        Parámetros:
        nueva_posicion: tuple[int, int] -- nueva posición del personaje
        """
        self._x, self._y = nueva_posicion
        print(f"{self._nombre} se ha movido a la posición {nueva_posicion}")

    def interactuar(self, otro: 'IDibujable'):
        """
        Interacción entre este personaje y otro elemento dibujable en el mapa

        Parámetros:
        otro: Dibujable -- elemento con el que interactuar
        """

        from elementos.extra.mascota import Mascota

        # Un orco siempre atacará a cualquier otro personaje
        if type(self) == 'Orco' and isinstance(otro, Personaje):
            self.usar_arma(objetivo=otro)
        # si me encuentro con un objeto, lo recojo
        elif type(otro) == Objeto:
            self.recoger_objeto(objeto=otro)
        # si me encuentro con una mascota, la adopto
        elif type(otro) == Mascota:
            self.set_mascota(mascota=otro)
        # en cualquier otro caso, hablo
        else:
            print(f"{self.get_nombre()} habla con {otro}")