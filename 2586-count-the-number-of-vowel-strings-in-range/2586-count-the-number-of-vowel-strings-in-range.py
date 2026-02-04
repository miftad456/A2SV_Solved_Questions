class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        result = 0
        vowel = "aeiou" 
        for i in range(left,right+1):
            if words[i][0] in vowel and words[i][-1] in vowel:
                result+=1
        return result
        