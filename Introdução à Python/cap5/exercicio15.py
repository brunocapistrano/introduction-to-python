arr = [1,2,3,5,9]

saida = 0

compras_do_usuario = []
quantidade_de_compras_do_usuario = []

while True:
    codigo_do_produto = int(input("Digite o código do produto: "))
    if codigo_do_produto in arr:
        print("Código válido")
        quantidade = int(input("Digite a quantidade que está comprando: ")) 
    else:
        print("Código inválido")
        break