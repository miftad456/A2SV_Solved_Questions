class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window  =  defaultdict(int)
        target =  Counter(p)
        left  = 0
        result   = []
        for i in range(len(s)):
            #print(Counter(s[left:i+len(p)]))
            if Counter(s[left:i+len(p)])  ==  target:
                result . append(left)
                left += 1
            else:
                left += 1
        return result
            
        














        for  i in range(len(s)):
            if window  ==  target:
                result . append(left)
                if window[left] ==  0:
                    del window[left]
                    left  += 1 
                else:
                    window[left] -= 1
                    left +=1 
            else:
                k  =  0 
                while  k  < len(p):
                    window[s[i]] += 1

            




        