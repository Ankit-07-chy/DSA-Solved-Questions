# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        '''
        Approach 1
        '''
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