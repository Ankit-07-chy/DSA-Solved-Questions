#Function to update a value in input array and segment tree.



def getSum(st, n, l, r):
    '''
    st: segment tree
    n:  len of given arr
    l:  left index
    r:  right index
    
    return: sum in range l and r
    '''
    #code here
    start = l; end = r; left = 0; right = n-1
    def querySum(start,end,idx,left,right):
        # out of bound case
        if left > end or right < start:
            return 0
        # complete inside
        elif left>=start and end>=right:
            return st[idx]
        else:
            mid = (left+right)//2
            return querySum(start,end,2*idx+1,left,mid)+querySum(start,end,2*idx+2,mid+1,right)
    return querySum(start,end,0,0,n-1)

#Function to return sum of elements in range from index
#qs (query start) to qe (query end).
def updateValue(arr, st, n, i, new_val):
    '''
    arr: given array
    st: segment tree
    n:  len of given arr
    i:  index of which value to be updated
    new_val:  value to replace
    
    '''
    #code here
    def update(idx,val,left,right):
        mid = (left+right)//2
        if left == right:
            st[idx] = val
            return 
        if i <= mid:
            update(2*idx+1,val,left,mid)
        else:
            update(2*idx+2,val,mid+1,right)
        st[idx] = st[2*idx+1]+st[2*idx+2]
    update(0,new_val,0,n-1)
