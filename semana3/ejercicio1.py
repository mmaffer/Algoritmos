class Node:
    """Node in a linked list, stores data and reference to the next node."""
    
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
    
    def get_next(self):
        return self.next
    
    def set_next(self, next_node):
        self.next = next_node


class LinkedList:
    """Singly linked list implementation."""
    
    def __init__(self):
        self.head = None
        self.length = 0

    def display(self):
        if self.head is None:
            return "Empty list"
        
        current = self.head
        result = ""
        
        while current is not None:
            result += str(current.get_data()) + " -> "
            current = current.get_next()
        
        return result + "None"


# --- 🔽 TEST CASES ---

# 🔹 Case 1: Empty list
ll1 = LinkedList()
print("Case 1 (empty list):", ll1.display())  # Expected: Empty list

# 🔹 Case 2: One node
ll2 = LinkedList()
n1 = Node(100)
ll2.head = n1
print("Case 2 (one node):", ll2.display())  # Expected: 100 -> None

# 🔹 Case 3: Three nodes
ll3 = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
ll3.head = n1
n1.set_next(n2)
n2.set_next(n3)
print("Case 3 (three nodes):", ll3.display())  # Expected: 1 -> 2 -> 3 -> None
