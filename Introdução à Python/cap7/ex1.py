string1 = "AABBEFAATT"
string2 = "BE"

p = 0

while (p>-1):
    p=string1.find(string2, p)
    if p >= 0:
        print("Posição:", p)
        p+=1

