class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        output = [0] * (len(s) +  1)
        for i , j , k in shifts:
            if  k ==  0 :
                output[i] -=  1
                output[j +  1] +=  1
            else:
                output[i] += 1
                output[j +  1] -=  1
        for i in range(1,len(output)):
            output[i]+=output[i-1]
        correct  =  output[:-1]
        result  =  []
        for i in range(len(s)):
            result.append(((ord(s[i]) - 97) +  correct[i])%26)
        results  = ""
        for i in range(len(result)):
            results +=  chr(97 +  result[i])
        return results