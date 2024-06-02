# beats 63% runtime and 88% memory
# O(n) time and O(n) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def hasPathSum(self, root#: Optional[TreeNode]
                   , targetSum#: int
                   ) -> bool:
        def dfs(node, nums_sum, target_sum):
            if not node:
                return False

            nums_sum += node.val
            if not node.left and not node.right:
                if nums_sum == targetSum:
                    return True

            return dfs(node.left, nums_sum, target_sum) or dfs(node.right, nums_sum, target_sum)

        return dfs(root, 0, targetSum)

