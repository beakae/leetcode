# beats 80% runtime and 89% memory
# O(n) runtime and O(1) space

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        smallPointer = 0
        bigPointer = 0
        while smallPointer < len(s) and bigPointer < len(t):
            if t[bigPointer] == s[smallPointer]:
                smallPointer += 1
            bigPointer += 1
        return smallPointer == len(s)