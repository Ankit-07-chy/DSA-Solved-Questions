# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next
        if stack:
            res = stack.pop()
            stack.append(res)
        else:
            res = None
        while stack:
            curr = stack.pop()
            if stack:
                next_ = stack.pop()
                curr.next  = next_
                stack.append(next_)
            else:
                curr.next = None
        return res