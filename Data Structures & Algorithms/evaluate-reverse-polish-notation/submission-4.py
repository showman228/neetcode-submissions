class DoubledLinkedList:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        head = DoubledLinkedList(tokens[0])
        curr = head

        for i in range(1, len(tokens)):
            curr.next = DoubledLinkedList(tokens[i], prev=curr)
            curr = curr.next

        while head is not None:
            if head.val in '+-*/':
                second = int(head.prev.val)
                first = int(head.prev.prev.val)

                if head.val == '+':
                    res = first + second
                elif head.val == '-':
                    res = first - second
                elif head.val == '*':
                    res = first * second
                elif head.val == '/':
                    res = int(first / second)

                head.val = str(res)
                head.prev = head.prev.prev.prev

                if head.prev is not None:
                    head.prev.next = head
            
            ans = int(head.val)
            head = head.next

        return ans
