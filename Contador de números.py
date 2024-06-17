import os
os.system("cls")

num = int(input("Ingrese un número: "))
aux = num
cont = 0
while(aux != 0):
    b = aux % 10
    print("Último dígito ", b)
    cont += 1
    aux = aux // 10
    print("El número que queda es: ", aux)
print("El total de dígitos del número es: ", cont)