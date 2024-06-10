# -*- coding: utf-8 -*-
# rechercher si une chaine contient e
chaine = list(input("Entrer le mot ou la phrase: "))
count = 0
recherche = list()
for i in chaine:
    if i == "e" or i == "E":
        count += 1
        recherche.append(count)

if len(recherche) == 0:
    print("la chaine ne contient pas le caractère \"e\" ")
else:
    print("La chaine contient le caractère \"e\" et le nombre de \"e\" est " + str(len(recherche)))
