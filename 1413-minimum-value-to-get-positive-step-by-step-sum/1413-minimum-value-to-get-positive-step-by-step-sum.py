class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        strt = 0

        pref = 0

        for i in nums:
            pref += i
            if pref < 1:
                strt += 1 - pref
                pref = 1
        if not strt:
            return 1
        return strt
        