# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        prev_tail = dummy = ListNode(0, head)

        while True:
            kth = prev_tail
            for _ in range(k):
                kth = kth.next
                if kth == None:
                    return dummy.next

            group_head = prev_tail.next
            next_group = kth.next

            prev, cur = next_group, group_head
            while cur != next_group:
                temp = cur.next 
                cur.next = prev
                prev = cur
                cur = temp

            prev_tail.next = kth
            prev_tail = group_head



            