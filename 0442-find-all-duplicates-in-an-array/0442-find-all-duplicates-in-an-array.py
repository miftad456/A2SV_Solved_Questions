class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        from collections import Counter
        check = Counter(nums)
        return [nums for nums in check if check[nums]==2]

        