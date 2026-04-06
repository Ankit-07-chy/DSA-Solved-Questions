# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        slow = dummy
        fast = dummy
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        # slow.val = slow.next.val
        slow.next = slow.next.next
        return dummy.next
        

        '''
        brute force
        total_node = 0
        curr = head
        while curr:
            total_node += 1
            curr = curr.next
        delete_node = total_node -n
        temp = head
        if delete_node == 0:
            return head.next
        
        for i in range(delete_node-1):
            temp = temp.next
        temp.next = temp.next.next
        
        
        return head
        '''