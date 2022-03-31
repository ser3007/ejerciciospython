alfabeto=('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
texto=str(input("digite la Palabra:"))
contar=0

for i in texto:
    if texto in alfabeto:
        contar+=1
    else:
        print("Todos los caracteres son alfabeticos" )
        break
if contar==len(texto): 
    print("Se ha encontrado caracter no Alfabetico")     
