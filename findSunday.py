#count sundays
days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
n=input("Enter a day") # eg mondey
m=int(input("Number of days to count"))
count=0
index=0

index=days.index(n)
for i in range(m):
    if days[(index + i) % 7] == "sunday":
        count += 1
print(count)
