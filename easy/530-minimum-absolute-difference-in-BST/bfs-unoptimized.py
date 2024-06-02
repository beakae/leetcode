# beats 5% runtime and 15% memory
# O(n^2) time and O(n) space

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
        seen_numbers = set()
        global_min = 0
        if root.left is None:
            next_node = root.right
            global_min = abs(root.val-next_node.val)
        else:
            next_node = root.left
            global_min = abs(root.val-next_node.val)

        queue = deque([])
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            
            for item in seen_numbers:
                global_min = min(global_min, abs(node.val - item))

            seen_numbers.add(node.val)
        return global_min
