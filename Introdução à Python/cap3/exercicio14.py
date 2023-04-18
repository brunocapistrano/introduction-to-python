# Exercício 3.14

quantidade_de_km_percorrido = float(input("Digite a quantidade de quilometros percorrido: "))
quantidade_de_dias_alugado = float(input("Digite a quantidade de dias alugado: "))

custo_diario = 60 * quantidade_de_km_percorrido
custo_por_km_rodado = 0.15 * quantidade_de_km_percorrido

print("O preço do aluguel ficou ", custo_diario + custo_por_km_rodado)