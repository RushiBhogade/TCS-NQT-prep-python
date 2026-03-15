a=[1,4,5,6,4]
b= [3,4,6,4,5]
k=2
heap=[]

def sortbyB(x):
    return x[1]
sort=sorted(zip(a,b), key=sortbyB)
newObjects =[(x,y) for x,y in sort]

for start,end in newObjects:
   if(len(heap)<k):
       heap.append[end]
       count+=1
   else:
       if(heap[0]<end):
           heap.pop[0]
           count+=1
           heap.append[end]