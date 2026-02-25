class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result  = []
        freq   =  Counter(s)
        for i in order:
            if i in freq:
                result.append(i*freq[i])
                del(freq[i])
        for i in freq:
            result.append(i*freq[i])
        return "".join(result)
            