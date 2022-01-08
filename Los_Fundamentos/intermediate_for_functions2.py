x = [ [5,2,3], [10,8,9] ] 
x[1][0]= 15
print(x)


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name']= 'Bryant'
print(students)


sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0]= 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y']= 30
print(z)

students1 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students1):
     for x in students1:
          name=''
          for y,z in x.items():
               if name == '':
                    name += y + "-" + z
               else:
                    name+= ', '+ y + ' - ' + z 
          print(name)

iterateDictionary(students1)

def iterateDictionary2 (kn, lst):
     for x in lst:
          print(x[kn])

iterateDictionary2('first_name', students1)
iterateDictionary2('last_name', students1)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo (sdict):
     for k in sdict.keys():
          print (len(sdict[k]),k.upper())
          for l in sdict[k]:
               print(l)

printInfo(dojo)
        




