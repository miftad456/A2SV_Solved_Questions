class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left  = 1
        right =  max(piles)
        ans  =  - 1
        def  check(mid ,piles , h):
        
            hour =  0
            for i in piles:
                if i < mid:
                    hour += 1
                else:
                    hour += ceil(i /mid )

            return hour <= h



        while left <=  right :
            mid  =  (left +  right) //  2
            if  check(mid , piles, h):
                ans  =  mid
                right  =  mid - 1
            else:
                left =  mid + 1
        return ans

        