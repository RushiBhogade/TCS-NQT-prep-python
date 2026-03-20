n = 55
res = ""

while n > 0:
    res = str(n % 2) + res
    n = n // 2

toogle=""
for ch in res:
    if ch == "0":
        toogle+="1"
    else:
        toogle+="0"    
 

print(res)

print(toogle)