# Escreva um programa que leia dois números e que pergunte qual 
# operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-), 
# multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

operacao = input("Escolha uma dessas operações:  + - / *")

if operacao == "+":
    print(num1 + num2)
elif operacao == "/":
    print(num1 / num2)
elif operacao == "-":
    print(num1 - num2)
elif operacao == "*":
    print(num1 * num2)

