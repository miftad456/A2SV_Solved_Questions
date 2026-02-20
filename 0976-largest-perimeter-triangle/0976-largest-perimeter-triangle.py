class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        result   = 0
        nums.sort()
        for i in range(len(nums)  -  2):
            a  ,  b , c  = nums[i] , nums[i+1]  , nums[i+2]
            if a + b  > c and b +  c >  a and a + c  > b:
                result  = max(result , a + b + c)
        return result   
        