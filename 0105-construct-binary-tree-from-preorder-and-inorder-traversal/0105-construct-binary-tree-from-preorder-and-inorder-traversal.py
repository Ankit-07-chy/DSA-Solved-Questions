class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inMap = {}

        for i, v in enumerate(inorder):
            inMap[v] = i

        def build(lPre, rPre, lin, rin):

            if lPre > rPre or lin > rin:
                return None

            root_val = preorder[lPre]
            root = TreeNode(root_val)

            idx_in = inMap[root_val]

            left_size = idx_in - lin

            root.left = build(
                lPre + 1,
                lPre + left_size,
                lin,
                idx_in - 1
            )

            root.right = build(
                lPre + left_size + 1,
                rPre,
                idx_in + 1,
                rin
            )

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)