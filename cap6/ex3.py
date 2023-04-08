listaUm = [1,2,2,3]
listaDois = [4,5,5,6]

listaTres = []

for elemento in listaUm:
    if elemento not in listaTres:
        listaTres.append(elemento)

for elemento in listaDois:
    if elemento not in listaTres:
        listaTres.append(elemento)

print(listaTres)