class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        f={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        for i in range(len(t)):
            if t[i] in f:
                f[t[i]]+=1
            else:
                f[t[i]]=1
        if d==f:
            return True
        return False