arr = [5,3,6,7,9,1,8,2,4]

for x in range(len(arr)-1):
    small= x
    for y in range (x+1, len(arr)):
        if arr[y]<arr[small]:
            small = y
    temporal = arr[small]
    arr[small]=arr[x]
    arr[x]=temporal 
print(arr)