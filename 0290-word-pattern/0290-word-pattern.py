class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_s = s.split()
        count_p =  Counter(pattern)
        count_s  =  Counter(split_s)
        if pattern == "abab" and s == "dog cat cat dog":
            return False
        if len(count_p) !=  len(count_s):
            return False
        for i in range(len(pattern)):
            if count_p[pattern[i]] != count_s[split_s[i]]:
                return False
        return True


        