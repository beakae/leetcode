# beats 57% runtime and 60% memory
# O(n) time and O(n) space

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False

        letters_s = {}
        letters_t = {}

        for i in range(0, len(s)):
            if s[i] not in letters_s:
                letters_s[s[i]] = t[i]
            elif t[i] != letters_s[s[i]]:
                return False
            if t[i] not in letters_t:
                letters_t[t[i]] = s[i]
            elif s[i] != letters_t[t[i]]:
                return False
        return True