# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque()
        q2 = deque()

        q1.append(p)
        q2.append(q)

        while q1 and q2:
            node_P, node_Q = q1.popleft(), q2.popleft()

            if not node_Q and not node_P:
                continue

            if not node_Q or not node_P or node_P.val != node_Q.val:
                return False

            q1.append(node_P.right)
            q1.append(node_P.left)
            q2.append(node_Q.right)
            q2.append(node_Q.left)

        return True