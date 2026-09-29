# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return

        sp = []
        while head:
            sp.append(head)
            head = head.next

        i, j = 0, len(sp) - 1
        res = []
        while i < j:
            sp[i].next = sp[j]
            i += 1

            if i == j:
                break
            
            sp[j].next = sp[i]
            j -= 1
        
        sp[i].next = None
        

            
        
