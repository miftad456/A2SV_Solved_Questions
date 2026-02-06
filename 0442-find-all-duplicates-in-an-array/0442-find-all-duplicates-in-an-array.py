class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result  = set()
        array  = []
        for num in nums:
            if num in result:
                array.append(num)
            else:
                result.add(num)
        return array

        