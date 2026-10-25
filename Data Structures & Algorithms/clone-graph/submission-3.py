"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        visit = dict()
        q = deque()
        q.append(node)
        visit[node] = Node(node.val)

        while q:
            current = q.popleft()

            for ner in current.neighbors:
                if ner not in visit:
                    visit[ner] = Node(ner.val)
                    q.append(ner)
                visit[current].neighbors.append(visit[ner])
        
        return visit[node]

