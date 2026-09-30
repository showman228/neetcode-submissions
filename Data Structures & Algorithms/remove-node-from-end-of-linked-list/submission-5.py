# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        idx_to_remove = len(nodes) - n
        if idx_to_remove == 0:
            return head.next

        nodes[idx_to_remove - 1].next = nodes[idx_to_remove].next
        return head
        



        