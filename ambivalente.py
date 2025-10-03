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


def possibleSquare(board, n, i, j):
    if i < 0 or i >= n:
        return False

    if j < 0 or j >= n:
        return False

    if board[i][j] != 0:
        return False

    return True


def selectSquare(board, n):
    valide = False

    while not valide:
        ligne = int(input("Entrez le n° de la ligne : "))
        colonne = int(input("Entrez le n° de la colonne : "))

        i = ligne - 1  # pour tomber sur les bonnes coordonées
        j = colonne - 1

        if possibleSquare(board, n, i, j):
            valide = True
        else:
            print("Case invalide ou occupée !")

    return (i, j)
