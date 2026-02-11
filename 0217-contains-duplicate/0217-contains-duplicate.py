class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq=  Counter(nums)
        for i in freq:
            if freq[i] >=2:
                return True
        return False
        