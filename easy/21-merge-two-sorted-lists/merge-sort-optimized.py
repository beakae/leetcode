# beats 97% runtime and 58% memory
# O(n + m) time and O(n + 1) space 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1#: Optional[ListNode]
                      , list2#: Optional[ListNode]
                        #Optional 
                        )->int:
        if list2 is None:
            return list1
        if list1 is None:
            return list2

        head = ListNode(0)
        curr = head
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 if list1 is not None else list2


        return head.next