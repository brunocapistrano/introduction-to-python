string1 = "AATTGGAA"
string2 = "TG"

string3 = ""

for caracter in string1:
    teste = list(string2)
    if caracter != teste[1][0] and caracter != teste[0][0]:
        print(caracter, teste)
        string3 += caracter


print(string3)