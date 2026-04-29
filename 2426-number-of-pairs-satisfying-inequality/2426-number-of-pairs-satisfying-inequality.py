
from bisect import bisect_right, insort
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr   = [a - b for a ,b in zip(nums1  , nums2)]
        sorted_sort  = []
        count   = 0
        for val in arr :
            count  += bisect_right(sorted_sort , val + diff)
            insort(sorted_sort  , val)
        return count 