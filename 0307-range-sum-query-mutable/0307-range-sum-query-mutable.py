class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.segmentTree = [0]*(4*self.n)
        self.buildTree(0,0,self.n-1,nums)

    def buildTree(self,idx,left,right,nums):
        if left == right:
            self.segmentTree[idx] = nums[left]
            return 

        mid = (left+right)//2
        self.buildTree(2*idx + 1, left,mid,nums)
        self.buildTree(2*idx+2,mid+1,right,nums) 
        self.segmentTree[idx] = self.segmentTree[2*idx+1] + self.segmentTree[2*idx+2]      

    def update(self, index: int, val: int) -> None:

        def updateSegmentTree(index,val,i,left,right):
            if left == right:
                self.segmentTree[i] = val
                return 
            mid = (left+right)//2
            if index <= mid:
                updateSegmentTree(index,val,2*i+1,left,mid)
            else:
                updateSegmentTree(index,val,2*i+2,mid+1,right)
            
            self.segmentTree[i] = self.segmentTree[2*i+1]+ self.segmentTree[2*i+2]
        updateSegmentTree(index,val,0,0,self.n-1)

        

    def sumRange(self, left: int, right: int) -> int:
        start = left; end = right
        l = 0; r = self.n-1

        def query(start,end,i,l,r):
            if l>end or r <start:
                return 0
            elif (l>=start and r<=end):
                return self.segmentTree[i]
            else:
                mid = (l+r)//2
                return query(start,end,2*i+1,l,mid)+query(start,end,2*i+2,mid+1,r)
        return query(start,end,0,0,self.n-1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)