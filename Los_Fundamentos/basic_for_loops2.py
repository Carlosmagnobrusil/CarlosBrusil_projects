def big(lista0):
    bigger=[]
    for y in lista0:
        if y>0:
             bigger.append("Big")
        else:
            bigger.append(y)
    return bigger
print(big([-2,3,-1,1]))

def positives(lista1):
    positive=[]
    w=0
    for y in lista1:
        if y>0:
            w= w + 1
            positive.insert(len(lista1),w)
        else:
            positive.append(y)
    return positive
print(positives([-2,1,2,4]))

def sum_total(lista2):
    if len(lista2) < 1:
        return False
    else:
        return lista2[0] + sum_total(lista2[1:])
print(sum_total([0,6,7,9,23]))

def average(lista3):
    if len(lista3)==0:
        return 0
    else:
        return (lista3[0]+average(lista3[1:]))/len(lista3)
print(average([23,45,6,9]))

def lenght(lista4):
    return len(lista4)
print(lenght([10,7,9]))

def maximun(lista5):
    if len(lista5)==0:
        return "False"
    else:
        return max(lista5)
print(maximun([-4,23,22,134]))

def minimun(lista6):
    if len(lista6)==0:
        return "False"
    else:
        return min(lista6)
print(minimun([-12,10,-8,5]))