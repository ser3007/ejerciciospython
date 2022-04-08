a = list(range(1, 21))
print(a)
while True:
    n = int(input("digite el numero :"))
    if n >= 0:
        print(a.index(n))
    elif n < 0:
        print("el numero es invalido digite un numero positivo")
