# beats 62% runime and 70% memory
# O(n) time and O(1) space

class Solution:
    def reverseString(self, s#: List[str]
                      ) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while right > left:
            placeholder = s[left]
            s[left] = s[right]
            s[right] = placeholder

            left += 1
            right -= 1