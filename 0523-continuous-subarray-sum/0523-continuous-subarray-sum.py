class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dicts =  {}
        pre_sum  = 0
        for  i , num in enumerate(nums):

            pre_sum +=  num

            remender =  pre_sum % k
            if remender == 0  and i >= 1:
                return True
            if remender in dicts :
                if i -  dicts[remender] >=  2:
                    return True
            else:
                dicts[remender]  =  i
        return False
        