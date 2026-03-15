n = int(input("Enter number of towers"))
towersHight = []
for _ in range(n):
    towersHight.append(int(input("Enter the hight of the tower")))

print("the second largest hight of thr tower is ", sorted(towersHight)[-2])




#### now second smallest

print("the second smallest hight of thr tower is ", sorted(towersHight)[1])