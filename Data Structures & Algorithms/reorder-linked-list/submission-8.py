# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # найти середину
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # перевернуть вторую половину
        cur = slow.next
        node = slow.next = None
        while cur:
            temp = cur.next
            cur.next = node
            node = cur
            cur = temp
        
        # соединить

        l1 = head
        l2 = node
        while l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2

            
        
