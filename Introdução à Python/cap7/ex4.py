# lê a string
string = input("Digite uma string: ")

# cria um dicionário para contar as ocorrências
ocorrencias = {}

# itera sobre os caracteres da string
for char in string:
    # se o caractere já estiver no dicionário, incrementa a contagem
    if char in ocorrencias:
        ocorrencias[char] += 1
    # caso contrário, adiciona o caractere ao dicionário com contagem 1
    else:
        ocorrencias[char] = 1

# imprime as ocorrências
for char, count in ocorrencias.items():
    print(f"O caractere '{char}' aparece {count} vez(es) na string.")