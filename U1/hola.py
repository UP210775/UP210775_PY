# hola mundo #
print("hola mundo")

print("-------------------------------------------")
#the function in python is diferente for the identation
a=[5,2,7,9,3]

for i in range(0, len(a)):
    print(a[i])

#bubble sort

for i in range(0, len(a)+1 -2):
    for j in range (0, len(a)+1 -i-2):
        x = a[j]
        y = a[j+1]
        if x > y:
            a[j] = y
            a[j+1] = x

print(a)

print("-----------------------------------------")

#funcion
a = 3
b = 4

def formula (a, b):
    suma = a**2 + b**2
    C = suma**.5

    return C
print(formula(a, b))

print("------------------------------------------")

#Funcion 2
leg_a = float(input("input first leg length:"))
leg_b = float(input("input second leg length:"))
leg_c = (leg_a**2 + leg_b**2) ** .5

print(round(leg_c, 4))
print("%.3f" % leg_c)
print(f'{leg_c:.2f}')


print(f'{1:0<6d}')

print("hypotenuse length is " + str(leg_c))

print("------------------------------------------")
#
x = 1
y = 1/(x + 1/(x + 1/(x + 1/x)))
print(y)

print("------------------------------------------")

horas = 12
minutos = 17
duracion = 59

horas_final = (horas+(minutos+duracion)//60)%24
minutos_finales = (minutos+duracion)%60

print(horas_final, ":" ,minutos_finales)

print("-----------------------------------------")
mayor = 0
num = int(input('Digite un numero entero positivo:'))
aux = num
menor = num

while num >= 1:
    aux = num % 10

    if aux > mayor:
        mayor = aux

    if aux < menor:
        menor = aux

    num = num/ 10

print('Digito mayor %d' %mayor)
print('Digito menor %d' %menor)

print("----------------------------------")
x = int(input(2))
y = int(input(4))

x = x // y
y = y // x

print(y)

print("-------------------------------------------")

