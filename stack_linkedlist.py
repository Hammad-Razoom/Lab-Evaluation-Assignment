# Stack implementation using Linked List

# Node class represents each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node

# Stack implementation using Linked List
class Stack:
    def __init__(self):
        self.top = None  # Top of the stack

    # Push operation to add an element to the stack
    def push(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.top  # Link the new node to the top
        self.top = new_node  # Update the top pointer

    # Pop operation to remove the top element from the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_data = self.top.data  # Get the data of the top node
        self.top = self.top.next  # Update the top pointer to the next node
        return popped_data

    # Peek operation to get the top element without removing it
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data

    # Check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Display all elements in the stack
    def display(self):
        current = self.top
        stack_elements = []
        while current:
            stack_elements.append(current.data)
            current = current.next
        return stack_elements

# Example usage of Stack
if __name__ == "__main__":
    print("Stack Operations:")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushes:", stack.display())
    print("Popped from stack:", stack.pop())
    print("Stack after pop:", stack.display())
    print("Top of stack:", stack.peek())
