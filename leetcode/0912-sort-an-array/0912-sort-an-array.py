class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merging(nums):
            if len(nums) <= 1:
                return nums
            middle  = len(nums) // 2
            left  = merging(nums[:middle])
            right  =  merging(nums[middle:])

            return merge(left , right)
        def merge(left , rigth):
            i , j  =  0 , 0
            result  = []
            while  i < len(left) and  j < len(rigth):
                if left[i] <= rigth[j]:
                    result .append(left[i])
                    i  +=  1
                else:
                    result.append(rigth[j])
                    j+= 1
            result.extend(left[i:])
            result.extend(rigth[j:])
            return result
        return merging(nums)
                