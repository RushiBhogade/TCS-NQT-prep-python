n=13
day="mon"
find="sunday"


days=["sun","mon","tus","wed","thr","fri","sat"]

count=n//7

remider=n %7

index= days.index(day) 

print(count)
print(remider)
print(index)

for i in range(remider):
    if(days[(index+i)%7]=="sun"):
        count+=1
print(count)        
