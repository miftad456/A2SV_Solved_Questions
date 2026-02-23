for i in range(int(input())):
    n , k = map(int,input().split())
    all_array  = []
    for i in range(n):
        array =  [int(i) for i in input().split()]
        all_array.append(array)
    all_array.sort()
    for i in  (all_array):
        if i[0] <= k  and   i[2]  > k:
            k =  i[2]
    print(k)
