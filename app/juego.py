from elementos.personajes.personaje import Personaje
from elementos.personajes.hobbit import Hobbit
from elementos.personajes.enano import Enano
from elementos.personajes.mago import Mago
from elementos.personajes.ent import Ent
from elementos.personajes.orco import Orco
from elementos.personajes.humano import Humano
from elementos.personajes.raza import Raza
from elementos.extra.mascota import Mascota
from elementos.extra.mision import Mision
from elementos.extra.armas.arma import TipoArma, Arma

if __name__ == '__main__':
    """
    Programa principal de prueba realista del juego del señor de los anillos
    """

    # Creamos un personaje hobbit (IMPORTANTE: Puedo seguir creando objetos de la clase Personaje, aunque no es correcto si ya tengo subclases específicas)
    frodo: Personaje = Personaje(nombre="Frodo", raza=Raza.HOBBIT, aliado=True, equipo="Comunidad del anillo")
    print(frodo)

    # Creamos una mascota
    smeagol: Mascota = Mascota(nombre="Smeagol", raza=Raza.HOBBIT, nivel=5)
    frodo.set_mascota(smeagol)
    print(smeagol)
    frodo.alimentar_mascota()

    # Creamos un personaje humano
    aragorn: Humano = Humano(nombre="Aragorn", raza=Raza.HUMANO, aliado=True, equipo="Comunidad del anillo")
    print(aragorn)

    # Ahora vamos a crear otro personaje, de tipo Hobbit
    sam: Hobbit = Hobbit(nombre="Sam", raza=Raza.HOBBIT, aliado=True, equipo="Comunidad del anillo")
    #sam.atacar(fuerza=4.5)    # Si es hobbit, no puede atacar. Esto daría error si se descomenta, pues no necesita parámetros en la subclase Hobbit.
    sam.atacar()               # Este método se ha sobreescrito en la subclase Hobbit y no necesita parámetros. [POLIMORFISMO]
    frodo.atacar(fuerza=4.5)   # Frodo es de tipo Personaje, y sí puede ejecutar el método original. Frodo debería crease de tipo Hobbit.

    # Creamos un personaje mago
    gandalf: Mago = Mago(nombre="Gandalf", raza=Raza.MAGO, aliado=True, equipo="Comunidad del anillo")
    print(gandalf)
    gandalf.atacar(hechizo="Rayo")  # Si es de tipo mago, sólo puede atacar con hechizos (parámetro obligatorio ahora!) [POLIMORFISMO]

    # Creamos un personaje ent (barbol)
    barbol: Ent = Ent(nombre="Barbol")  # No necesita más parámetros, ya que no tiene más atributos que el nombre
    barbol.atacar(fuerza=10)            # Asumimos que los Ents pueden atacar con fuerza, energía o hechizos.
    barbol.atacar(energia=10)
    barbol.atacar(hechizo="Llamas")
    barbol.añadir_moneda()              # Los Ents no pueden añadir monedas. Hemos sobreescrito el método en la subclase Ent.
    #barbol.da_moneda(gandalf)         # ERROR. Los Ents heredan el método da_moneda y no lo hemos sobreescrito.

    # Creamos un personaje enano
    gimli: Enano = Enano(nombre="Gimli", equipo="Comunidad del anillo")
    print(gimli)

    # Hacemos misión
    mision: Mision = Mision("Destruir el anillo", 10, "Destruir el anillo en el monte del destino")
    mision = frodo.realizar_mision(mision)

    # Creamos un personaje orco
    orco_jefe: Orco = Orco(jefe=gandalf, nombre="Gothmog")    # El jefe de un orco no puede ser un mago
    print(orco_jefe)
    orco: Orco = Orco(jefe=orco_jefe, nombre="Shagrat")
    print(orco)

    # Batalla
    #armaAbstracta: Arma = Arma(nombre="Espada", tipo=TipoArma.CORTA_DISTANCIA, dueño=orco) # ERROR! No se puede instanciar un objeto de una clase abstracta.

    gandalf.fabricar_arma(nombre="Bastón", tipo=TipoArma.LARGA_DISTANCIA)
    gandalf.usar_arma(objetivo=orco)   # Gandalf ataca a un orco con su bastón

    orco.fabricar_arma(nombre="Espada", tipo=TipoArma.CORTA_DISTANCIA)
    orco.usar_arma(objetivo=gandalf)   # El orco ataca a Gandalf con su espada
    orco.mejorar_arma()
    orco.usar_arma(objetivo=frodo)

    frodo.fabricar_arma(nombre="Magnum", tipo=TipoArma.FUEGO)
    frodo.usar_arma(objetivo=orco)

    # Mostramos el número de personajes creados
    print(f"Personajes creados: {Personaje.get_numero_personajes()}")
    