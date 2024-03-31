#beat 95% and 96.5%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(q, p):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return (p.val == q.val) and isMirror(q.left, p.right) and isMirror(q.right, p.left)
        return isMirror(root, root)