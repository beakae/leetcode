# beats 60% runtime and 96% memory
# O(n) time and O(n) space

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letter_to_word_match = {}
        word_to_letter_match = {}
        array = s.split()

        if len(array) != len(pattern):
            return False

        for char, word in zip(pattern, array):
            if (char in letter_to_word_match and letter_to_word_match[char] != word) or \
                (word in word_to_letter_match and word_to_letter_match[word] != char):
                return False

            letter_to_word_match[char] = word
            word_to_letter_match[word] = char
        return True