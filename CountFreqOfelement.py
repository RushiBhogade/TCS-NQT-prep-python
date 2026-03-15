from collections import Counter
arr=[1,2,4,5,3,5,4,5,6,6,4,3,3,5,6,7]


# direct by counter function but import first
print(Counter(arr))


#by the loop and the get method of dict
freq={}
for num in arr:
    freq[num]= freq.get(num,0)+1

#most number of freq eleemnet
element=0
value=0
maxvalue=0

for key,value in freq.items():
    if value > maxvalue:
        maxvalue=value
        element=key

#leaset number of freq eleemnet
for key,value in freq.items():
    if value == 1:
        element=key
        break         

print(element) 