from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node, currentSum):
            if not node:
                return 0

            currentSum += node.val

            count = prefix[currentSum - targetSum]

            prefix[currentSum] += 1

            count += dfs(node.left, currentSum)
            count += dfs(node.right, currentSum)

            prefix[currentSum] -= 1

            return count

        return dfs(root, 0)