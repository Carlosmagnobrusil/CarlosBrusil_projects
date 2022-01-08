P = 400000 #valor del capital delprestamo
R = 0.03 #tasa de interes
r = R/12
#print(r)
N = 30 #numero de años
n = N*12 #Termino o numero de pagos a realizar.

pmensual = P * ((r*((1+r)**n))/(((1+r)**n)-1))

print('\n','*'*50,'\n Pago Mensual:',round(pmensual,ndigits=2),'\n','*'*50 )