class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter
        freq  =  Counter(nums)
        maximum  = 0
        result  = 0 
        for i in freq:
            if freq[i] > maximum:
                maximum  = freq[i]
        for i  in nums:
            if freq[i] == maximum:
                result+=1
        return result


        