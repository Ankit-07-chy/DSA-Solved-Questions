# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        Optimal
        '''
        pt1 = headA; pt2 = headB
        while pt1 != pt2:
            pt1 = pt1.next if pt1 else headB
            pt2 = pt2.next if pt2 else headA
        return pt1

        """ 
        Brute Force

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
        """
        