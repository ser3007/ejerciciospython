NOMBRE=input("digite el nombre del estudiante: ")
NEF=float(input("digite la nota de la evalucion final: "))
NQ1=float(input("digite la nota del quiz 1: " ))
NQ2=float(input("digite la nota de quiz 2: "))
NQ3=float(input("digite la nota de quiz 3: "))
NTF=float(input("digite la nota de trabajo final: "))
NQ=(NQ1+NQ2+NQ3)/3
NFA=float(NEF*0.5)+(NQ*0.20)+(NTF*0.30)
print(f" El estudiante {NOMBRE} , tiene una nota final de asignatura de: {NFA} ")
