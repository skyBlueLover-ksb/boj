class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i, cur in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur:
                j = stack.pop()
                answer[j] = i-j

            stack.append(i)

        return answer
