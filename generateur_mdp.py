import random

print("Je suis votre générateur de mot de passe.")

code = input("Entrer les mots(prenom, nom ou adresse) ou nombre ou symbol dont tu veux générer un mot de passe (tout collé):")
nombre = input("Entrer le nombre de mots de passe que tu veux générer :")
nombre = int(nombre)
longueur = input("Entrer la longueur des mots de passe :")
longueur = int(longueur)

for mdp in range(nombre):
    password = ''
    for caractere in range(longueur):
        password += random.choice(code)
    print(password)