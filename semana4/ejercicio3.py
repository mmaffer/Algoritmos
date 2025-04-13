class MinStack:
    """Stack that supports retrieving the minimum element in O(1) time."""

    def _init_(self):
        self.stack = []      
        self.min_stack = []  

    def push(self, x):
        self.stack.append(x)
     
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.stack:
            raise IndexError("Pop from empty stack")
        value = self.stack.pop()
  
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def top(self):
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            raise IndexError("Stack is empty")
        return self.min_stack[-1]



stack = MinStack()
stack.push(3)
stack.push(5)
print("Min:", stack.getMin())  
stack.push(2)
stack.push(1)
print("Min:", stack.getMin()) 
stack.pop()
print("Min:", stack.getMin())  
stack.pop()
print("Top:", stack.top())     
print("Min:", stack.getMin())
