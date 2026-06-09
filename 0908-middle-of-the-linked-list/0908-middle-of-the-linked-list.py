# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# can use as len also, but that takes complexity O(n+n/2), in this case it use complexity o(N/2)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        slow = head
        fast = head
        while fast:
            if fast.next == None:
                return slow
            slow = slow.next
            fast = fast.next.next
        return slow
