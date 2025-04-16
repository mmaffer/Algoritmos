class MyCircularDeque:


    def __init__(self, k: int):
        self.capacity = k
        self.deque = [None] * k
        self.front = 0
        self.rear = 0
        self.size = 0


    #insertFront
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.capacity
        self.deque[self.front] = value
        self.size += 1
        return True


    #insertLast
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True


    #deleteFront
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True


    #deleteLast
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        return True


    #getFront
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]


    #getRear
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1) % self.capacity]


    #isEmpty
    def isEmpty(self) -> bool:
        return self.size == 0


    #isFull
    def isFull(self) -> bool:
        return self.size == self.capacity
   
deque = MyCircularDeque(3)
print(deque.insertLast(1))   # True
print(deque.insertLast(2))   # True
print(deque.insertFront(3))  # True
print(deque.insertFront(4))  # False, está lleno
print(deque.getRear())       # 2
print(deque.isFull())        # True
print(deque.deleteLast())    # True
print(deque.insertFront(4))  # True
print(deque.getFront())      # 4


