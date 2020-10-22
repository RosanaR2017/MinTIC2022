import random


def main():
    lista_animales = [
        "Abadejo", "Abalone", "Abejarón", "Abejaruco", "Abeja", "Abejorro", "Ácaro", "Acedía", "Acentor", "Agamido", "Águila", "Alacrán", "Albatros", "Alce", "Almeja", "Alondra", "Ánade Real", "Anchoa", "Anémona de mar", "Anfioxo", "Angelote", "Anguila", "Antílope","Araña", "Arenque", "Armadillo", "Armiño", "Asno", "Atún", "Avefría", "Avestruz", "Avetoro", "Avispa", "Babirusa", "Babosa", "Babuino", "Bacalao", "Ballena", "Banteng", "Barasinga", "Barracuda", "Becada","Beira", "Beluga", "Bengalí", "Bermejuela", "Berrendo", "Besugo", "Bisbita", "Bisonte", "Blanquillo", "Boa", "Bogavante", "Bongo", "Bonito", "Bonobo", "Boto", "Buey", "Búfalo", "Búho", "Buitre","Burro", "Caballo", "Caballito de mar", "Cacatúa", "Cachalote", "Calamón", "Camaleón", "Camello", "Canguro", "Canario", "Cangrejo","Caracol", "Castor", "Cebra", "Centollo", "Cerdo", "Chacal","Chimpancé", "Chinchilla", "Ciempiés", "Ciervo", "Cigala", "Cisne", "Cobaya", "Cochinilla", "Cocodrilo", "Coendú", "Coipú", "Colibrí", "Comadreja", "Conejo", "Coral", "Coridora", "Cormorán", "Cóndor","Cotorra", "Coyote", "Damán", "Delfín", "Diablo de Tasmania", "Dik-dik", "Dingo", "Dragón de Komodo", "Dromedario", "Elefante", "Emú", "Equidna", "Erizo", "Escarabajo", "Escorpión", "Escuerzo","Espátula común", "Estrella de mar", "Farra", "Faisán", "Flamingo", "Flamenco", "Foca", "Gacela", "Galápago", "Gallina", "Gallipato", "Gallo", "Gamba", "Ganso", "Garcilla", "Garrapata", "Garza", "Gato","Gavilán", "Glotón", "Golondrina", "Gorila", "Gorgojo", "Gorrión", "Grillo", "Grulla", "Guepardo", "Halcón", "Hamster", "Hiena", "Hipocampo", "Hipopótamo", "Holoturia", "Hormiga", "Hurón", "Hupón","Ibice", "Icotea", "Iguana", "Insecto palo", "Intendio", "Impala", "Jabalí", "Jabirú", "Jerbo", "Jirafa", "Jaguar", "Kaguang", "Kiwi","Krill", "Koala", "Labro", "Lagarto", "Langosta", "Langostino","Lechuza", "Lémur", "León", "León marino", "Leopardo", "Libélula","Liebre", "Lince", "Llama", "Lobo", "Lobo marino", "Lombriz", "Loro","Luciérnaga", "Mamut", "Mandril", "Mantis religiosa", "Mapache","Marabú", "Marabunta", "Mariposa", "Marmota", "Medusa", "Mejillón", "Milpiés", "Mofeta", "Mono", "Mosca", "Mosquito", "Morsa","Murciélago", "Narval", "Navaja", "Nécora", "Nutria", "Ñandú", "Ñu","Ocelote", "Okapi", "Oso", "Oso de agua", "Oso hormiguero","Oso panda", "Oso pardo", "Ornitorrinco", "Oveja", "Pájaro", "Paloma","Pantera", "Papagayo", "Pelicano", "Perca", "Perdiz", "Perezoso","Perico", "Peripato", "Periquito", "Perro", "Petirrojo", "Pez","Pingüino", "Pinzón", "Piojo", "Piquituerto", "Polilla", "Puercoespín","Pulga", "Pulpo", "Puma", "Quebrantahuesos", "Quetzal", "Quitón", "Rana", "Rata", "Ratón", "Raya", "Rebeco", "Rémora", "Reno","Rinoceronte", "Rubia Gallega", "Ruiseñor", "Salamandra", "Salmón","Saltamontes", "Sanguijuela", "Sapo", "Sepia", "Serpiente", "Tábano","Tejón", "Tenia", "Termita", "Tiburón", "Tigre", "Tijereta", "Topo","Toro", "Tortuga", "Tritón", "Trucha", "Tucán", "Urogallo", "Urraca","Vaca", "Varano", "Venado", "Vicuña", "Wapití", "Walabi", "Walaró","Weta", "Wombat", "Xenopus", "Xenopus laevis", "Xoloescuintle", "Yak","Yacare", "Yegua", "Zarigüeya", "Zorro", "Zebra"
    ]
    cantidad_intentos = 5
    animal_secreto = (aleatorio(lista_animales))
    #print(animal_secreto)
    adivinado =[]
    j = 0
    for letra in animal_secreto:
      adivinado.append("*")
      j += 1
    bandera = True

    contador=0
    intento_anterior = ""
    while bandera:
      intento = evaluar_letra(entrada(), animal_secreto, adivinado)
      print (intento)
      #print (intento,animal_secreto)
      if (animal_secreto.lower() == intento.lower()):
        #print (intento,animal_secreto)
        bandera = False
        print("Felicidades ha adivinado")
      if intento.lower() == animal_secreto.lower():
        bandera = False
        print("Felicidades ha adivinado")
      elif intento_anterior.lower()==intento.lower() and contador<cantidad_intentos:
        print("anterior:", intento_anterior, "actual: ", intento)
        print("Le quedan", cantidad_intentos - contador , "intentos")
        contador +=1
      elif contador >= cantidad_intentos:
        print("Ha superado",cantidad_intentos,"intentos errados, ha perdido")
        print("La palabra era: ",animal_secreto)
        bandera = False
      

      intento_anterior = intento




def entrada():
    return input("Ingrese letra: ")


def aleatorio(lista):
    return random.choice(lista)


def evaluar_letra(letra, palabra, adivinado):
    i = 0
    if(letra.lower() == palabra.lower()):
      return letra

    for l in palabra:
      #print(letra)
      if letra == palabra[i].lower() and adivinado[i].lower() == "*":
        adivinado[i] = letra

      #print(adivinado)
      i += 1
    salida =""
    for l in adivinado:
      salida += l
    return salida


main()
