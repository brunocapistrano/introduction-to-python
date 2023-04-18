deposito_inicial = float(input("Digite o depósito inicial: "))
taxa_de_juros = int(input("Digite a taxa de juros da poupança: "))
aporte = int(input("Valor do aporte: "))

meses = 24
i = 0

dinheiro_final = 0

while i < 24:
    i = i + 1
    if i == 1:
        dinheiro_final = int(deposito_inicial * (1 + (taxa_de_juros/100) )**meses)
        print(dinheiro_final)    
    else:
        dinheiro_final = dinheiro_final * (1 + (taxa_de_juros/100) ) + aporte
        print(dinheiro_final)

# print(i)
# print(dinheiro_final)
# dinheiro_final =  int(deposito_inicial * (1 + (taxa_de_juros/100) )**meses)
print("O total de ganhos será de:", dinheiro_final,"Você terá ganho com juros:", dinheiro_final - deposito_inicial)