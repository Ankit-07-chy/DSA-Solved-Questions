# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
        maxi = -inf
        temp = head
        while temp:
            maxi = max(maxi,temp.val+stack.pop())
            temp = temp.next
        return maxi