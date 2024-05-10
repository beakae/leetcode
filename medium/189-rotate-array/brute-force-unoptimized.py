# beats 11% runtime and 69% memory
# O(k * n) time and O(1) space 

class Solution:
    def rotate(self, nums#: List[int]
               , k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, k):
            replacement = nums.pop()
            nums.insert(0, replacement)