class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = set()
        left  = 0
        right =  0
        max_len =  0
        while right  < len(s):
            while s[right]  in freq:
                freq.discard(s[left])
                left +=1
            freq.add(s[right])
            right += 1 
            max_len =  max(max_len,len(freq))
        return max_len

    