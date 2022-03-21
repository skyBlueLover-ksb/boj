from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):

            while stack and temperature > temperatures[stack[-1]] :
                temp = stack.pop()
                answer[temp] = i-temp
            stack.append(i)

        return answer

