arr = [5,3,6,7,9,1,8,2,4]

for x in range(1, len(arr)):
    act = arr[x]
    index = x
    while index>0 and arr[index-1]>act:
        arr[index] = arr[index-1]
        index =index -1 
    arr[index]=act
print(arr)