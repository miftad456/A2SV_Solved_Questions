class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def check(left , right, turn ):
            if left >= right :
                return  0 
            if turn == 0:
                return max(check(left+1 ,right, 1-  turn)+ nums[left] , check(left,right -1,1-turn) + nums[right])
            else:
                return min(check(left+1 ,right, 1-  turn) -nums[left] , check(left,right -1,1-turn) - nums[right])
        return check(0,len(nums)-1,0) >= 0

         
        