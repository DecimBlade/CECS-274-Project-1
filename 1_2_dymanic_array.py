from utils import new_array
class DynamicArray():
    def __init__(self):
        self.array = new_array(1)  # This is to establish the array
        self.n = 0  # This variable is to count the elements in the array
        self.capacity = len(self.array)  # Takes the length of the array

    def resize(self, k, capacity):
        b = [None] * capacity  # Make a new array to transfer
        for i in range(self.n):  # This will then make a copy of A ^^^
            b[i] = self.array[i]
        for j in range(self.n - 1, k - 1, -1):  # This will then put all of the original array into the new array
            b[j + 1] = self.array[j]
        self.array = b  # This will restate the new array into the original array since the original array
                        # Is used in the entire problem not just for the resize value

    def insert(self, k, value):  # This resizes the list to add 1 more than the original array
        self.resize(k, self.n + 1)
        self.array[k] = value  # This will then set the value to the index, k
        self.n += 1  # This is to increment the elements in the array

    def __str__(self):  # This function is so it will print the array and add the bracket in the front
        s = "["
        for i in range(self.n):
            s += "%r" % self.array[i]
            if i < self.n - 1:
                s += ","
        s += "]"  # This will add the bracket at the end of the array
        return s

dynamic_array = DynamicArray()
dynamic_array.insert(0, 1)
dynamic_array.insert(0, 2)
dynamic_array.insert(1, 3)
dynamic_array.insert(3, 5)
dynamic_array.insert(2, 4)  # this will print [2,3,4,1,5]

print(dynamic_array)
