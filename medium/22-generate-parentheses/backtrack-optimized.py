# beats 50% runtime and 89% memory
# O(4^n) time and O(4^n) space

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def backtrack(s, open, close):
            if len(s) == 2*n:
                answer.append(s)
                return
            
            if (open < n):
                backtrack(s + "(", open + 1, close)
            if (close < open):
                backtrack(s + ")", open, close + 1)

        backtrack("", 0, 0)
        return answer
