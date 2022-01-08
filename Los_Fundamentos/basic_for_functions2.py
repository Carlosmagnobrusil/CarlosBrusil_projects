regresiva = []
def cuenta_regresiva(x):
    for x in range (x,-1,-1):
        regresiva.append(x)
    return(regresiva)
cr = cuenta_regresiva(8)
print(cr)



def print_and_return (lista):
    print(lista[0])
    return (lista[1])
print(print_and_return([6,23]))


def first_plus_length (lista1):
    x = len(lista1)
    return lista1[0] + x

print(first_plus_length([12,23,4,5,1]))


lista2 = []
def length_and_value(a,b):
   for _ in range(0,a):
    lista2.append(b)
   return lista2
print (length_and_value(10,9))