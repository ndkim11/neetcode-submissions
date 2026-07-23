class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i,tem in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < tem:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i

            stack.append(i)

        return res