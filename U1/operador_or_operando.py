def prioridad(a):
    if a in ['(',')']:
        return 4
    elif a == '^':
        return 3
    elif a == ['*','/']:
        return 2
    elif a == ['+','-']:
        return 1

P = [5,6,2,'+','*',12,4,'/','-']
for i in P:
    try:
        float(i)
        print(f"{i} es un operando")
    except ValueError:
        if i in ['+','-','/','*','(',')','^']:
            print(f"{i} Esto es un operandor con prioridad", prioridad(i))

        else:
            print(f"{i}Esto es una letra")


