class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        overlap  = [0] * (len(nums) + 1)
        for start ,  end in requests:
            overlap[start] += 1
            overlap[end  +  1] -= 1
      
        for i in range(1, len(overlap)):
            overlap[i] +=  overlap[i - 1]

        nums.sort()
        overlap.sort()
        ans =  sum([nums[i] *  overlap[i  +  1]for i in range(len(nums))])
        return ans % (10 ** 9 + 7)