n , m  = map(int,input().split())
array  =  [int(i) for i in input().split()]

if n  == 1:
    print(array[-1]   - array[0])
else:
    numbers =  []
    for i in range(len(array ) -  1):
        numbers .append(array[i + 1] -  array[i])
    numbers .sort(reverse=True)
    #print(numbers)

    total  =  array[-1]  -  array[0]
    for j in range(m-1):
        total -=  numbers[j]
    print(total)
