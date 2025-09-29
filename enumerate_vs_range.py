nomes = ['Pedro', 'Ana', 'Maria', 'João']

print('Usando len:')
for i in range(len(nomes)):
    print(i+1, nomes[i])

print('\nUsando enumerate:')
for i,nome in enumerate(nomes, start=1):
    print(i, nome)

print('\nExemplo com tuplas:')
dados = [(1, "maçã",), (2, "banana"), (3, "laranja")]

for id, fruta in dados:
    print(id, fruta)