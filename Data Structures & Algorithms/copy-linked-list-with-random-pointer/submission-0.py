"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.old_val_map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        if head in self.old_val_map:
            return self.old_val_map[head]
            
        copy = Node(head.val)
        self.old_val_map[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.old_val_map.get(head.random)
        return copy