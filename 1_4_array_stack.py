from utils import new_array
from base import BaseList

class ArrayStack(BaseList):
    def __init__(self, iterable=[]):  # This makes the class iterable or else it will give an error from Base.py
        self._initialize()
        self.add_all(iterable)
        
    def _initialize(self):  # Initializes the variables
        self.array = new_array(1)  # Created a new array to start
        self.n = 0

    def remove(self, i):  # This is the remove function that takes in an index
        x = self.array[i]
        self.array[index:self.n - 1] = self.array[index + 1:self.n]
        self.n -= 1
        if len(self.array) >= 3*self.n:
            self.resize()
        return x

    def add(self, index, x):  # This adds value x at the index into the array
        if self.n == len(self.array):
            self.resize()  # This goes to the resize function
        self.array[index + 1:self.n + 1] = self.array[index:self.n]
        self.array[index] = x
        self.n += 1  # Set this to increment

    def get(self, index):  # This gets the value at the index in the array
        return self.array[index]  # Returns the value at the given index

    def set(self, index, x):  # This sets the value,x, at the declared index
        y = self.array[index]
        self.array[index] = x
        return y  # This returns the value at the given index
  
    def resize(self):  # This function creates a new array, that takes the max of either 1 or double of the capacity
        b = new_array(max(1, 2 * self.n))
        b[0:self.n] = self.array[0:self.n]  # Takes the original array and copies into the new array
        self.array = b  # Restates the original array to equal to the new array

stack = ArrayStack()
stack.add(0,1)
stack.add(0,2)
stack.add(1,3)
stack.add(3,5)
stack.add(2,4)
print(stack.get(0))  # this will print 2
print(stack.get(1))  # this will print 3
print(stack.get(2))  # this will print 4
print(stack.get(3))  # this will print 1
print(stack.get(4))  # this will print 5


