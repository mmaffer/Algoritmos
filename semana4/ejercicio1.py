class Stack:
    """Simple Stack implementation using a list."""
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def size(self):
        return len(self.items)


def reverse_string(input_string):
    """Reverse a string using a stack."""
    stack = Stack()

    # Push all characters to the stack
    for char in input_string:
        stack.push(char)

    # Pop all characters to form the reversed string
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

# Test Cases
print(reverse_string("hello"))        
print(reverse_string("Stack"))        
print(reverse_string("123456789"))