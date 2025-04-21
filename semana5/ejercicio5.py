import random
import queue

# Customer class
class Customer:
    def __init__(self, customer_id, item_count):
        self.customer_id = customer_id
        self.item_count = item_count
        self.arrival_time = None
        self.completion_time = None

# CheckoutLane class
class CheckoutLane:
    def __init__(self, lane_id, processing_rate):
        self.lane_id = lane_id
        self.processing_rate = processing_rate
        self.queue = queue.Queue()
    
    def add_customer(self, customer):
        self.queue.put(customer)
    
    def process_customer(self, current_time):
        if not self.queue.empty():
            customer = self.queue.get()
            customer.arrival_time = current_time
            customer.completion_time = current_time + customer.item_count / self.processing_rate
            return customer
        return None

# Supermarket class
class Supermarket:
    def __init__(self, num_lanes):
        self.lanes = [CheckoutLane(i, random.uniform(1, 3)) for i in range(num_lanes)]
        self.customers = []
    
    def simulate_customer_arrival(self, current_time):
        customer = Customer(len(self.customers) + 1, random.randint(1, 30))
        self.customers.append(customer)
        shortest_lane = min(self.lanes, key=lambda lane: lane.queue.qsize())
        shortest_lane.add_customer(customer)
    
    def simulate_checkout(self, current_time):
        completed_customers = [lane.process_customer(current_time) for lane in self.lanes if lane.process_customer(current_time)]
        return completed_customers

    def calculate_statistics(self):
        total_wait_time = sum(c.completion_time - c.arrival_time for c in self.customers if c.completion_time)
        throughput = len(self.customers) / (self.customers[-1].completion_time - self.customers[0].arrival_time) if len(self.customers) > 1 else 0
        return total_wait_time / len(self.customers), throughput

def test_case_1():
    print("Test Case 1: 3 lanes, 10 time units")
    supermarket = Supermarket(3)
    for t in range(10):
        supermarket.simulate_customer_arrival(t)
        supermarket.simulate_checkout(t)
    avg_wait, throughput = supermarket.calculate_statistics()
    print(f"Avg Wait Time: {avg_wait:.2f}, Throughput: {throughput:.2f}")

test_case_1()

def test_case_2():
    print("Test Case 2: 5 lanes, fewer customers")
    supermarket = Supermarket(5)
    for t in range(10):
        supermarket.simulate_customer_arrival(t)
        supermarket.simulate_checkout(t)
    avg_wait, throughput = supermarket.calculate_statistics()
    print(f"Avg Wait Time: {avg_wait:.2f}, Throughput: {throughput:.2f}")

test_case_2()

def test_case_3():
    print("Test Case 3: Customers with more items")
    supermarket = Supermarket(3)
    for t in range(10):
        supermarket.simulate_customer_arrival(t)
        supermarket.simulate_checkout(t)
    avg_wait, throughput = supermarket.calculate_statistics()
    print(f"Avg Wait Time: {avg_wait:.2f}, Throughput: {throughput:.2f}")

test_case_3()