class Solution:
    def isHappy(self, n: int) -> bool:
        visits  = set()
        def check(n):
            output = 0
            while n:
                digit =  n%10
                output+=digit**2
                n//=10
            return output
        while n not in visits:
            visits.add(n)
            n =  check(n)
            if n==1:
                return True
        return False
        