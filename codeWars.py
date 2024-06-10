"""
# une fonction qui permet qui reçoit un nombre, range ce nombre sous forme de liste puis renverse la liste
def digitize(n):
    liste1 = []
    for i in str(n):
        liste1.append(int(i))

    liste1.reverse()
    return liste1


liste = digitize(1765406)
print(liste)
"""
"""
# une fonction qui reçcoit une chaine de caractere et un nombre n puis elle repete la chaine de caractere n fois
def repeat_str(repeat, string):
    string = repeat * string
    return str(string)

thiao = repeat_str(4, 'assane')
print(thiao)
"""
"""
# on prend un nombre on le renverse sans pour autant affiche la 1ere case de 0
def reverse_seq(n):
    liste = []
    if n > 0:
        for i in range(n + 2):
            liste.append(int(i))
    liste.reverse()
    return liste[1:-1]
thiao = reverse_seq(30)
print(thiao)
"""
"""
# convertir une chaine d'ADN en ARN
def dna_to_rna(dna):
    arn = ""
    i = 0
    for i in dna:
        if i == "T":
            arn = arn + "U"
        else:
            arn = arn + i
    return arn
thiao = dna_to_rna("AGGUUTCC")
print(thiao)
"""
"""
# abbreviation
def abbrev_name(name):
    first = name[0]
    first = first.upper()
    last = " "
    count = 0
    for i in name:
        count += 1
        count = int(count)
        if i == " ":
            last = name[count]
            break
    last = last.upper()
    abbrev = first + "." + last
    return abbrev
thiao = abbrev_name("abdoulaye wade mané")
print(thiao)
"""
