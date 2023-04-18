#Escreva um programa para aprovar o empréstimo bancário para 
#compra de uma casa. O programa deve perguntar o valor da casa a comprar, o 
#salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser 
#superior a 30% do salário. Calcule o valor da prestação como sendo o valor da 
#casa a comprar dividido pelo número de meses a pagar.

valor_da_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos_a_pagar = int(input("Por quantos anos deseja pagar? "))

meses_pagando = anos_a_pagar * 12
prestacao_mensal = int(valor_da_casa / meses_pagando)

porcentagem_salario = salario * 0.3

if porcentagem_salario > prestacao_mensal:
    print("Empréstimo concedido. O valor da prestação mensal será de R$ {:.2f}.".format(prestacao_mensal))
else:
    print("Infelizmente não podemos conceder o empréstimo.")