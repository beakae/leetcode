# 99% runtime and 96% space
# O(n + m) time and O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeOne = headA
        nodeTwo = headB

        while nodeOne is not nodeTwo:
            if nodeOne is None:
                nodeOne = headB
            else:
                nodeOne = nodeOne.next
            if nodeTwo is None:
                nodeTwo = headA
            else:
                nodeTwo = nodeTwo.next
        return nodeOne