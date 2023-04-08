string1 = "CTA"
string2 = "ABC"

string3 = ""

for caracter in string2:
    if caracter not in string1:
        string3 += caracter

for caracter in string1:
    if caracter not in string2:
        string3 += caracter
    

print(string3)