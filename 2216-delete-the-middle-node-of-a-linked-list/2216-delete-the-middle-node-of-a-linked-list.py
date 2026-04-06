# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        slow = dummy; fast = dummy
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return dummy.next

"""
This code is giving issue in case my slow becomes the Lastnode
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        slow = dummy; fast = dummy
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
        if slow.next:
            slow.val = slow.next.val
            slow.next = slow.next.next
        else:
            slow.val = None
        return dummy.next

        """