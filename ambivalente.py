# Ambivalence


def newBoard(n):  # créer un nouveau plateau vide ( symbolisé par des . )
    board = []
    for i in range(n):
        ligne = [0] * n
        board.append(ligne)
    return board


# créé l'affichage du plateau et traduis les nombres de la liste par le bon symbole
def displayBoard(board, n):

    for i in range(n):

        print(f" {i+1} |", end=" ")  # {i +1} car commence à 0 de base

        for j in range(n):
            valeur = board[i][j]
            # Convertion nombre -> symbole
            if valeur == 0:
                symbole = "."
            elif valeur == 1:
                symbole = "x"
            elif valeur == 2:
                symbole = "o"
            elif valeur == 3:
                symbole = "N"

            print(symbole, end=" ")

        print()

    # Ligne en bas
    print("   " + "‾" * (n*2+1))

    # Numéros colonnes
    print("    ", end="")
    for col in range(1, n+1):
        print(col, end=" ")
    print()


def play(board, n, player):

    jeu = True

    while jeu:

        ligne = int(input("Choississez la ligne : "))
        colone = int(input("Choisissez la colone : "))

        if 1 <= ligne <= n and 1 <= colone <= n:

            L = ligne - 1  # pour que quand user entre 1, le pion est placé en 1 et non en 2
            C = colone - 1

            if board[L][C] == 0:
                jeu = False
                board[L][C] = player
            else:
                print("Case déjà occupée")
        else:
            print("Coordonées invalides")
    return (ligne, colone)
