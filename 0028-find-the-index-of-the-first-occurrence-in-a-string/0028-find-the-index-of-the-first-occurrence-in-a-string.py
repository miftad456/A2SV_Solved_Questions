class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=0
        if len(haystack)<len(needle):
            return -1
        while l<len(haystack):
            k=len(needle)
            if haystack[l:k+l]==needle:
                return l
            l+=1
        return -1