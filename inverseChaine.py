# inverser une chaine de caractere
chaine = input("Etrer le mot ou la phrase: ")
count = ""
for i in range(0, len(chaine)):
    count += chaine[len(chaine) - i - 1]

print(count)
