class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0:1}
        curr_sum  = 0
        total  =  0
        for num in nums:
            curr_sum  += num
            if curr_sum  -  goal  in count :
                total += count[curr_sum  -  goal]

            count[curr_sum ] =  count.get(curr_sum , 0) + 1
        return total
        