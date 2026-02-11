class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        
        
        for string  in range(len(responses)):
            responses[string] = list(set(responses[string]))
        extending = []
        for i in responses:
            extending.extend(i)
        freq = Counter(extending)
        maxs =  float("-inf")
        for i in freq:
            maxs = max(maxs,freq[i])
        result  = []
        for i in freq:
            if freq[i] == maxs:
                result.append(i)
        result.sort()
        return result[0]
