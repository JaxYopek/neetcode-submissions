class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []  # indices, with nums[stack] in decreasing order

        for i, x in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < x:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)

        return ans


