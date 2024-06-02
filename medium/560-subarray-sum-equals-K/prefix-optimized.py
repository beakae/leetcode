# beats 95% runtime and 75% memory
# O(n) time and O(n) space

class Solution:
    def subarraySum(self, nums#: List[int]
                    , k#: int
                    ) -> int:
        sums_prefix = {}
        sums_prefix[0] = 1
        sums = 0
        total_count = 0

        for num in nums:
            sums += num
            if sums-k in sums_prefix:
                total_count += sums_prefix[sums-k]
            
            if sums in sums_prefix:
                sums_prefix[sums] += 1
            else:
                sums_prefix[sums] = 1
        return total_count

        