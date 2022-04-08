meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
v_i = []
for i in meses:
    valores = int(input("ingrese los valores de la produccion de cafe: "))
    v_i.append(valores)
    promedio = sum(v_i)/len(meses)
print(f"{meses}\n{v_i}\n promedio de produccion en el año: {promedio}")
