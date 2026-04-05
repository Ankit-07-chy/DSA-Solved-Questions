# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 2
        """
        n = len(lists) # gives total no of list
        if n<=0:
            return None
        elif n == 1:
            return lists[0]
        else:
            result = lists[0]
            for i in range(1,n):
                result = self.mergeTwoLists(result,lists[i])
            return result
    def mergeTwoLists(self,l1,l2):
        dummy = ListNode(0)
        temp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return dummy.next

        
        '''
        Approach 1

        aj = []
        n = len(lists)
        for i in range(n):
            curr_list = lists[i]
            while curr_list:
                aj.append(curr_list.val)
                curr_list = curr_list.next
        aj.sort()
        m = len(aj)
        if m>0:
            head = ListNode(aj[0],None)
            temp = head
            for i in range(1,m):
                new_node = ListNode(aj[i],None)
                temp.next = new_node
                temp = temp.next
            return head
        else:
            return None
        '''
        