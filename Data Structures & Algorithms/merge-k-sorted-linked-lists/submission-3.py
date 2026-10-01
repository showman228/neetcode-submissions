# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        sp = []
        for lst in lists:
            while lst:
                sp.append(lst.val)
                lst = lst.next

        dummy = ListNode()
        sp.sort()

        curr = dummy
        for val in sp:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next