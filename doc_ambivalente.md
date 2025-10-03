### Documentation du programme ambivalente.py 

- Fonction "newBoard" :
    -

On commence par créer une liste vide. Puis, pour autant de fois qu'on indiquera dans la variable n, on ajoute un 0 multiplié par le nombre n et on ajoute la liste ainsi créée à la lise board. Cela a pour effet de créer une liste de liste, permettant de changer les valeurs à l'intérieurs sans coflit dans les autres. Une fois fait, on retourne board afin de l'utiliser plus tards dans les autres fonctions.


- Fonction "displayNoard" : 
    -
Pour autant de fois que n, on répète :

    - écrire une barre | et un nombre corespondant à la valeur de i + 1 afin de commencer l'affichage à 1 et non 0
|

    - on commence ensuite une boucle for qui permet d'associer le bon symbole à chacque valeur contenue dans la liste. Elle associe les 0 aux "." , les "1" aux "x" , les 2 aux "o" et les 3 aux "N". Ensuite, on écris les symboles en séparant chacun par un espace au lieu du retour à la ligne. Une fois la boucle finie, on fait un print() vide pour faire le retour à la ligne et pouvoir écrire les prochaines lignes qui composent le tableau.
|

    - la fonction " print("   " + "‾" * (n*2+1)) " permet d'écrire les tirets en bas de la grilles afin de la fermer.
|

    - la fin permet d'écrire les numéros de colone en dessous de la grille.


- Fonction "possibleSquare"
    -

Elle permet de vérifier si une cas est disponible pour le joueur. Si la valeur numérique de la case est égale à à, alors le joueur peux l'utiliser. Sinon, c'est qu'elle est ocupée.

- Fonction selectSquare
    -
sert au joueur à sélectionner la case qu'il souhaite occuper. Elle fonctionne en deux étape, le numéro de ligne, puis de colone. Ces numéros sont stockés dans des variables auxquels ont retire 1 pour que le programme retrouve son fonctionnement "normal". Si la case est validée par la fonction possibleSquare, alors on return True, sinon on demande au joueur de sélectioner une autre case.

- Fonction "updateBoard"
    -
permet de mettre à jour le plateau pour le joueur suivant. Elle commence par placer le pion du joueur actuel à la position sélectionnée. Ensuite, elle détermine qui est l'adversaire (si joueur = 1 alors adversaire = 2, sinon adversaire = 1). La fonction vérifie dans les 8 directions possibles autour du pion placé pour détecter les intrusions et encerclements. Pour les intrusions, elle cherche si deux pions adverses sont alignés avec le pion placé. Pour les encerclements, elle vérifie si un pion adverse est entre le pion placé et un autre pion allié. Les pions neutralisés deviennent des "N" (valeur 3).

- Fonction "again"
    -
Vérifie s'il reste des cases vides sur le plateau pour continuer la partie. Elle parcourt toutes les cases du plateau et retourne True s'il reste au moins une case avec la valeur 0 (vide), sinon elle retourne False pour indiquer que la partie est terminée.

- Fonction "winner"
    -
Permet de savoir quel joueur a gagné. Elle parcourt tout le plateau et compte le nombre de pions pour le joueur 1, le joueur 2, les pions neutres et les cases vides. Elle affiche ensuite les résultats finaux et retourne 1 si le joueur 1 gagne, 2 si le joueur 2 gagne, ou 0 en cas d'égalité.

- Fonction "ambivalente"
    -
C'est la fonction qui fait fonctionner le jeu. Elle commence par créer un nouveau plateau. Elle gère ensuite la boucle de jeu principale où les joueurs alternent leurs tours. Elle lance chacun des sous programmes.

- Fonction "main"
    -
Permet le démarage de chacun des sous programes du jeu.
