
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heapify_max(piles)
        for i in range(k):
            root  =  heappop_max(piles)
            root  = ceil(root  / 2)
            heappush_max(piles  , root )
        return (sum(piles))





        
        