class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result  =  []
        for string in dictionary:
            k =  0
            j =   0
            while k < len(s) and j   <  len(string) :
                if string[j] == s[k]:
                    k+=1
                    j+=1
                else:
                    k+=1
             

            if j   == len(string):
                result.append(string)
        my_dict =  {}
        for i in result  :
            my_dict[i]  = len(i)
        check   =  []
        maximum =  0
        for i in my_dict:
            maximum =  max(my_dict[i] , maximum)
        checker =  []
        for i in my_dict:
            if my_dict[i] == maximum:
                checker.append(i)
        checker.sort()
        if checker:
            return checker[0]
        return ""





        