"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visit = dict()

        def dfs(node):
            if node in visit:
                return visit[node]
            
            copy_graph = Node(node.val)
            visit[node] = copy_graph
            for ner in node.neighbors:
                copy_graph.neighbors.append(dfs(ner))
            return copy_graph

        return dfs(node) if node else None



