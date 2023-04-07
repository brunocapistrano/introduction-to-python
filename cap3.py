# #Exercício 3.6 Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.

# materia1 = 6
# materia2 = 7
# materia3 = 8
# media = (materia1 + materia2 + materia3)/3
# aprovado = media >= 7

# print(aprovado)

# print("")

# #Exercício 3.7 Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))

# teste = num1 + num2
# print(teste)

# print("")

# #Exercício 3.8 Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

# numEmMetros = int(input("Digite uma metragem: "))
# convert = numEmMetros * 1000
# print(convert)

# print("")

# #Exercício 3.9 Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
# import datetime

# data = datetime.date.today()
# dia = int(data.day)
# print("O dia atual é: %s" % dia)
# horário = datetime.datetime.now()
# hora = int(horário.strftime("%H"))
# print("A hora atual é: %s" % hora)
# minuto = int(horário.strftime("%M"))
# print("O minuto atual é: %s" % minuto)
# segundo = int(horário.strftime("%S"))
# print("O segundo atual é: %s" % segundo)

# convertM = minuto * 60
# convertH = hora * 3600
# convertD = dia * 86400

# arr = [convertM, convertH, convertD]
# Sum =  sum(arr)
# segundos = Sum + segundo 

# print("Isso tudo em segundos é igual à %s segundos." % segundos)

# print("")

# # Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

# salario = float(input("Digite seu salário: "))
# porcentagem = float(input("Digite a porcentagem de aumento sem o simbolo %: "))

# porcentagemC = porcentagem / 100

# salarioAjustado = salario + (salario * porcentagemC)

# print("O salário ajustado ficou %s" % salarioAjustado)

# print("")

# # Exercício 3.11 Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

# preco = float(input("Digite o valor da mercadoria: "))
# desconto = float(input("Digite o percentual de desconto: "))

# percentual = desconto / 100
# descontoDoProduto = preco * percentual
# valorDoProduto = preco - descontoDoProduto

# print("O desconto foi de R$ %s reais, e o valor total ficou R$ %d reais." % (descontoDoProduto, valorDoProduto))

# print("")

# # Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

# distancia = float(input("Qual a distância a percorrer? "))
# velocidadeM = float(input("Qual a velocidade que pretende manter? "))

# tempoDeViagem = int(distancia / velocidadeM)

# print("A viagem irá durar %s horas." % tempoDeViagem)

# print("")

# # Exercício 3.13 Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é: F = (9xC)/5+32

# temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

# temperatura_fahrenheit = (temperatura_celsius * 9) / 5 + 32

# print("A temperatura de", temperatura_celsius, "graus Celsius corresponde a", temperatura_fahrenheit, "graus Fahrenheit.")

# print("")

# # Exercício 3.14 Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

# quantidade_de_km_percorrido = float(input("Digite a quantidade de quilometros percorrido: "))
# quantidade_de_dias_alugado = float(input("Digite a quantidade de dias alugado: "))

# custo_diario = 60 * quantidade_de_km_percorrido
# custo_por_km_rodado = 0.15 * quantidade_de_km_percorrido

# print("O preço do aluguel ficou ", custo_diario + custo_por_km_rodado)

# print("")

# # Exercício 3.15 Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

quantidade_de_cigarros_fumados_por_dia = float(input("Digite a quantidade de cigarros fumados por dia: "))
quantidade_de_anos_fumando = float(input("Digite a quantidade de anos que fuma: "))

total_cigarros = quantidade_de_anos_fumando * 365 * quantidade_de_cigarros_fumados_por_dia

tempo_perdido = int(total_cigarros * 10 / 1440)

print("Os dias de vida perdido são ", tempo_perdido)