class Solution:
    def minSteps(self, s: str, t: str) -> int:
        first = Counter(s)
        sec= Counter(t)
        res =  0
        for i in first:
            if sec[i] < first[i]:
                res+= first[i] - sec[i]
        return res
