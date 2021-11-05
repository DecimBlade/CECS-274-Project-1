# When the stack is empty, the algorithm will push all the elements in the queue and push them to the reverse queue
# until the reverse queue is empty. The time for this is O(n).
# The time is O(n) because if the code pushes and pops in large amounts, the total time would be linearly proportional
# but since we used enqueue, dequeue, first, is_empty the running time is O(1)

class Queue():
    def __init__(self):
        self.q = Stack()  # This creates 2 variables for queue and a reverse queue that is used with the Stack() function
        self.rq = Stack()

    def is_empty(self):  # This function is called if the queue is empty, it will go to the function if the queue is empty
        return self.q.is_empty()

    def add(self, value):  # This will go to the push function in the stack to append the value into the array
        self.q.push(value)

    def remove(self):  # This will check if the queue is empty and will go to the is_empty function if it is
        if self.q.is_empty():
            return "Queue is empty"
        while not self.q.is_empty() > 0:
            self.rq.push(self.q.pop())
        value = None
        value = self.rq.pop()
        while not self.rq.is_empty() > 0:  # This will go through the functions and return the number that was removed in the queue
            self.q.push(self.rq.pop())
        if value is not None:
            return value


class Stack():
    def __init__(self):
        self.s = []  # Initializes the Stack array

    def pop(self):  # This returns the value in the stack
        return self.s.pop()

    def push(self, value):  # This puts the value at the end of the list
        self.s.append(value)

    def is_empty(self):  # This will return True and print "Queue is empty" when True
        return len(self.s) == 0

    def not_empty(self):  # If the stack isn't empty it will return the first value in the array
        if not self.s.is_empty():
            return self.s[-1]


# Test case is the same as problem 3

queue = Queue()  # Don't forget you need to put print before the remove function
print(queue.remove())  # because the remove function is returning a value not printing one.
queue.add(1)  # This is going to add 1 to the queue
queue.add(2)  # Same with the rest of these numbers
queue.add(3)
print(queue.remove())
queue.add(4)
print(queue.remove())
print(queue.remove())
queue.add(5)
print(queue.remove())
print(queue.remove())
print(queue.remove())  # Since all the items are removed this is going to print "Queue is empty"