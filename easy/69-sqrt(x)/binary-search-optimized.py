# beats 98% runtime and 42% memory
# O(logn) time and O(1) space

class Solution:
    def mySqrt(self, x#: int
               ) -> int:
        if x == 0:
            return 0
        first, last = 1, x
        
        while first <= last:
            mid = (first + last) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                last = mid - 1
            else:
                first = mid + 1
        return last