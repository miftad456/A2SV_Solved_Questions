class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq  = Counter(nums)
        check  = []
        for i in freq:
            check.append([freq[i],i])
        res = sorted(check, key =  lambda x : x[0])
        slice_it  = res[-k:]
        print(slice_it)
        numbers  = [j for i,j in slice_it]
        print(numbers)
        return numbers



        