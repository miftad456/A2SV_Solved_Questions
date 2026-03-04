for i in range(int(input())):
    n , m  = map (int,input().split())
    color  = input()

    record =  0
    for i in range(m):
        if color[i] ==  "W":
            record += 1
    

    minimum =  record 

    left =  0
    for j in range(m , n):
        
        if color[j]  == "W":

            record += 1
        if color[left] =="W":
            record -= 1
        left += 1

        minimum  =  min(minimum , record)
    print(minimum)
