class minHeap:
    
    def __init__(self):
        # Initialize the internal array to store the heap elements
        self.heap = []
        
    # --- Internal Helper Methods ---
    
    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left_child(self, i: int) -> int:
        return 2 * i + 1

    def _right_child(self, i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, i: int):
        """Moves an element up the tree to restore the min-heap property after insertion."""
        while i > 0 and self.heap[self._parent(i)] > self.heap[i]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _sift_down(self, i: int):
        """Moves an element down the tree to restore the min-heap property after extraction."""
        n = len(self.heap)
        while True:
            smallest = i
            l = self._left_child(i)
            r = self._right_child(i)
            
            # Check if left child exists and is smaller than current smallest
            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
                
            # Check if right child exists and is smaller than current smallest
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r
                
            # If the smallest is not the current node, swap and continue sifting down
            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    # --- Public API Methods ---

    # Insert x into the heap
    def push(self, x: int):
        # 1. Add to the very end to maintain the Complete Binary Tree shape
        self.heap.append(x)
        # 2. Bubble up to maintain the Min-Heap property
        self._sift_up(len(self.heap) - 1)

    # Remove the top (minimum) element
    def pop(self):
        if not self.heap:
            return -1  # Return -1 if empty (consistent with peek)
        
        # If only one element, just pop and return it
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # 1. Store the minimum value (root)
        min_val = self.heap[0]
        
        # 2. Move the last element to the root to maintain tree shape
        self.heap[0] = self.heap.pop()
        
        # 3. Bubble down to restore the Min-Heap property
        self._sift_down(0)
        
        return min_val

    # Return the top element or -1 if empty
    def peek(self) -> int:
        if not self.heap:
            return -1
        return self.heap[0]

    # Return the number of elements in the heap
    def size(self) -> int:
        return len(self.heap)
