from elementos.personaje import Personaje
from elementos.raza import Raza
from elementos.extra.mascota import Mascota
from elementos.extra.mision import Mision
from elementos.extra.arma import TipoArma


if __name__ == '__main__':
    """
    Programa principal de prueba realista del juego del señor de los anillos
    """

    # Creamos un personaje hobbit
    frodo: Personaje = Personaje(nombre="Frodo", raza=Raza.HOBBIT, aliado=True, equipo="Comunidad del anillo")
    print(frodo)

    # Creamos un personaje humano
    aragorn: Personaje = Personaje(nombre="Aragorn", raza=Raza.HUMANO, aliado=True, equipo="Comunidad del anillo")
    print(aragorn)

    # Creamos un personaje mago
    gandalf: Personaje = Personaje(nombre="Gandalf", raza=Raza.MAGO, aliado=True, equipo="Comunidad del anillo")
    print(gandalf)

    # Creamos un personaje enano
    gimli: Personaje = Personaje(nombre="Gimli", raza=Raza.ENANO, aliado=True, equipo="Comunidad del anillo")
    print(gimli)

    # Creamos una mascota
    smeagol: Mascota = Mascota(nombre="Smeagol", raza=Raza.HOBBIT, nivel=5)
    frodo.set_mascota(smeagol)
    print(smeagol)
    frodo.alimentar_mascota()

    # Hacemos misión
    mision: Mision = Mision("Destruir el anillo único", 10, "Destruir el anillo en el monte del destino")
    mision = frodo.realizar_mision(mision)

    # Creamos un personaje orco
    orco = Personaje(nombre="Gothmog", raza=Raza.ORCO, aliado=False, equipo="Aliados de Sauron")
    print(orco)

    # Batalla
    orco.fabricar_arma(nombre="Espada", tipo=TipoArma.CORTA_DISTANCIA)
    orco.disparar()      # Si no es de tipo fuego, no se puede disparar

    gandalf.fabricar_arma(nombre="Bastón", tipo=TipoArma.LARGA_DISTANCIA)
    gandalf.disparar()   # Si no es de tipo fuego, no se puede disparar

    frodo.fabricar_arma(nombre="Magnum", tipo=TipoArma.FUEGO)
    frodo.disparar()

    # Mostramos el número de personajes creados
    print(f"Personajes creados: {Personaje.get_numero_personajes()}")





    