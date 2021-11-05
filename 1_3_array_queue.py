from utils import new_array

class ArrayQueue:

    def __init__(self):
        # Put these variables as 0 because they will be used to compare and changed in the functions later
        self.front = 0
        self.n = 0
        capacity = 1
        self.data = [None] * capacity  # Creates an array with the number of capacity slots

    def is_empty(self):  # This is activated from def remove meaning that if there nothing in the array
        return self.n == 0  # This statement will return true meaning that it will print "Queue is empty"

    def resize(self, newcapacity):  # This function is to resize everything
        pastdata = self.data
        FrontNumber = self.front
        # This reassigned the original array to a new array
        self.data = [None] * newcapacity
        # This for loop is to put everything in the original array in the new array
        for k in range(self.n):
            self.data[k] = pastdata[FrontNumber]
            FrontNumber = (FrontNumber + 1) % len(pastdata)
        self.front = 0

    def add(self, x):  # This function adds the value into the queue
        if self.n == len(self.data):
            self.resize(self.n * 2)
        index = (self.front + self.n) % (len(self.data))
        self.data[index] = x
        self.n = self.n + 1

    def remove(self):  # This is to remove the number in the first index
        if self.is_empty():  # This is because the ArrayQueue is FIFO
            # This function returns True if there is nothing in the Queue and will print the statement below
            return "Queue is empty"
        # You have to print this statement because it is returning the string
        frontofthearray = self.data[self.front]
        # This gets the number at the first index in the array
        self.data[self.front] = None
        self.front = (self.front + 1) % (len(self.data))
        self.n = self.n - 1
        # We need to resize the array and cut it down
        if self.n < len(self.data) // 4:
            self.resize(len(self.data) // 2)
        # This is going to return the number we removed because in the outputs
        # We want to return the number in the front that is removed.
        return frontofthearray


queue = ArrayQueue()  # Don't forget you need to put print before the remove function
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