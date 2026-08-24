''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def minTime(self, root, target):
        # code here
        parent = {}
        target_node = None
        
        def find_parent(root):
            nonlocal target_node
            parent[root] = -1
            from collections import deque 
            queue = deque([])
            queue.append(root)
            while queue:
                temp = queue.popleft()
                if temp.data == target:
                    target_node = temp
                if temp.left:
                    parent[temp.left] = temp
                    queue.append(temp.left)
                if temp.right:
                    parent[temp.right] = temp
                    queue.append(temp.right)
            
        find_parent(root)
        from collections import deque
        queue = deque([])
        visited = set()
        visited.add(target_node)
        queue.append([target_node,0])
        time = 0
        while queue:
            node,time = queue.popleft()
            if node == None :
                continue
            for neig in (node.left,node.right,parent.get(node)):
                if neig == -1:
                    continue
                if neig == None or neig in visited:
                    continue
                queue.append([neig,time+1])
                visited.add(neig)
                
        return time