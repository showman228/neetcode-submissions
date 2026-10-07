# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.pop()

            if node.left and node.right:
                left = node.left
                right = node.right

                if (left.val == p.val and right.val == q.val) or (left.val == q.val and right.val == p.val):
                    return node
                
                if ((node.val == p.val or node.val == q.val) and (left.val == p.val or left.val == q.val)) or ((node.val == p.val or node.val == q.val) and (right.val == p.val or right.val == q.val)):
                    return node
            
                queue.append(left)
                queue.append(right)
        
        return root
        
