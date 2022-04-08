from multiprocessing.connection import Listener
from turtle import listen

listan = int(input("digite tamaño de la lista de desea capturar"))
numeritos = []
i = 0
while i <= listan:
    numero = int(input("digite el numero : "))
    numeritos.append(numero)
    i += 1
    for index, value in enumerate(numeritos):
        if (value < 1):
            numeritos[index] = 0
            print(value)
