# Ambivalence


def newBoard(n):  # créer un nouveau plateau vide ( symbolisé par des . )
    board = []
    for i in range(n):
        ligne = [0] * n
        board.append(ligne)
    return board
