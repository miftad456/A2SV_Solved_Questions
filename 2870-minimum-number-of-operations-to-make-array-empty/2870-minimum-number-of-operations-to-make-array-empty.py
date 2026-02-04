class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)
        result = 0
        for f in freq.values():
            if f == 1:
                return -1
            if f % 3 == 0:
                result += f // 3
            elif f % 3 == 1:
                result += (f // 3 - 1) + 2
            else: 
                result += f // 3 + 1

        return result



            