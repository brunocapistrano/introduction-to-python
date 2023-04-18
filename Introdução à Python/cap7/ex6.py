# lê as strings
string1 = "AATTCGAA"
string2 = "TG"
string3 = "AC"

# realiza a substituição dos caracteres da segunda string pelos da terceira string na primeira string
nova_string = ''
for char in string1:
    if char in string2:
        nova_string += string3
    else:
        nova_string += char

# imprime a nova string
print(f"A nova string é: {nova_string}")