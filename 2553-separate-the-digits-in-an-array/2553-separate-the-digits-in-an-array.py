class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result  = []
        for i in nums:
            res= str(i)
            for i in range(len(res)):
                result.append(int(res[i]))
        return result
        