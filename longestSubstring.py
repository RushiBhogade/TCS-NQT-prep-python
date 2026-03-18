


str="rushikesh"



char=set()
i=0
max_lenght=0
longest=""
for j in range(len(str)):
    while str[j] in char:
        char.remove(str[i])
        i+=1
    char.add(str[j])
    while j-i+1 > max_lenght:
        max_lenght = j - i+1
        longest=str[i:j+1]
               

print(max_lenght,longest)


        



