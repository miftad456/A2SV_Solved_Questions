class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        collect =  Counter(answers)

        total  =  0
        for i , j in collect.items():
            size  =  i + 1
            group =  ceil(j / size)
            total += group  * size
        return total
        