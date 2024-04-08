# time exceeded
# O(n^2) time and O(1) space

class Solution:
    def singleNumber(self, nums#: List[int]
                     ) -> int:
        if len(nums) == 1:
            return nums[0]

        counter = True

        for i in range(0, len(nums)):
            for j in range (0, len(nums)):
                if nums[i] == nums[j] and i != j:
                    counter = False
            if counter == True:
                return nums[i]
            counter = True
