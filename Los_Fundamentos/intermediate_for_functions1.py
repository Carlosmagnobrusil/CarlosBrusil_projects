import random
def randint(min= 0  , max= 100 ):
    x = random.random() * max + min
    return round(x)

print (randint())
print (randint(max=50))
print (randint(min=50))
print (randint(min=50,max=500))
print (randint(min=300))
print (randint(max=-1))
