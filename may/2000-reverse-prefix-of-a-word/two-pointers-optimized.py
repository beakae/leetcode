# beats 85% runtime and 93% memory
# O(n) time and O(n) space

class Solution:
    def reversePrefix(self, word#: str
                      , ch#: str
                      ) -> str:
        def find_index(word, ch) -> int:
            for i in range(0, len(word)):
                if word[i] == ch:
                    return i
            return -1
        
        left = 0
        right = find_index(word, ch)

        word = list(word)
        
        while left <= right:
            temp = word[left]
            word[left] = word[right]
            word[right] = temp
            left += 1
            right -= 1
        
        return ''.join(word)