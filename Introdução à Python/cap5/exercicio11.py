deposito_inicial = float(input("Digite o depósito inicial: "))
taxa_de_juros = int(input("Digite a taxa de juros da poupança: "))

meses = 24

dinheiro_final =  int(deposito_inicial * (1 + (taxa_de_juros/100) )**meses)

print("O total de ganhos será de:", dinheiro_final,"Você terá ganho com juros:", dinheiro_final - deposito_inicial)

