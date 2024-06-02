# beats 77% runtime and 95% memory
# O(n^2) time and O(1) space

class Solution:
    def countStudents(self, students#: List[int]
                      , sandwiches#: List[int]
                      ) -> int:
        count = 0
        while count < len(students):
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                count = 0
            else:
                students.append(students[0])
                count += 1
            students.pop(0)
        return len(students)