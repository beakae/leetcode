# beats 90% runtime and 78% memory
# O(n) time and O(1) space

class Solution:
    def majorityElement(self, nums#: List[int]
                        ) -> int:
        ans = nums[0]
        counter = 1

        for i in range(1, len(nums)):
            if nums[i] != ans:
                counter -= 1
                if counter == 0:
                    ans = nums[i]
                    counter = 1
            else:
                counter += 1
        return ans