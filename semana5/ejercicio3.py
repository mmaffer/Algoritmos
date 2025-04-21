# Exercise 3: Hot potato game
import random

class SimpleQueue:
    """Simple queue implementation using a Python list."""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


def hot_potato_game(players, max_passes):
    """
    Simulate the Hot Potato game using a queue with emoji-style output.
    """
    queue = SimpleQueue()
    
    for player in players:
        queue.enqueue(player)

    while queue.size() > 1:
        passes = random.randint(1, max_passes)
        print(f"\n🎲 Ronda: {passes} {'pase' if passes == 1 else 'pases'}")

        for _ in range(passes):
            passed = queue.dequeue()
            queue.enqueue(passed)
            print(f"📦 Pasó a {queue.peek()}")

        eliminated = queue.dequeue()
        print(f"💥 Eliminado: {eliminated}")

    winner = queue.dequeue()
    print(f"\n🏆 Ganador: {winner}")
    return winner

# Test Case 1
players1 = ["Alice", "Bob", "Charlie"]
winner1 = hot_potato_game(players1, 3)
print("Winner (Test 1):", winner1)

# Test Case 2
players2 = ["Anna", "Ben", "Cathy", "Dan", "Ella"]
winner2 = hot_potato_game(players2, 5)
print("Winner (Test 2):", winner2)

# Test Case 3
players3 = ["Tom", "Jerry"]
winner3 = hot_potato_game(players3, 1)
print("Winner (Test 3):", winner3)
