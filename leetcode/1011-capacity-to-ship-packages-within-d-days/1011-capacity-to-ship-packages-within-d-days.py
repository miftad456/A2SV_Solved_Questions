class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(current , weights):
            day =  1
            sums = 0
            for i in weights:
                if sums  + i >  current:
                    day += 1
                    sums  = i
                else:
                    sums += i
            return day <=  days

        ans  = -1
        low  = max(weights)
        high =  sum (weights)

        while low <= high:
            mid  = (low +  high)//2
            if check(mid,weights):
                ans  =  mid
                high =  mid - 1
            else:
                low =  mid + 1
        return ans

        