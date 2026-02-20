class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        my_dict   = defaultdict(int)
        new_nums =  sorted(nums)
        for i , num  in enumerate(new_nums):
            if num not in my_dict:
                my_dict[num] =  i
        for i , num in enumerate(nums):
            nums[i]  =  my_dict[nums[i]]
        return nums