class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def pancakeSort(arr):
            res = []
            def flip(k):
                arr[:k] = arr[:k][::-1]

            n = len(arr)

            for size in range(n, 1, -1):

            
                max_index = arr.index(max(arr[:size]))
                
                if max_index == size - 1:
                    continue

                if max_index != 0:
                    flip(max_index + 1)
                    res.append(max_index + 1)

                flip(size)
                res.append(size)

            return res
        return pancakeSort(arr)
                