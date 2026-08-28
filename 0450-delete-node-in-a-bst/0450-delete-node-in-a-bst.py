class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return None

        # Find the node and its parent
        temp = root
        parent = None

        while temp and temp.val != key:
            parent = temp

            if key < temp.val:
                temp = temp.left
            else:
                temp = temp.right

        # Node not found
        if temp is None:
            return root

        # Case 1: node has no right subtree
        # Replace node with its left subtree
        if temp.right is None:
            new_child = temp.left

        # Case 2: node has right subtree
        else:
            new_child = temp.right

            # Find leftmost node in right subtree
            successor = temp.right

            while successor.left:
                successor = successor.left

            # Attach temp's left subtree
            successor.left = temp.left

        # If deleting root
        if parent is None:
            return new_child

        # Connect parent to new subtree
        if parent.left == temp:
            parent.left = new_child
        else:
            parent.right = new_child

        return root