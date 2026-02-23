class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        my_dict  = defaultdict(int)
        for i in range(len(s)):
            my_dict[s[i:i+10]]+=1
        result  =  []

        for i in my_dict:
            if my_dict[i] >= 2:
                result.append(i)
        return result 
                