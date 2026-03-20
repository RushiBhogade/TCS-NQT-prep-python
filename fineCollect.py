numberofVechicls=int(input("Enter Number of vechical:-"))
arr=[]
for i in range(numberofVechicls):
    arr.append(int(input(f"Enter vechical number {i+1}")))
date=int(input("Enter date:"))
fine=int(input("Enter fine:"))
isEven=False
collectedFine=0

if(date % 2 == 0):
    isEven=True

for i in range(len(arr)):
    if(isEven):
        if(arr[i]%2!=0):
            collectedFine+=fine
    else:
        if(arr[i]%2==0):
            collectedFine+=fine

print(collectedFine)



