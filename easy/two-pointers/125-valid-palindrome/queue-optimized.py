# beats 91% runtime and 7% memory
# O(N) time and O(N) space

from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        queue = deque()
        for char in s:
            if char.isalnum():
                queue.append(char.lower())
        while True:
            if len(queue) == 1 or len(queue) == 0:
                break
            if queue.pop() == queue.popleft():
                continue
            return False
        return True