class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        array = [i for i in range(1, n + 1)]
        ans = []

        def backtrack(index, path):
        
            if len(path) == k:
                ans.append(path[:])
                return     
            if index == len(array):
                return   
            path.append(array[index])
            backtrack(index + 1, path)
            path.pop()
            
            backtrack(index + 1, path)

        backtrack(0, [])
        return ans


                