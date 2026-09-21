# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            return 1 + max(self.dfs(root.right), self.dfs(root.left))
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if abs(left - right) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

            

