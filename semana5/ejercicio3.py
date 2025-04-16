import heapq
class PriorityQueue:
    """Priority queue implementation using a binary heap."""
    
    def __init__(self):
        self._heap = []
        self._count = 0  # To maintain insertion order on same priority

    def enqueue(self, item, priority):
        """
        Add an item with the given priority.
        Higher number means higher priority.
        """
        heapq.heappush(self._heap, (-priority, self._count, item))
        self._count += 1

    def dequeue(self):
        """
        Remove and return the item with the highest priority.
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return heapq.heappop(self._heap)[2]

    def peek(self):
        """
        Return the item with the highest priority without removing it.
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self._heap[0][2]

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self._heap) == 0

    def size(self):
        """Return the number of items in the priority queue."""
        return len(self._heap)

    def __str__(self):
        """Return a string representation of the queue."""
        return f"PriorityQueue: {[item[2] for item in sorted(self._heap)]}"


# Ejemplo de uso:
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("A", 2)
    pq.enqueue("B", 3)
    pq.enqueue("C", 1)
    pq.enqueue("D", 3)

    print("Elemento con mayor prioridad:", pq.peek())  # B
    print("Atendiendo:", pq.dequeue())  # B
    print("Atendiendo:", pq.dequeue())  # D
    print("Tamaño actual:", pq.size())  # 2
    print("¿Está vacía?:", pq.is_empty())  # False
    print("Cola actual:", pq)
