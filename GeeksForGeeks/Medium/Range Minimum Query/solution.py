def constructST(arr, n):
    segment_tree = [0]*(4*n)
    
    def buildTree(idx,left,right):
        if left == right:
            segment_tree[idx] = arr[left]
            return 
        mid = (left+right)//2
        buildTree(2*idx+1,left,mid)
        buildTree(2*idx+2,mid+1,right)
        segment_tree[idx] = min(segment_tree[2*idx+1],segment_tree[2*idx+2])
    buildTree(0,0,n-1)    
    return segment_tree


def RMQ(st, n, qs, qe):
    def query(start,end,idx,left,right):
        # outof bount case
        if left > end or right < start:
            return 10**9
        elif left >= start and right <= end:
            return st[idx]
        else:
            mid = (left+right)//2
            return min(query(start,end,2*idx+1,left,mid),query(start,end,2*idx+2,mid+1,right))
    return query(qs,qe,0,0,n-1)