import random

# Initialisation des variables
bingo_boules = ["B" + str(i) for i in range(1, 16)]
bingo_boules += ["I" + str(i) for i in range(16, 31)]
bingo_boules += ["N" + str(i) for i in range(31, 46)]
bingo_boules += ["G" + str(i) for i in range(46, 61)]
bingo_boules += ["O" + str(i) for i in range(61, 76)]

boules_tirees = []

# Fonction pour afficher la grille
def afficher_grille():
    print("Boules non tirées")
    print("+----+----+----+----+----+")
    for i in range(5):
        print("|", end=" ")
        for j in range(15):
            index = i*15+j
            if index < len(bingo_boules):
                boule = bingo_boules[index]
                if boule in boules_tirees:
                    print("\033[90m" + boule + "\033[0m", end=" | ")
                else:
                    print(boule, end=" | ")
            else:
                print(" ", end=" | ")
        print()
        print("+----+----+----+----+----+")



# Boucle principale pour le jeu
while True:
    # Affichage de la grille
    print()
    afficher_grille()

    # Demande de l'utilisateur pour tirer la boule suivante
    entree = input("Appuyez sur ENTER pour tirer une boule ou Q pour quitter le jeu : ")
    if entree.lower() == "q":
        break

    # Tirage aléatoire d'une boule
    boule_tiree = random.choice(bingo_boules)
    boules_tirees.append(boule_tiree)
    bingo_boules.remove(boule_tiree)

    # Affichage de la boule tirée
    print("La boule tirée est : \033[1m" + boule_tiree + "\033[0m")

# Affichage final de la grille
print()
afficher_grille()



