class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        revers=0
        xcopy=x
        while x>0:
            revers=(revers*10)+(x%10)
            x//=10
        return xcopy==revers

        
