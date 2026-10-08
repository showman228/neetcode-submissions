# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count = 0
        max_node = float("-inf")

        q = deque()
        q.append(root)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                max_node = max(max_node, node.val)

                if max_node <= node.val:
                    count += 1
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return count