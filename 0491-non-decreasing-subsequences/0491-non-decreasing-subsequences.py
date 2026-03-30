class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        all_combinations = []
        min_length = 2
        for i in range(min_length, len(nums) + 1):
            all_combinations.extend(list(combinations(nums, i)))

        change =  set(all_combinations )
        lists  =  list(change)
        results  = []
        for i in lists:
            for j in range(1, len(i)):
                if i[j] < i[j-1]:   
                    break
            else:
                results.append(i)
        return results