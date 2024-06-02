# 97% runtime and 81% memory
# honestly idk

class Solution:
    def isHappy(self, n#: int
                ) -> bool:
        def sum_nums(n: int) -> int:
            ans = 0
            while n > 0:
                last_digit = n % 10
                ans += last_digit * last_digit
                n //= 10
            return ans

        slow = fast = n
        
        while True:
            slow = sum_nums(slow)
            fast = sum_nums(fast)
            fast = sum_nums(fast)

            if slow == fast:
                break

        if slow == 1:
            return True
        return False

