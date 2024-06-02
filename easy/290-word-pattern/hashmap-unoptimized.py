# beats 52% runtime and 96% memory
# O(n) time and O(n) space

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letter_to_word_match = {}
        word_to_letter_match = {}
        array = s.split()

        if len(array) != len(pattern):
            return False

        index = 0

        for char in pattern:
            if (char in letter_to_word_match and letter_to_word_match[char] != array[index]) or \
                (array[index] in word_to_letter_match and word_to_letter_match[array[index]] != char):
                return False

            letter_to_word_match[char] = array[index]
            word_to_letter_match[array[index]] = char
            index += 1
        return True
        