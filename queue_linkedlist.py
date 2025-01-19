# Queue implementation using Linked List

# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node

# Queue implementation using Linked List
class Queue:
    def __init__(self):
        self.front = None  # Front of the queue
        self.rear = None   # Rear of the queue

    # Enqueue operation to add an element to the queue
    def enqueue(self, data):
        new_node = Node(data)  # Create a new node
        if self.rear is None:  # If the queue is empty
            self.front = self.rear = new_node  # Update both front and rear pointers
            return
        self.rear.next = new_node  # Link the new node to the rear
        self.rear = new_node  # Update the rear pointer

    # Dequeue operation to remove the front element from the queue
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        dequeued_data = self.front.data  # Get the data of the front node
        self.front = self.front.next  # Update the front pointer to the next node
        if self.front is None:  # If the queue becomes empty
            self.rear = None  # Update the rear pointer as well
        return dequeued_data

    # Peek operation to get the front element without removing it
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.data

    # Check if the queue is empty
    def is_empty(self):
        return self.front is None

    # Display all elements in the queue
    def display(self):
        current = self.front
        queue_elements = []
        while current:
            queue_elements.append(current.data)
            current = current.next
        return queue_elements

# Example usage of Queue
if __name__ == "__main__":
    print("Queue Operations:")
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue after enqueues:", queue.display())
    print("Dequeued from queue:", queue.dequeue())
    print("Queue after dequeue:", queue.display())
    print("Front of queue:", queue.peek())
