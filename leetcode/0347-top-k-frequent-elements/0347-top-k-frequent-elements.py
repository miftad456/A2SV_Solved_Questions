class Solution:
   def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
    freq = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

  
    for key, value in freq.items():
        buckets[value].append(key)
    
    result = []
    
 
    for i in range(len(buckets) - 1, -1, -1):
        for element in buckets[i]:
            result.append(element)
            if len(result) == k:
                return result



        # freq  = Counter(nums)
        # check  = []
        # for i in freq:
        #     check.append([freq[i],i])
        # res = sorted(check, key =  lambda x : x[0])
        # slice_it  = res[-k:]
      
        # numbers  = [j for i,j in slice_it]
      
        # return numbers
        
        