class MinHeap:
    # Define MinHeap class for min-heap data structure implementation
    def __init__(self):
        # Constructor initializes an empty list to store heap elements
        self.heap = []

    def insert(self, value):
        # Method to insert a new value while maintaining min-heap property
        # First, append the new value to the end of the heap list
        self.heap.append(value)
        # Then, restore heap property by moving the new element up if needed
        # Pass the index of the newly inserted element (last index)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Private method to move a value up the heap to restore min-heap property
        # Continue while we haven't reached the root (index 0)
        while index > 0:
            # Calculate parent index using the heap formula: (child_index - 1) // 2
            parent_index = (index - 1) // 2
            # Check if current node is smaller than its parent (violates min-heap)
            if self.heap[index] < self.heap[parent_index]:
                # Swap current node with its parent to fix the violation
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                # Move up to check the parent's position next
                index = parent_index
            else:
                # If heap property is satisfied, stop the process
                break

# 🧪 Test cases
def test_min_heap_insert():
    h = MinHeap()
    h.insert(5); print("🍀 Test 1:", h.heap == [5])
    h.insert(3); print("🍀 Test 2:", h.heap == [3,5])
    h.insert(4); print("🍀 Test 3:", h.heap == [3,5,4])
    h.insert(1); print("🍀 Test 4:", h.heap == [1,3,4,5])
    # 🍀 Test 5: parent ≤ children
    valid = all(
        (h.heap[i] <= h.heap[2*i+1] if 2*i+1 < len(h.heap) else True)
        and (h.heap[i] <= h.heap[2*i+2] if 2*i+2 < len(h.heap) else True)
        for i in range(len(h.heap))
    )
    print("🍀 Test 5:", valid)

test_min_heap_insert()