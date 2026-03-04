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
            result.append(ord(s[i])- ord("a"))
        final =   []
        for i in range(len(result)):
            final.append((result[i] +  correct[i]) % 26)
        for i in range(len(final)):
            final[i]  =  97 +  final[i]
        for i in range(len(final)):
            final[i]  = chr(final[i])
        return "".join(final)