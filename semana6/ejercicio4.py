class Task:
    def __init__(self, name, total_time):
        self.name = name
        self.total_time = total_time  # Total time required by the process
        self.remaining_time = total_time  # Remaining time for the process

def round_robin_scheduling(tasks, time_quantum):
    queue = tasks[:]  # We make a copy of the task list
    total_waiting_time = 0
    total_turnaround_time = 0
    time_elapsed = 0
    completed_tasks = 0  # To keep track of completed processes

    front = 0  # Index indicating the first process (front of the queue)

    while completed_tasks < len(tasks):  # While not all processes are complete
        task = queue[front]  # We take the first process in the queue

        if task.remaining_time > time_quantum:
            # If the process needs more time than the quantum, reduce the remaining time
            task.remaining_time -= time_quantum
            time_elapsed += time_quantum
        else:
            # If the process finishes in this cycle
            time_elapsed += task.remaining_time
            turnaround_time = time_elapsed
            waiting_time = turnaround_time - task.total_time
            total_turnaround_time += turnaround_time
            total_waiting_time += waiting_time
            print(f"Process {task.name} completed. Waiting time: {waiting_time}, Turnaround time: {turnaround_time}")
            completed_tasks += 1  # We increment the completed processes
            task.remaining_time = 0  # The process has finished

        # We cyclically move to the next process (simulating a circular queue)
        front = (front + 1) % len(queue)

    # Calculate the average waiting time and turnaround time
    num_tasks = len(tasks)
    avg_waiting_time = total_waiting_time / num_tasks
    avg_turnaround_time = total_turnaround_time / num_tasks

    print(f"\nAverage waiting time: {avg_waiting_time}")
    print(f"Average turnaround time: {avg_turnaround_time}")

# Example of usage
tasks = [
    Task("T1", 1),  # Process with total time of 10 units
    Task("T2", 3),   # Process with total time of 5 units
    Task("T3", 1)    # Process with total time of 8 units
]

round_robin_scheduling(tasks, time_quantum=4)