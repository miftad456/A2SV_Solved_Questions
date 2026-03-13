for i in range(int(input())):
    s  = input()
    n  = len(s)
    i = 0
    res =  set()
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        
        if (j - i) % 2 != 0:
            res.add(s[i])
        
        i = j
        
    print("".join(sorted(list(res))))
