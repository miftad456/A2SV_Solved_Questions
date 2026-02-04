class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        import math
        from collections import Counter
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0:
                return False

            limit = int(math.sqrt(n))
            for i in range(3, limit + 1, 2):
                if n % i == 0:
                    return False
            return True
        freq =  Counter(nums)
        for i in freq:
            if is_prime(freq[i]):
                return True
        else:
            return False
        

                