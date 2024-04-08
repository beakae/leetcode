# beats 62% runtime and 8% memory
# O(n) time and O(n) space
# O(n/2) space

class Solution:
    def singleNumber(self, nums#: List[int]
                     ) -> int:
        if len(nums) == 1:
            return nums[0]

        seenNumbers = set()

        for num in nums:
            if num not in seenNumbers:
                seenNumbers.add(num)
            else:
                seenNumbers.remove(num)
        return list(seenNumbers)[0]