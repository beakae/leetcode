# beats 93% runtime and 8% memory
# O(n) time and O(n) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head#
                 ) -> bool:
        visited_nodes = set()
        
        while head is not None:
            if head in visited_nodes:
                return True
            else:
                visited_nodes.add(head)
            head = head.next
        return False