class MinHeapWithSizeK:
    def __init__(self,capacity):
        self.minHeap = []
        self.capacity = capacity
        
    def __left(self,idx):
        return 2*idx + 1
    def __right(self,idx):
        return 2*idx + 2
    def __parent(self,idx):
        return (idx-1)//2 
    def __swap(self,i,j):
        self.minHeap[i],self.minHeap[j] = self.minHeap[j],self.minHeap[i]
        
    def __heapifyUp(self,idx):
        while idx > 0:
            parent = self.__parent(idx)
            if self.minHeap[parent] <= self.minHeap[idx]:
                break
            self.__swap(idx, parent)
            idx = parent
    def __heapifyDown(self,idx):
        n = len(self.minHeap)
        while True:
            smallest = idx
            left = self.__left(idx)
            right = self.__right(idx)
            
            if left < n and self.minHeap[left] < self.minHeap[smallest]:
                smallest = left 
            if right < n and self.minHeap[right]<self.minHeap[smallest]:
                smallest = right
                
            if smallest != idx:
                self.__swap(idx,smallest)
                idx = smallest
            else:
                break 
    
    def push(self,x):
        if len(self.minHeap) < self.capacity:
            self.minHeap.append(x)
            self.__heapifyUp(len(self.minHeap)-1)
        else:
            if x > self.minHeap[0]:
                self.minHeap[0] = x
                self.__heapifyDown(0)
                
    


class Solution:
    def kthLargest(self, arr, k):
        # code here
        minheap = MinHeapWithSizeK(k)
        for i in range(len(arr)):
            minheap.push(arr[i])
            
        return minheap.minHeap[0]
        
        
        