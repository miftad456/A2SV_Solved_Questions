class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        res = []
        for k in range(len(nums) + 1):
            res.extend(combinations(nums, k))
        print(res)
        return res
                