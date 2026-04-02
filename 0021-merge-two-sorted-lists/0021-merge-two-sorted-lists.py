# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            newList = ListNode(min(list1.val,list2.val),None)
            if newList.val == list1.val:
                list1 = list1.next
            else:
                list2 = list2.next
        elif list1:
            newList = ListNode(list1.val,None)
            list1 = list1.next
        elif list2:
            newList = ListNode(list2.val,None)
            list2 = list2.next
        else:
            newList = None
            return None

        temp = newList
        while list1 or list2:
            if list1 and list2:
                t = min(list1.val,list2.val)
                if t == list1.val:
                    newNode = ListNode(t,None)
                    list1 = list1.next
                    newList.next = newNode
                    newList = newList.next
                else:
                    newNode = ListNode(t,None)
                    list2 = list2.next
                    newList.next = newNode
                    newList = newList.next
            elif list1:
                newNode = ListNode(list1.val,None)
                list1 = list1.next
                newList.next = newNode
                newList = newList.next
            elif list2 :
                newNode = ListNode(list2.val,None)
                list2 = list2.next
                newList.next = newNode
                newList = newList.next
        return temp


        