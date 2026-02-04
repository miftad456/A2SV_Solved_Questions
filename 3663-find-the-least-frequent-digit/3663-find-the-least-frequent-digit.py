class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        from collections import Counter
        strs  =  str(n)
        freq = Counter(strs)
        mins =  float("inf")
        for i in freq:
            mins =  min(mins,freq[i])
        result  = float("inf")
        for i in freq:
            if freq[i] == mins:
                result  =  min(int(i),result)
        print(mins)
        return result


        