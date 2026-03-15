arr=[1,0,5,0,3,4,2]
i=0
while i< len(arr):
    if(arr[i]==0):
        arr.pop(i)
        arr.append(0)
    else:
        i+=1
print(arr)    