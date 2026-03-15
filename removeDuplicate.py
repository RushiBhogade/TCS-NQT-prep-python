arr=[1,2,3,4,4,3,2,4,6,7]

setArr=list(set(arr))
print(setArr)

unique =[]

# by the loop 

for num in arr:
    if num not in unique:
        unique.append(num)
print(unique)