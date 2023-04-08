#Escreva um programa que pergunte a velocidade do carro de um 
#usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário 
#foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 
#80 km/h.

velocidade_carro = int(input("Digite a velocidade do carro: "))

if velocidade_carro > 80:
    print("Você foi multado!")
    km_acima = velocidade_carro - 80
    valor_multa = km_acima * 5
    print("O valor da multa é de", valor_multa, "reais.")