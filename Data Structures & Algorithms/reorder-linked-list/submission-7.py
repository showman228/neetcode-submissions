# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        sp = []
        cur = head
        while cur:
            sp.append(cur)
            cur = cur.next

        i, j = 0, len(sp) - 1
        while i < j:
            sp[i].next = sp[j]
            i += 1

            if i >= j:
                break
            
            sp[j].next = sp[i]
            j -= 1
        
        sp[i].next = None
            
        
