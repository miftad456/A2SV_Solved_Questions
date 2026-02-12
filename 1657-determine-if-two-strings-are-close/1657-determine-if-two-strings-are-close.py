class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        string1 = Counter(word1)
        string2  =  Counter(word2)
        array1 =[]
        array2 = []
        for i in string1:
            array1.append(string1[i])
        for i in string2:
            array2.append(string2[i])
        array1.sort()
        array2.sort()
        response = list(zip(array1,array2))
        for i ,j in response:
            if i!=j:
                return False
        return True


        

        