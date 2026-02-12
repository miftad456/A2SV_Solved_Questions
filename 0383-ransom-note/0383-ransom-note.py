class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        for i in ransomNote:
            if ransomNote.count(i)>magazine.count(i):
                return False
        return True
        