# mettre une chaine sous format (c*h*a*i*n*e)
chaine = input("Etrer le mot ou la phrase: ")
count = ""
for i in range(0, len(chaine)):
    if i != len(chaine) - 1:
        count += chaine[i] + "*"
    else:
        count += chaine[i]

print(count)