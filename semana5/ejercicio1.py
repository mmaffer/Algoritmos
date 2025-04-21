class QueueUsingStacks:
    def __init__(self):
        self.stack_enqueue = []  # Stack for enqueue operations
        self.stack_dequeue = []  # Stack for dequeue operations

    def enqueue(self, value):
        self.stack_enqueue.append(value)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        self._transfer_if_needed()
        return self.stack_dequeue.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty queue")
        self._transfer_if_needed()
        return self.stack_dequeue[-1]

    def isEmpty(self):
        return not self.stack_enqueue and not self.stack_dequeue

    def size(self):
        return len(self.stack_enqueue) + len(self.stack_dequeue)

    def _transfer_if_needed(self):
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())


q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.peek())     # Output: 2
print(q.size())     # Output: 2
print(q.isEmpty())  # Output: False