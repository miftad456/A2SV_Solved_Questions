class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        a=0
        b=0
        res=""
        ret=[]
        while b<len(s):
            if s[b] not in res:
                res+=s[b]
                b+=1
                if b==len(s):
                    ret.append(len(res))
            elif s[b] in res:
                ret.append(len(res))
                res=""
                a+=1
                b=a
          
               
        if ret:
            return max(ret)
        return 0