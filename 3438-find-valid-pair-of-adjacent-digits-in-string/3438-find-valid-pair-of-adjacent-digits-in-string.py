class Solution:
    def findValidPair(self, s: str) -> str:
        count =  Counter(s)
        for a,b in pairwise(s):
            if a !=  b and count[a] == int(a) and count[b] == int(b):
                return a+b
        return ''  
        