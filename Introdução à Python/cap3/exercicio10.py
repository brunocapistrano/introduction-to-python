# Exercício 3.10

salario = float(input("Digite seu salário: "))
porcentagem = float(input("Digite a porcentagem de aumento sem o simbolo %: "))

porcentagemC = porcentagem / 100

salarioAjustado = salario + (salario * porcentagemC)

print("O salário ajustado ficou %s" % salarioAjustado)
