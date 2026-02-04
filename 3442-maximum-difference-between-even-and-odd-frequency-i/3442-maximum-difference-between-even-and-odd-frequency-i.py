class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter
        counter =  Counter(s)
        max_odd = -1
        min_even =  float("inf")
        for count  in counter.values():
            if count % 2 ==1:
                max_odd =  max(count,max_odd)
            else:
                min_even  = min(min_even,count)
        if max_odd == -1 or min_even ==  float("inf"):
            return 0
        else:
            return max_odd -  min_even 
