from collections import Counter
n , m  =  map(int,input().split())
array  =  [int(i) for i in input().split()]
array2  =  [int(i) for i in input().split()]
freq1 =  Counter(array2)
count  =  0
for i in array:
    if i in freq1:
        count +=  freq1[i]
print(count)



