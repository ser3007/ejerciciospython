objetivo_x=int(input("Digite el numero entero: "))
objetivo_y=input(input("Digite el numero entero: "))
caballo_x=0
caballo_y=0

flow="True"
while caballo_x!=objetivo_x and caballo_y!=objetivo_y:
    if flow:
        
        caballo_x +=1
        caballo_y +=2
        print(f"({caballo_x},{caballo_y})",end=" , ")
    else:
        caballo_x +=2
        caballo_y +=1
        print(f"({caballo_x},{caballo_y})",end=" , ")
    flow= not flow
