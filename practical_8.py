# implememntation of stack using list
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Test the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.size())  # Should print 2

#  Implementation od queque 
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test the Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.front())  # Should print 2
print(queue.size())  # Should print 2

# Implementatingf stack using queque
from queue import Queue

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.get()

    def top(self) -> int:
        return self.q1.queue[0]

    def empty(self) -> bool:
        return self.q1.empty()

# Function to evaluate postfix expressions using a stack
def evaluate_postfix(expression):
    stack = Stack()
    for char in expression:
        if (char.isdigit()):
            stack.push(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.push(a + b)
            elif char == '-':
                stack.push(a - b)
            elif char == '*':
                stack.push(a * b)
            elif char == '/':
                stack.push(a / b)
    return stack.pop()

# Function to implement a queue using two stacks
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if not self.stack2.is_empty():
            return self.stack2.pop()
        else:
            raise IndexError("Queue is empty")

# Function to implement a basic task scheduler using a queue
def task_scheduler(tasks):
    queue = Queue()
    for task in tasks:
        queue.enqueue(task)
    while not queue.is_empty():
        task = queue.dequeue()
        print(f"Processing task: {task}")

# Function to convert infix expressions to postfix using a stack
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = Stack()
    postfix = []
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char in precedence:
            while (not stack.is_empty() and
                   precedence.get(stack.peek(), 0) >= precedence[char]):
                postfix.append(stack.pop())
            stack.push(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '('
    while not stack.is_empty():
        postfix.append(stack.pop())
    return ''.join(postfix)

# Example usage:
# Evaluate postfix expression
print(evaluate_postfix("231*+9-"))  # Should print -4

# Queue using two stacks
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1

# Task scheduler
task_scheduler(["Task1", "Task2", "Task3"])

# Convert infix to postfix
print(infix_to_postfix("a+b*(c^d-e)^(f+g*h)-i"))  # Should print abcd^e-fgh*+^*+i-

