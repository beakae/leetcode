# beats 19% runtime and 95% memory
# O(N) runtime and O(logN) memory

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root#: Optional[TreeNode]
                 ) -> int:
        if not root:
            return 0
        def bfs(node):
            if not node:
                return float('inf')
            if not node.left and not node.right:
                return 1
            return min(bfs(node.left), bfs(node.right)) + 1
        return bfs(root)