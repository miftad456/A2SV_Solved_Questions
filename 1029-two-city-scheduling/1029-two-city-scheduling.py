class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        array  = sorted(costs, key =  lambda x:x[0] -  x[1])

        result  =  0
        for i in range(len(array)):
            if i< len(array) // 2:
                result += array[i][0]
            else:
                result += array[i][1]
        return result