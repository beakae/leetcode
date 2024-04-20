# 97% runtime and 6% memory
# O(n + m) time and O(n) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA#: ListNode
                            , headB#: ListNode
                            # -> Optional[ListNode]
                            ):   
        seenNodes = set()

        while headA:
            seenNodes.add(headA)
            headA = headA.next

        while headB:
            if headB in seenNodes:
                return headB
            headB = headB.next
            
        return None