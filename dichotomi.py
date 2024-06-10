def recherche_dichotomique(aRechercher, tableau):
    debut = 0
    fin = len(tableau)
    milieu = 0
    
    while debut <= fin:
        milieu = (debut + fin) // 2
        
        if tableau[milieu] < aRechercher:
            debut = milieu + 1
        elif tableau[milieu] > aRechercher:
            fin = milieu - 1
        else:
            return milieu
    return -1
        

tableau = [ 0, 3, 4, 5, 7, 9, 10, 12, 13, 15, 16, 18, 19]
aRechercher = input("Entrer le nombre que vous voulez rechercher : ")
aRechercher = int(aRechercher)
resultat = recherche_dichotomique(aRechercher, tableau)

if (resultat != -1):
    print(str(aRechercher) + " se trouve a la position " + str(resultat))
else:
    print(str(aRechercher) + " ne se trouve pas dans le tableau")
