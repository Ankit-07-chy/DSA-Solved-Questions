# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# using recursion -> it will take recursion stack space too
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node):
            if node == None or node.next == None:
                return node
            t = rev(node.next)
            front = node.next
            front.next = node
            node.next = None
            return t
            
        return rev(head)


"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev1 = None; curr = head
        if not head:
            return 
        while curr.next != None:
            temp = curr
            curr = curr.next
            temp.next = prev1
            prev1 = temp
        curr.next = prev1
        return curr



# Brute Force
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next
        if stack:
            res = stack.pop()
            stack.append(res)
        else:
            res = None
        while stack:
            curr = stack.pop()
            if stack:
                next_ = stack.pop()
                curr.next  = next_
                stack.append(next_)
            else:
                curr.next = None
        return res'''
        """