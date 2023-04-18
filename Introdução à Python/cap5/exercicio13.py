divida = int(input("Digite o valor da sua dívida: "))
juros = int(input("Digite a porcentagem da dívida: "))/100

pagamento_mensal = int(input("Digite o valor que será pago mensalmente: "))

meses = 0
total_pago = 0
total_juros = 0

while divida > 0:
    meses = meses + 1
    juros_mes = divida * juros
    total_juros = total_juros + juros_mes
    divida = divida + juros_mes
    divida = divida - pagamento_mensal
    total_pago = total_pago + pagamento_mensal

print(total_juros)
print(total_pago)
print(meses)