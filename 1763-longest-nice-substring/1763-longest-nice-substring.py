class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        seen  =  set(s)
        if len(s) < 2:
            return ""
            
        for i in range(len(s)):
            if s[i] .swapcase() not in seen:
                left  = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return left  if len(left) >= len(right)  else right
        return s
        