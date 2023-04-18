#Reescreva a função da listagem 8.5 de forma a utilizar os métodos de pesquisa em lista, vistos no capítulo 7

def pesquise(lista, valor):   
    for x,e in enumerate(lista):
        if e == valor:
            return x 
    return None 

L=[10, 20, 25, 30]

print(pesquise(L, 25))
print(pesquise(L, 27))