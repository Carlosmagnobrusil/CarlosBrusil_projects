List1=[]    # Creo una lista vacia 
for x in range (1,21,1):    #creo un bucle que crea numeros del uno al 20 que van aumentando de uno en uno
    List1.append(x) #utiliuzo el metodo apend para que cada numero que se va creandoi en el bucle se añada a mi lista vacia  
#print(List1) #Con este print comprobe que la creacion de la lista haya sido correcta 

for x in List1:
    if x%3==0 and x%5==0:     ##con el condicional if estoy estableciendo una revision para todos aquellos numeros que sean divisibles exactos de 3 y 5
        print('FizzBuzz')
    elif x%5==0:    #con el condicional if estoy estableciendo una revision para todos aquellos numeros que sean divisibles exactos de 5
        print('Buzz')   #le estoy pidiendo al codigo que todos los numeros que sean divisibles de cinco imprima la cadena 'Buzz'
    elif x%3==0:  #con el condicional if estoy estableciendo una revision para todos aquellos numeros que sean divisibles exactos de 3
        print('Fizz')   #le estoy pidiendo al codigo que todos los numeros que sean divisibles de tres imprima la cadena 'Fizz'
    else:
        print(x)    #Con el condicional else estoy diciendo que para cualquier otro nuemro que no cumpla las condiciones if o elif
                    #imprima unicamente el numero

#El orden de como planteo es muy importante siempre primero debe ir la condicional compuesta como las que son llamadas por los
#conectores logicos and,or, etc.