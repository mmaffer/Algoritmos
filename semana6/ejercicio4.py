class CircularQueueMax:
    def __init__(self, size):
        self.size = size
        self.queue = [0] * size  # Stores indices
        self.start = 0
        self.end = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def add_end(self, value):
        if not self.is_full():
            self.queue[self.end] = value
            self.end = (self.end + 1) % self.size
            self.count += 1

    def remove_start(self):
        if not self.is_empty():
            value = self.queue[self.start]
            self.start = (self.start + 1) % self.size
            self.count -= 1
            return value

    def end_value(self):
        return self.queue[(self.end - 1 + self.size) % self.size]

    def front_value(self):
        return self.queue[self.start]

    def traverse(self):
        res = []
        i = self.start
        for _ in range(self.count):
            res.append(self.queue[i])
            i = (i + 1) % self.size
        return res

def sliding_window_max_no_deque(nums, k):
    if not nums or k == 0:
        return []

    n = len(nums)
    max_values = []
    queue = CircularQueueMax(n)  # Circular queue of same size as nums

    for i in range(n):
        # Remove indices out of window range
        if not queue.is_empty() and queue.front_value() < i - k + 1:
            queue.remove_start()

        # Remove from end elements smaller than nums[i]
        while not queue.is_empty() and nums[queue.end_value()] < nums[i]:
            queue.end = (queue.end - 1 + queue.size) % queue.size
            queue.count -= 1

        # Add current index
        queue.add_end(i)

        # Store the max if window is full
        if i >= k - 1:
            max_values.append(nums[queue.front_value()])

    return max_values

num = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max_no_deque(num, k))  # Output: [3, 3, 5, 5, 6, 7]