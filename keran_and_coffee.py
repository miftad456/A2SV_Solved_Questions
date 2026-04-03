MAX = 200000
n, k, q = map(int, input().split())
diff = [0] * (MAX + 2)
for i in range(n):
    l , r   = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1
for i in range(1, len(diff)):
    diff[i] += diff[i  - 1]

good  =  [0] * (MAX +  2)


for i in range(len(diff)):
    if diff[i] >= k : 
        good [i]  =  1
for  i in range(1, len(good)):
    good[i] += good[i  - 1]
for i in range(q):
    a , b =  map(int, input().split())
    print(good[b]  - good [ a  - 1])
