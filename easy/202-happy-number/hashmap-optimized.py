# 71% runtime and 81% memory
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

        seen_nums = set()
        while True:
            squares_sum = sum_nums(n)

            if squares_sum == 1:
                return True
            
            if squares_sum in seen_nums:
                return False
            seen_nums.add(squares_sum)

            n = squares_sum
