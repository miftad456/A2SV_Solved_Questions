class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter
        if len(nums)%2 != 0:
            return False
        else:
            new_nums  = Counter(nums)
            for i in new_nums:
                if new_nums[i]%2==1:
                    return False
            else:
                return True

        