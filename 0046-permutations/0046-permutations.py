class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutation(s, start=0, result=None):
            if result is None:   
                result = []

            if start == len(s) - 1:
                result.append(s[:])   
            else:
                for i in range(start, len(s)):
                    s[start], s[i] = s[i], s[start]
                    permutation(s, start + 1, result)
                    s[start], s[i] = s[i], s[start]  
            return result
        return permutation(nums)