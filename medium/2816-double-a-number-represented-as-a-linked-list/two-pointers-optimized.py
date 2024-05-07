# beats 99% runtime and 99% memory
# O(n) time and O(1) space

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head#: Optional[ListNode]
                 ) -> int:#Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            doubled_val = cur.val * 2

            if doubled_val < 10:
                cur.val = doubled_val
            elif prev:
                cur.val = doubled_val % 10
                prev.val += 1
            else:
                head = ListNode(1, cur)
                cur.val = doubled_val % 10
            prev = cur
            cur = cur.next
        return head

        return head

            