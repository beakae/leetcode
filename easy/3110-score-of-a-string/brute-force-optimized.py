# beats 100% runtime and 100% memory
# O(n) time and O(1) space

class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i-1]))
        return score