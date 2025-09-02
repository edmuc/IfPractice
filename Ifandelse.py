#Implrementar
#A= int ("10")

#print (type(A), "y la variable valoR", A)
#Convertir los tipos de datos Float, Int, String entre si
#result= A+A

# Estructura de control, Operaciones logicas
#Booleano, 1,0,

#if(A>5):
#    print ("Este es el resultado del if verdadero")
#    print (f"La variable a es igual a: {A}")    
#else:
#    print ("La condicion no se ejecuto")


X= int(input("Ingrese el valor de X: "))
Y= int(input("Ingrese el valor de Y: "))
Z= int(input("Ingrese el valor de Z: "))
W= int(input("Ingrese el valor de W: "))

# Mayor que
if X > Z:
    print(f"{X} es mayor que {Z}")
else:
    print(f"{X} no es mayor que {Z}")

# Menor que
if W < Y:
    print(f"{W} es menor que {Y}")
else:
    print(f"{W} no es menor que {Y}")

# Igual que
if X == Z:
    print(f"{X} es igual a {Z}")
else:
    print(f"{X} no es igual a {Z}")

# Mayor o igual que
if Y >= W:
    if Y > W:
        print(f"{Y} es mayor que {W}, pero no igual")
    else:
        print(f"{Y} es igual a {W}")
else:
    print(f"{Y} no es mayor o igual que {W}")

# Menor o igual que
if Z <= X:
    if Z < X:
        print(f"{Z} es menor que {X}, pero no igual")
    else:
        print(f"{Z} es igual a {X}")
else:
    print(f"{Z} no es menor o igual que {X}")