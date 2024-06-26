# beats 98% runtime and 85% memory
# O(n) time and O(n) space
# O(logn) space best case

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root#: Optional[TreeNode]
                 ) -> int:        
        def searchChildren(node, depth):
            if not node:
                return depth
            return max(searchChildren(node.left, depth + 1), searchChildren(node.right, depth + 1))
        return searchChildren(root, 0)
