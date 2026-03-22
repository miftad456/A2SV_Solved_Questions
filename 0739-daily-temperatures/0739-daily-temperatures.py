class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer =  [0] * len(temperatures)

        stack  =  []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:

                cut_off =  stack.pop()

                answer[cut_off]  =  i -  cut_off

            stack.append(i)
        return answer
        