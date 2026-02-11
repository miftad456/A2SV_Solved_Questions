class Solution:
    def frequencySort(self, s: str) -> str:
       from collections import Counter
       element   =  Counter(s)

       result = ''.join(char  * count for char,count in element.most_common())
       return result
