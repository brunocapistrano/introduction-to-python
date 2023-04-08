num = 1

arr = []

while True:
    num = int(input("Digite um número: "))
    arr.append(num)
    print(arr)
    if num == 0:
        arr.pop()
        print("A soma dos números adicionados é",sum(arr))
        print("A média dos números no array é", sum(arr) / len(arr))
        break