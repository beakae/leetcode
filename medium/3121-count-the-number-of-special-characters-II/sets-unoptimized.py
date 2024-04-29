# beats 73% runtime and 54% memory
# O(n) time and O(n) space

class Solution:
    def numberOfSpecialChars(self, word#: str
                             ) -> int:
        seen_upper = set()
        seen_lower = set()
        wrong = set()
        right = set()
        
        ans = 0
        
        for char in word:
            if char.islower():
                if char.upper() not in seen_upper and char not in wrong:
                    right.add(char)
                elif char.upper() in seen_upper and char in right:
                    right.remove(char)
                    wrong.add(char)
                seen_lower.add(char)
            else:
                seen_upper.add(char)
        
        for char in right:
            if char.upper() in seen_upper:
                ans += 1
        return ans