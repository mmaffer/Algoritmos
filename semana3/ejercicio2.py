class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def list_length(self):
        """Cuenta y devuelve el número de nodos en la lista."""
        count = 0
        current = self.head
        
        while current is not None:
            count += 1
            current = current.next
        
        return count