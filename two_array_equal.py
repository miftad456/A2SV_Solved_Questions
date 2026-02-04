class Solution:
    def checkEqual(self, a, b) -> bool:
        a.sort()
        b.sort()
        return True if a==b else False
