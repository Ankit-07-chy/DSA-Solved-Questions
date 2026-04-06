# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """ 
        Brute Force
        """
        freq = {}
        temp1,temp2 = headA, headB
        while temp1:
            freq[temp1] = 1
            temp1 = temp1.next
        while temp2:
            if temp2 in freq:
                return temp2
            freq[temp2]= 1
            temp2 = temp2.next