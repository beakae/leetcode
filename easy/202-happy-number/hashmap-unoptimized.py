# beats 97% runtime and 81% memory
# honestly idk

class Solution:
    def isHappy(self, n#: int
                ) -> bool:
        seen_nums = set()

        while True:
            squares_sum = 0
            num_list = list(map(int, str(n)))
            for num in num_list:
                squares_sum += num * num

            if squares_sum == 1:
                return True
            
            if squares_sum in seen_nums:
                return False
            seen_nums.add(squares_sum)

            n = squares_sum
