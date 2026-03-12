class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums  == [0]:
            return True
        mx = 0 
        for i in range(len(nums)):
            
            step =  max(mx-1,nums[i])
            if step<= 0 and i < len(nums) :
                return False
            mx =  step
         
        return True

        