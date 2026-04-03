n , m    = map(int, input().split())
array = [int(i) for i in input().split()]

curr_sum  = 0
left =  0
result  = 0
for right in range(len(array)):
    curr_sum += array[right] 
    while curr_sum >= m :
        result += (n -  right)
        curr_sum-=array[left]
        left  += 1
print(result)
