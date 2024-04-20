# beats 86.4% runtime and 90% memory
# O(n+m) time and O(n) space 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(0)
        cur = head
        
        while l1 is not None or l2 is not None:
            if l1 is None:
                cur.next = ListNode((l2.val + carry) % 10)
                if l2.val + carry >= 10:
                    carry = 1
                else:
                    carry = 0
                l2 = l2.next
            elif l2 is None:
                cur.next = ListNode((l1.val + carry) % 10)
                if l1.val + carry >= 10:
                    carry = 1
                else:
                    carry = 0          
                l1 = l1.next
            else:
                cur.next = ListNode((l2.val + l1.val + carry) % 10)
                if (l2.val + l1.val + carry) >= 10:
                    carry = 1
                else:
                    carry = 0
                l1 = l1.next
                l2 = l2.next
            cur = cur.next
        if carry == 1:
            cur.next = ListNode(1)
        return head.next
