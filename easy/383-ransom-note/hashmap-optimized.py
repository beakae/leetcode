# beats 92% runtime and 84% memory
# O(n + m) time and O(1) space

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap = Counter(magazine)

        for char in ransomNote:
            if magazineMap[char] == 0:
                return False
            else:
                magazineMap[char] -= 1
        return True

        # letterPairs = {}

        # for char in ransomNote:
        #     if char in letterPairs:
        #         letterPairs[char] += 1
        #     else:
        #         letterPairs[char] = 1

        # for char in magazine:
        #     if char in letterPairs:
        #         letterPairs[char] -= 1
        
        # for letter in letterPairs:
        #     if letterPairs[letter] > 0:
        #         return False
        # return True
