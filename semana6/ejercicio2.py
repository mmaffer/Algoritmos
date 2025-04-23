class DynamicCircularQueue:
    def __init__(self, initial_capacity=5):
        self.capacity = initial_capacity
        self.queue = [None] * self.capacity
        self.front = -1
        self.rear = -1
        self.size_count = 0

    def is_empty(self):
        return self.size_count == 0

    def is_full(self):
        return self.size_count == self.capacity

    def enqueue(self, item):
        if self.is_full():
            self._resize()
        
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        
        self.queue[self.rear] = item
        self.size_count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        item = self.queue[self.front]
        self.queue[self.front] = None
        
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        
        self.size_count -= 1
        return item

    def _resize(self):
        new_capacity = self.capacity * 2
        new_queue = [None] * new_capacity
        index = self.front

        for i in range(self.size_count):
            new_queue[i] = self.queue[index]
            index = (index + 1) % self.capacity
        
        self.queue = new_queue
        self.capacity = new_capacity
        self.front = 0
        self.rear = self.size_count - 1


def rotate_array(arr, k):
    n = len(arr)
    if n == 0:
        return arr

    k = k % n  # Normalize
    queue = DynamicCircularQueue(n)

    for item in arr:
        queue.enqueue(item)

    # Rotate right by dequeuing and re-enqueuing n - k times
    for _ in range(n - k):
        queue.enqueue(queue.dequeue())

    rotated = []
    while not queue.is_empty():
        rotated.append(queue.dequeue())
    
    return rotated


# Caso 1: k mayor que el tamaño del arreglo
print(rotate_array([1, 2, 3], 5))
#  [2, 3, 1] (k=5 % 3 = 2, rotación a la derecha 2 pasos)

# Caso 2: Arreglo con valores repetidos
print(rotate_array([1, 2, 2, 3, 3, 4], 4))
#  [2, 3, 3, 4, 1, 2]

# Caso 3: Arreglo de caracteres
print(rotate_array(['a', 'b', 'c', 'd'], 2))
#  ['c', 'd', 'a', 'b']