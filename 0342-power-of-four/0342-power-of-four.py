class Solution:
    def isPowerOfFour(self, n: int,x=0) -> bool:
        if n==4**x:
            return True
        if n<4**x:
            return False
        return self.isPowerOfFour(n,x+1)