#beat 97.5% and 84.5%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        def searchChildren(node, depth):
            if not node:
                return depth
            return max(searchChildren(node.left, depth + 1), searchChildren(node.right, depth + 1))
        return searchChildren(root, 0)
