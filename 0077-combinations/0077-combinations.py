class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        array = [i for i in range(1, n + 1)]
        result  =  list(combinations(array ,k))
        print(result)
        return result