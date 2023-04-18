# Exercício 3.11

preco = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))

percentual = desconto / 100
descontoDoProduto = preco * percentual
valorDoProduto = preco - descontoDoProduto

print("O desconto foi de R$ %s reais, e o valor total ficou R$ %d reais." % (descontoDoProduto, valorDoProduto))