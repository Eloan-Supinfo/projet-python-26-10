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


def updateBoard(board, n, player, i, j):

    board[i][j] = player

    adversaire = 2 if player == 1 else 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    intrusions_neutralisee = []
    encerclement_neutralisee = []

    for di, dj in directions:
        i1, j1 = i + di, j + dj
        i2, j2 = i + 2*di, j + 2*dj

        if 0 <= i1 < n and 0 <= j1 < n and 0 <= i2 < n and 0 <= j2 < n:

            # check intrusions
            if board[i1][j1] == adversaire and board[i2][j2] == adversaire:
                intrusions_neutralisee.append((i1, j1))
                intrusions_neutralisee.append((i2, j2))

            # check encerclement
            if board[i1][j1] == adversaire and board[i2][j2] == player:
                encerclement_neutralisee.append((i1, j1))

    # Appliquer intrusion
    for ni, nj in intrusions_neutralisee:
        board[ni][nj] = 3

    # Appliquer encerclement
    for ni, nj in encerclement_neutralisee:
        board[ni][nj] = 3

    if len(intrusions_neutralisee) > 0:
        print("Intrusion ! Des pions adverses sont devenus neutres.")
    if len(encerclement_neutralisee) > 0:
        print("Encerclement ! Des pions adverses sont devenus neutres.")


def again(board, n):

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return True
    return False


def winner(board, n):
    count_player1 = 0
    count_player2 = 0
    count_neutral = 0
    count_empty = 0

    for i in range(n):
        for j in range(n):
            valeur = board[i][j]

            if valeur == 1:
                count_player1 += 1
            elif valeur == 2:
                count_player2 += 1
            elif valeur == 3:
                count_neutral += 1
            else:
                count_empty += 1

    print(f"\nRésultats finaux :")
    print(f"Joueur 1 (blanc) : {count_player1} pions")
    print(f"Joueur 2 (noir)  : {count_player2} pions")
    print(f"Pions neutres    : {count_neutral} pions")
    print(f"Cases vides      : {count_empty} cases")

    if count_player1 > count_player2:
        return 1
    elif count_player2 > count_player1:
        return 2
    else:
        return 0
