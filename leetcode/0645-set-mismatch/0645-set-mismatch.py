class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq =  Counter(nums)
        first = 0
        for i in freq:
            if freq[i] == 2:
                first = i
                break
        result  = [first]
        se =  set(nums)
        for i in range(1,len(nums)+1):
            if i  not in se:
                result.append(i)
                break
        return result
