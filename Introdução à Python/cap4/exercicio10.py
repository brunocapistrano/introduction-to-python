#Escreva um programa que calcule o preço a pagar pelo fornecimento 
#de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a 
#pagar de acordo com a tabela a seguir.

quantidade_kWh_consumida = int(input("Digite a quantidade de kWh consumida: "))
tipo_intalacao = input("Qual o tipo de instalação? Digite R, I ou C.")

if tipo_intalacao == "R" and quantidade_kWh_consumida > 500:
    print(quantidade_kWh_consumida * 0.65)
elif tipo_intalacao == "R" and quantidade_kWh_consumida <= 500:
    print(quantidade_kWh_consumida * 0.5)
elif tipo_intalacao == "I" and quantidade_kWh_consumida < 5000:
    print(quantidade_kWh_consumida * 0.55)
elif tipo_intalacao == "I" and quantidade_kWh_consumida > 5000:
    print(quantidade_kWh_consumida * 0.60)
elif tipo_intalacao == "C" and quantidade_kWh_consumida < 1000:
    print(quantidade_kWh_consumida * 0.55)
elif tipo_intalacao == "C" and quantidade_kWh_consumida > 1000:
    print(quantidade_kWh_consumida * 0.60)