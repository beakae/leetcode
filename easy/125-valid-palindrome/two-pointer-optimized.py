# beats 89% runtime and 92% memory
# O(n) time and O(1) space

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and s[left].isalnum() == False:
                left += 1
            while right > left and s[right].isalnum() == False:
                right -= 1
            if left > right or s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True