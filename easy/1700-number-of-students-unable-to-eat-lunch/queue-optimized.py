# beats 93% runtime and 56% memory
# O(n) time and O(1) space

class Solution:
    def countStudents(self, students#: List[int]
                      , sandwiches#: List[int]
                      ) -> int:
        binary = [0,0]
        for student in students:
            binary[student] += 1
        count = 0

        while count < len(sandwiches):
            if binary[sandwiches[count]] > 0:
                binary[sandwiches[count]] -= 1
            else:
                break
            count += 1
        return len(sandwiches) - count