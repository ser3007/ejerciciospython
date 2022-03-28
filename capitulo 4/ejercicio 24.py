numero1=int(input("digite el numero1: "))
numero2=int(input("digite el numero2: "))
numero3=int(input("digite el numero3: "))

if numero1<numero2 and numero2<numero3:
    print(f"el numero menor es: {numero1}")
elif numero2<numero1 and numero3<numero2:
    print(f"el numero menor es: {numero1}")

elif numero2<numero1 and numero1<numero3:
    print(f"el numero menor es: {2}")
elif numero2<numero3 and numero3<numero1:
    print(f"el numero menor es: {numero2}")
elif numero3<numero2 and numero3<numero1:
    print(f"el numero menor es: {numero3}")
elif numero3<numero1 and numero1<numero2:
    print(f"el numero menor es: {numero3}")
elif numero1==numero2 and numero3<numero2:
    print(f"el numero menor es: {numero3}")
elif numero1<numero2 and numero2==numero3:
    print(f"el numero menor es: {numero1}")
elif numero1<numero2 and numero2==numero3:
    print(f"hay dos numeros menores iguales: {numero2},{numero3}")
elif numero1==numero2 and numero2<numero3:
    print(f"hay dos numeros menores iguales: {numero1},{numero2}")
elif numero1==numero2==numero3:
    print(f"todos los numeros son iguales")
    