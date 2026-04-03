class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        my_dicts =  defaultdict(int)

        my_dicts[0] =  1

        sums =  0

        result  =  0

        for i in range(len(nums)):
            sums +=  nums[i]
            rem  =  sums % k
            result +=  my_dicts[rem]
            my_dicts[rem] += 1
        return result

        