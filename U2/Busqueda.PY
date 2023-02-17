lista = [-5,2,3,6,1,9,14]
Lista2 = [-3,0,5,7,9,10,14]
n = int(input("ingrese un numero:"))

def lineNotSort(lista, n):...
def linearSort(lista, n):
    lista
    c = False
    i = 0
    while c is False and i < len(lista) and lista[i] <= n:
        if lista[i] == n:
            c = True
        i += 1
    if c is True:
        return i-1
    else:
        return None
print(linearSort(lista,n))
print(linearSort(Lista2,n))
