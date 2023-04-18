from time import sleep
x=10 
while x>=0: 
    sleep(1)
    print(x)
    if x == 0:
        print("Fogo!")
    x = x - 1 