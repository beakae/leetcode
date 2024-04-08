# beats 98% runtime and 95% memory
# O(n) time and O(1)) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head#: Optional[ListNode]
                 ) -> bool:
        fast_pointer = head
        slow_pointer = head

        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            if fast_pointer == slow_pointer:
                return True
        return False