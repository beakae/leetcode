# beats 53% runtime and 99% memory
# O(n) time and O(n) space

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges = []
        first = nums[0]
        second = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                second = nums[i]
            else:
                if first == second:
                    ranges.append(f"{first}")
                else:
                    ranges.append(f"{first}->{second}")
                first = nums[i]
                second = nums[i]
        if first == second:
            ranges.append(f"{first}")
        else:
            ranges.append(f"{first}->{second}")
        return ranges