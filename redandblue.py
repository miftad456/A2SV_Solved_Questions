n =  int(input())
for i in range(n):
    m  = int(input())
    array   =   [ int(i) for i in input().split()]
    b =  int(input())
    array_b =   [ int(i) for i in input().split()]

    curr_a =  0
    max_arr =  0

    for i in array:
        curr_a += i
        max_arr  = max(max_arr , curr_a)
    curr_b  = 0
    max_arr_b   = 0
    for i in array_b:
        curr_b += i
        max_arr_b =  max(max_arr_b,curr_b)
    print(max_arr_b + max_arr)
