# Exercício 3.15 

quantidade_de_cigarros_fumados_por_dia = float(input("Digite a quantidade de cigarros fumados por dia: "))
quantidade_de_anos_fumando = float(input("Digite a quantidade de anos que fuma: "))

total_cigarros = quantidade_de_anos_fumando * 365 * quantidade_de_cigarros_fumados_por_dia

tempo_perdido = int(total_cigarros * 10 / 1440)

print("Os dias de vida perdido são ", tempo_perdido)