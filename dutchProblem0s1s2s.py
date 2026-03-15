#rearrge array by 0s 1s 2s
arr=[1,0,1,2,0,1,0,2,1,0,2,2,0,1,1,0]

# simple way

arr.sort()
print(arr)



# this can be use without any hesitation
count0=arr.count(0)
count1=arr.count(1)
count2=arr.count(2)

newarr=[0]*count0 + [1]*count1+[2]*count2   



##### this can be solution but if only we dont want in sorted arry this print like [1,1,2,2,0,0]
freq={}
for num in arr:
    freq[num]= freq.get(num,0)+1

newArr=[]
for key,value in freq.items():
    for i in range(value):
        newArr.append(key)
print(newarr)    
