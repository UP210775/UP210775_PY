# Programas Unidad 1

## Joshua Natanael Martinez Alonso / UP210775

## Biseccion

- - -
```
import math

def fnEcuacion(valor):
    return (math.pow(valor, 2))-2

x1 = 1
x2 = 2

Es = 0.001
Er = abs(x2-x1)
i = 1
it = round((math.log(x2-x1)-math.log(Es))/math.log(2))
print(it)

print("i   |     x1    |     x2    |      Er   |     xm    |"
           "   f(x1)   |   f(xm)   | f(x1) * f(xm) |\n")

while Er >= Es:
    xm = (x1 + x2) / 2
    print("{} |{} |{} |{} |{} |{} |{} \n".format(i, x1, x2, Er, xm,  fnEcuacion(x1), fnEcuacion(xm)))
    if (fnEcuacion(x1) * fnEcuacion(xm)) < 0:
        x2 = xm
    else:
        x1 = xm
    Er = abs(x2-x1)
    i = i + 1

print(xm)

- - - 
```
## Run Code 
![m]("C:\Users\joshu\OneDrive\Imágenes\README\BiseccionPY.png")

- - - 
## Numero secreto 
- - - 
```
import random

secret_num = random.randint(1,100)


print('""""""Bienvenido al juego del número secreto""""""')
print("Tienes que adivinar un número entre el 1-100")


while True:
    opcion = int(input("Para comenzar presiona escribe un 1 o para salir un 0:"))
    if opcion == 0:
        break
    elif opcion == 1:
        while True:
            n = int(input("Ingresa un numero: "))
            if n < secret_num:
                print("El numero secreto es mayor.")
            elif n > secret_num:
                print("El numero secreto es menor.")
            elif n == secret_num:
                print("Has encontrado el número secreto: {}".format(secret_num))
                print("Has ganado")
                break

- - - 
```
## Run code 
![m]("C:\Users\joshu\OneDrive\Imágenes\README\Numero secreto.png")
- - - 
## Boleto
- - - 
```
n = 0
sumatoria1 = int(input("Ingrese la sumatoria: "))
i = 0
sumatoria2 = 0
c = sumatoria1


while sumatoria1>0:
    i += 1
    sumatoria1 -=i
    if sumatoria1 <0:
        print("Numero inexacto: {}".format(i-1))
        n = i-1
    elif sumatoria1 ==0:
        print("Numero exacto: {}".format(i))
        n = i

for i in range(1, n+1):
    sumatoria2 += i
restante = c-sumatoria2
print("La sumatoria es : {}".format(sumatoria2))
print("Restante = {} - {} = {}".format(c,sumatoria2,restante))
- - - 
```
## Run code 
![m]("C:\Users\joshu\OneDrive\Imágenes\README\BoletoPY.png")
- - -
## Bubble
- - - 
```
import random

lista = random.sample(range(100),10)
print(lista)

for i in lista:
    for j in range((len(lista))-1):
        if lista[j] > lista[j+1]:
            lista[j],lista[j+1] = lista[j+1],lista[j]
print(lista)
- - - 
```
## Run code
![m]("C:\Users\joshu\OneDrive\Imágenes\README\BubblePY.png")
- - -
## Matriz
- - - 
```
import random
#Se pide el tamaño de la matriz con un bucle que solo permite numeros enteros
while True:
    try:
        n = int(input("Ingrese el tamaño de la matriz: "))
    except ValueError:
        print("Ingrese un numero entero.")
    else:
        break
#Se crea una lista con numeros aleatorios sin repetir con un rango del tamaño al cuadrado
lista = random.sample(range(n**2), (n**2))
#Se crea la matriz con los elementos de la lista
matriz = [[(lista.pop()) for i in range(n)] for i in range(n)]
#Se imprime la matriz
print("Matriz:")
for i in matriz:
    for j in i:
        print(f"{j:3d}", end = " ")
    print()
#Se obtiene la diagonal de la matriza en la variable lista
for i in range(n):
    for j in range(n):
        if i == j:
            lista.append(matriz[i][j])
#Se imprime la lista
print("Diagonal de la matriz:\n",lista)
#Se obtiene la otra diagonal de la matriz en la variable lista2
lista2 = []
for i in range(n):
    lista2.append(matriz[i][(n-1)-i])
#Se imprime lista2
print("Diagonal invertida de la matriz:\n",lista2)
- - - 
```
## Run code
![m]("C:\Users\joshu\OneDrive\Imágenes\README\MatrizPY.png")