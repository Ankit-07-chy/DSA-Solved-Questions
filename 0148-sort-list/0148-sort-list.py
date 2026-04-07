# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Brute Force Approach
        """
        num = []
        temp = head
        while temp:
            num.append(temp.val)
            temp = temp.next
        num.sort()
        temp = head
        curr = 0
        while temp:
            temp.val = num[curr]
            curr+= 1
            temp = temp.next
        return head
            