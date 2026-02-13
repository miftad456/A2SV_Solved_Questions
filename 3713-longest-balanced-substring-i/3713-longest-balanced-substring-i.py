class Solution:
    def longestBalanced(self, s: str) -> int:
        n  =  len(s)
        max_len =  0
        for start in range(n):

            freq  = [0] * 26
            for end in range(start,n):
                indx =  ord(s[end])  - ord('a')
                freq[indx] +=1

                values = [f for f in freq if f>0]

                if len(values) > 0 and min(values) ==  max(values):
                    max_len =  max(max_len,end - start + 1 )
        return max_len
        