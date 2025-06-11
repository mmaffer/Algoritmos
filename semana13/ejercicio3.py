class MinHeap:
    # Define MinHeap class for min-heap data structure implementation
    def __init__(self):
        # Constructor initializes an empty list to store heap elements
        self.heap = []

    def delete_min(self):
        # Method to remove and return the smallest element (root) from the heap
        # Check if the heap is empty
        if len(self.heap) == 0:
            # Return None if there are no elements to delete
            return None
        
        # Check if there's only one element in the heap
        if len(self.heap) == 1:
            # Remove and return the single element using pop()
            return self.heap.pop()
        
        # Store the minimum value (root) to return later
        min_value = self.heap[0]
        # Move the last element to the root position
        self.heap[0] = self.heap.pop()
        # Restore heap property by moving the new root down if needed
        self._heapify_down(0)
        # Return the original minimum value
        return min_value

    def _heapify_down(self, index):
        # Private method to move a value down the heap to restore min-heap property
        # Continue until we reach a leaf node or heap property is satisfied
        while True:
            # Calculate indices of left and right children
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            # Assume current index has the smallest value initially
            smallest = index
            
            # Check if left child exists and is smaller than current smallest
            if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
                # Update smallest to point to left child
                smallest = left_child
            
            # Check if right child exists and is smaller than current smallest
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
                # Update smallest to point to right child
                smallest = right_child
            
            # If current node is already the smallest, heap property is satisfied
            if smallest == index:
                # Break the loop as no more swaps are needed
                break
            
            # Swap current node with the smaller child
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            # Move down to the position of the swapped child
            index = smallest

# Test function to verify delete_min and heapify_down functionality
def test_min_heap_delete_min():
    h = MinHeap()
    print("🧹 Test 1:", h.delete_min() is None)
    h.heap=[1]; print("🧹 Test 2:", h.delete_min()==1 and h.heap==[])
    h.heap=[1,3,2]; print("🧹 Test 3:", h.delete_min()==1 and h.heap==[2,3])
    h.heap=[1,3,4,5]; print("🧹 Test 4:", h.delete_min()==1 and h.heap==[3,5,4])
    h.heap=[1,2,3,4,5]
    print("🧹 Test 5:", h.delete_min()==1)

test_min_heap_delete_min()