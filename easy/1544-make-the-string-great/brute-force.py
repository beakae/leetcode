# beats 83% runtime and 91% memory
# O(n^2) time and O(n) space

class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s):
            if s[i].isupper():
                if i - 1 >= 0 and s[i].lower() == s[i-1]:
                    s = s[:i-1] + s[i+1:]
                    i = 0
                elif i + 1 < len(s) and s[i].lower() == s[i+1]:
                    s = s[:i] + s[i+2:]
                    i = 0
                else:
                    i += 1
            else:
                i += 1
        return s