class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)  % 2 !=0   :
            return []
        changed.sort()
        freq =  Counter(changed)
        result   = []
        for i in changed:
            if freq[i]  == 0:
                continue
            if freq[2*i] ==0:
                return []
            result .append(i)
            freq[i]-=1
            freq[2*i]-=1
        return result 
        