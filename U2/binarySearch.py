def binarySearch(lista, valor):
    inicio = 0
    Final = len(lista)
    Mit = (inicio + Final)//2
    N = 0

    while inicio <= Final and lista[Mit] != valor:
        if valor < lista[Mit]:
            Final = Mit - 1
        else:
            inicio = Mit + 1
        Mit = (inicio + Final)//2
        N += 1
    if lista[Mit] == valor:
        return Mit, N
    else:
        return None

lista =[-3,0,1,5,7,9]
n = int(input("Elige un numero:"))
print(binarySearch(lista, n))


