class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        idxMap = {}

        for i, val in enumerate(inorder):
            idxMap[val] = i

        def buildTreeFull(inorder, lin, rin, postorder, lpost, rpost, idxMap):

            if lin > rin or lpost > rpost:
                return None

            root = TreeNode(postorder[rpost])

            inorder_idx = idxMap[postorder[rpost]]

            # Number of nodes in right subtree
            right_size = rin - inorder_idx

            # Right subtree
            right = buildTreeFull(
                inorder,
                inorder_idx + 1,
                rin,
                postorder,
                rpost - right_size,
                rpost - 1,
                idxMap
            )

            # Left subtree
            left = buildTreeFull(
                inorder,
                lin,
                inorder_idx - 1,
                postorder,
                lpost,
                rpost - right_size - 1,
                idxMap
            )

            root.left = left
            root.right = right

            return root

        return buildTreeFull(
            inorder,
            0,
            len(inorder) - 1,
            postorder,
            0,
            len(postorder) - 1,
            idxMap
        )