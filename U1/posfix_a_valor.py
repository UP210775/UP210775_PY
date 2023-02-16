i = 0
P = [5,6,2,'+','*',12,4,'/','-']
pila = []
P.append(')')
while P[i] != ")":
    if type(P[i]) == int:
        pila.append(P[i])
    elif type(P[i]) == str:
        b = pila.pop()
        a = pila.pop()
        if P[i] == P[3]:
            c= a+b
        elif P[i] == P[4]:
            c= a*b
        elif P[i] == P[7]:
            c= a/b
        elif P[i] == P[8]:
            c= a-b
        pila.append(c)
    i += 1
print(pila)
