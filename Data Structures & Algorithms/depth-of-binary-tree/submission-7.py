# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append([root, 1])
        res = 0

        while q:
            node, height = q.popleft()
            if node:
                res = max(res, height)
                if node.left:
                    q.append([node.left, height + 1])
                if node.right:
                    q.append([node.right, height + 1])
        
        return res


                   
