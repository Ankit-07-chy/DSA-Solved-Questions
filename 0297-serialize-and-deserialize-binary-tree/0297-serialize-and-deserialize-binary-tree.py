# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string = ''
        from collections import deque
        queue = deque([])
        queue.append(root)
        while queue:
            temp = queue.popleft()
            if temp:
                string += str(temp.val) + ','
                queue.append(temp.left)
                queue.append(temp.right)
            else:
                string += '#,'
        # print(string)
        return string
            

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data = data.split(',')
        if data[0] == '#':
            return None
        root = TreeNode(int(data[0]))
        temp = root
        i = 1
        queue = deque([]); queue.append(temp)
        j = 0
        while i < len(data) and queue:
            parent = queue.popleft()
            if data[i] == '#':
                parent.left = None
            if data[i+1] == '#':
                parent.right = None
            if data[i] != '#':
                node = TreeNode(int(data[i]))
                parent.left = node
                queue.append(node)
            if data[i+1] != '#':
                node = TreeNode(int(data[i+1]))
                parent.right = node 
                queue.append(node)
            i += 2
            j += 1
        return root


            
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))