# beats 37% runtime and 30% memory
# O(n) time and O(n) space

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head#: Optional[ListNode]
                 ) -> int:#Optional[ListNode]
    
        if not head:
            return None

        stack = []
        putBackStack = []

        cur = head
        while (cur):
            stack.append(cur.val)
            cur = cur.next
        
        counter = 0

        while stack:
            digit = stack.pop() * 2 + counter
            counter = digit // 10
            putBackStack.append(digit % 10)
        if counter:
            putBackStack.append(counter)
        
        dummy = ListNode(0)
        last = dummy

        while putBackStack:
            new_node = ListNode(putBackStack.pop())
            last.next = new_node
            last = new_node
        
        return dummy.next