class MaxHeap:
    # Define MaxHeap class for max-heap data structure where parent >= children
    def __init__(self):
        # Constructor initializes an empty list to store heap elements
        self.heap = []

    def insert(self, value):
        # Method to insert a new value while maintaining max-heap property
        # First, append the new value to the end of the heap list
        self.heap.append(value)
        # Then, restore heap property by moving the new element up if needed
        # Pass the index of the newly inserted element (last index)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Private method to move a value up the heap to restore max-heap property
        # Continue while we haven't reached the root (index 0)
        while index > 0:
            # Calculate parent index using the heap formula: (child_index - 1) // 2
            parent_index = (index - 1) // 2
            # Check if current node is larger than its parent (violates max-heap)
            # Note: This is opposite of min-heap - we use > instead of <
            if self.heap[index] > self.heap[parent_index]:
                # Swap current node with its parent to fix the violation
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                # Move up to check the parent's position next
                index = parent_index
            else:
                # If heap property is satisfied, stop the process
                break

    def delete_max(self):
        # Method to remove and return the largest element (root) from the heap
        # Check if the heap is empty
        if len(self.heap) == 0:
            # Return None if there are no elements to delete
            return None
        
        # Check if there's only one element in the heap
        if len(self.heap) == 1:
            # Remove and return the single element using pop()
            return self.heap.pop()
        
        # Store the maximum value (root) to return later
        max_value = self.heap[0]
        # Move the last element to the root position
        self.heap[0] = self.heap.pop()
        # Restore heap property by moving the new root down if needed
        self._heapify_down(0)
        # Return the original maximum value
        return max_value

    def _heapify_down(self, index):
        # Private method to move a value down the heap to restore max-heap property
        # Continue until we reach a leaf node or heap property is satisfied
        while True:
            # Calculate indices of left and right children using heap formulas
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            # Assume current index has the largest value initially
            largest = index
            
            # Check if left child exists and is larger than current largest
            # Note: This is opposite of min-heap - we use > instead of <
            if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
                # Update largest to point to left child
                largest = left_child
            
            # Check if right child exists and is larger than current largest
            # Note: This is opposite of min-heap - we use > instead of <
            if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
                # Update largest to point to right child
                largest = right_child
            
            # If current node is already the largest, heap property is satisfied
            if largest == index:
                # Break the loop as no more swaps are needed
                break
            
            # Swap current node with the larger child to maintain max-heap property
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            # Move down to the position of the swapped child for next iteration
            index = largest

# Test function to verify MaxHeap functionality
def test_max_heap():
    h = MaxHeap()
    h.insert(1);         print("🦁 Test 1:", h.heap==[1])
    for v in [3,2,8,5]:
        h.insert(v)
    print("🦁 Test 2:", h.heap[0]==max(h.heap))
    h.delete_max();      print("🦁 Test 3:", h.heap[0]==max(h.heap))
    h = MaxHeap()
    for v in [5,3,1]:
        h.insert(v)
    h.delete_max();      print("🦁 Test 4:", h.heap==[3,1])
    h=MaxHeap(); h.insert(10)
    print("🦁 Test 5:", h.delete_max()==10 and h.heap==[])

test_max_heap()