#User function Template for python3

class Solution:
    from collections import Counter
    def isSubset(self, a, b):
        check = self.Counter(a)
        check2  = self.Counter(b)
        for i in check2:
            if i not in check or check2[i] > check[i]:
                return False
        else:
            return True
    
    
    
