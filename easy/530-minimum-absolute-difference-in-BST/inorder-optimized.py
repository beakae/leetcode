# beats 73% runtime and 90% memory
# O(n) space and O(n) time

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getMinimumDifference(self, root#: Optional[TreeNode]
                             ) -> int:
        array = []

        def inOrderTraversal(node, array):
            if node is None:
                return
            
            inOrderTraversal(node.left, array)
            array.append(node.val)
            inOrderTraversal(node.right, array)

        inOrderTraversal(root, array)
        global_min = array[1] - array[0]
        for i in range(2, len(array)):
            global_min = min(global_min, array[i] - array[i-1])
        return global_min