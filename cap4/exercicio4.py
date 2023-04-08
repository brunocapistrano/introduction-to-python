salario = float(input("Digite o seu salário: "))

if salario > 1250:
    print("O seu salário será:", salario+(salario * (10/100)))
if salario <= 1250:
    print("O  seu salário será:", salario+(salario * (15/100)))
