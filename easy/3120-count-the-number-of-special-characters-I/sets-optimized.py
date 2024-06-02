# beats 77% runtime and 92% memory
# O(n) time and O(1) space

class Solution:
    def numberOfSpecialChars(self, word#: str
                             ) -> int:
        seen_lower = set()
        seen_upper = set()
        
        ans = 0
        
        for char in word:
            if char.islower():
                seen_lower.add(char)
            else:
                seen_upper.add(char.lower())
        for char in seen_lower:
            if char in seen_upper:
                ans += 1
        
        return ans