class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        from collections import Counter
        freq =  Counter(nums)
        result =  0
        for  i in freq:
            if freq[i] % k ==0:
                result +=  freq[i] * i
        return result
        