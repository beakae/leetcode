# beats 88% runtime and 79% memory
# O(n) time and O(1) space

class Solution:
    def dailyTemperatures(self, temperatures#: List[int]
                          ) -> int:#List[int]:
        stack = []
        length = len(temperatures)
        ans = [0] * length

        for i in range(length - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                ans[i] = stack[-1] - i
            
            stack.append(i)
        return ans