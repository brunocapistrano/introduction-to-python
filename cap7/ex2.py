string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

# Inicializa a string resultante como uma string vazia
resultado = ""

# Percorre cada caractere da primeira string
for caractere in string1:
    # Verifica se o caractere está presente na segunda string e ainda não foi adicionado ao resultado
    if caractere in string2 and caractere not in resultado:
        resultado += caractere

# Imprime o resultado
print("Resultado:", resultado)