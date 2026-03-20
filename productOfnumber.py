num=1727
product=1
# for i in range(len(str(num))):
#     last=num % 10
#     product= product * last
#     num = num // 10
# print(product)    



for ch in str(num):
    product*= int(ch)
print(product)    