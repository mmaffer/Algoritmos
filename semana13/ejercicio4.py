class MinHeap:
    # Define MinHeap class for min-heap data structure implementation
    def __init__(self):
        # Constructor initializes an empty list to store heap elements
        self.heap = []

    def build_heap(self, array):
        # Method to transform any unordered array into a valid min-heap in O(n) time
        # Create a copy of the input array to avoid modifying the original
        self.heap = array.copy()
        
        # Start from the last non-leaf node and work backwards to root
        # Last non-leaf node is at index (length // 2) - 1
        # This is because in a complete binary tree, nodes after this index are leaves
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            # Apply heapify_down to each non-leaf node to restore heap property
            self._heapify_down(i)

    def _heapify_down(self, index):
        # Private method to move a value down the heap to restore min-heap property
        # Continue until we reach a leaf node or heap property is satisfied
        while True:
            # Calculate indices of left and right children using heap formulas
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
            
            # Swap current node with the smaller child to maintain min-heap property
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            # Move down to the position of the swapped child for next iteration
            index = smallest

# Test function to verify build_heap functionality
def test_build_heap():
    h = MinHeap()
    h.build_heap([5,3,8,1,2]); print("🔨 Test 1:", h.heap[0]==1)
    h.build_heap([7,6,5,4,3,2,1]); print("🔨 Test 2:", h.heap[0]==1)
    h.build_heap([2,1]);           print("🔨 Test 3:", h.heap==[1,2])
    h.build_heap([10]);            print("🔨 Test 4:", h.heap==[10])
    h.build_heap([]);              print("🔨 Test 5:", h.heap==[])

test_build_heap()