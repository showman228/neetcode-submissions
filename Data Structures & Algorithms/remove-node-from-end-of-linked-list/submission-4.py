# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        idx = len(nodes) - n

        if idx == 0:
            return head.next

        nodes[idx - 1].next = nodes[idx].next

        return head
