class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        freq =  defaultdict(int)
        freq[0] =  1
        result  = 0
        current_sum  = 0
        for i in nums:
            current_sum += i
            result += freq[current_sum-k]
            freq[current_sum]+=1
        return result
        