class Solution:
    def querySum(self, n, arr, q, queries):
        # code here
        class SegmentTree:
            def __init__(self,n,arr):
                self.size = n
                self.arr = arr
                self.segment_tree = [0]*(4*self.size)
                self.buildTree(0,0,self.size-1) # (index, left,right)
            
            def buildTree(self,idx,left,right):
                if left == right:
                    self.segment_tree[idx] = self.arr[left]
                    return
                mid = (left+right)//2
                self.buildTree(2*idx+1,left,mid)
                self.buildTree(2*idx+2,mid+1,right)
                self.segment_tree[idx] = self.segment_tree[2*idx+1] + self.segment_tree[2*idx+2]
            
            def query(self,start,end,idx,left,right):
                # out of bound
                if start > right or end < left:
                    return 0
                # completely inside
                elif start<=left and right<=end:
                    return self.segment_tree[idx]
                else:
                    mid = (left+right)//2
                    return self.query(start,end,2*idx+1,left,mid)+self.query(start,end,2*idx+2,mid+1,right)
        
        seg = SegmentTree(n, arr)
        ans = []
        
        for i in range(0, 2 * q, 2):
            start = queries[i] - 1  # Convert to 0-indexed
            end = queries[i + 1] - 1  # Convert to 0-indexed
            ans.append(seg.query(start, end, 0, 0, n - 1))
        
        return ans
            
            