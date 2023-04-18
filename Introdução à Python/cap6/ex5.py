último = 10
fila = list(range(1,último+1))
while True:
    listaString = []
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operação (F, A ou S):")
    listaString.append(list(operação))
    print(len(listaString[0]))
    i = 0
    while i < len(listaString[0]):
        if listaString[0][i] == "A":
            print(listaString[0][i])
            if(len(fila))>0:
                i += 1
                atendido = fila.pop(0)
                print("Cliente %d atendido" % atendido)
            else:
                print("Fila vazia! Ninguém para atender.")
        elif listaString[0][i] == "F":
            print(listaString[0][i])
            i += 1
            último+=1 # Incrementa o ticket do novo cliente
            fila.append(último)
        elif listaString[0][i] == "S":
            print(listaString[0][i])
            i = len(listaString[0]) + 1
            print("break")

            break