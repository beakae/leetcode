# beats 64% runtime and 62% memory
# O(nlogn) time and O(1) space (nlogn because of sort)

class Solution:
    def maximumHappinessSum(self, happiness#: List[int]
                            , k: int) -> int:
        happiness.sort()
        dec = 0
        ans = 0

        for i in range(0, k):
            ans += max(happiness[-1 - i] - dec, 0)
            dec += 1

        return ans