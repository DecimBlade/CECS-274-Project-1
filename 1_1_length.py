import sys

data = []
user_input = int(input("Please Enter a Positive Number: "))
byte = 0  # Initializes the variable before going into the for loop, to compare the size of the bytes
for k in range(user_input):  # Takes the user's input as the range for the entire for loop and iterate through it
    a = len(data)  # This gets the length of the array
    b2 = sys.getsizeof(data)  # This will get the number of bytes in the array for each index
    if b2 > byte and a > 0:
        byte = b2
        print("length:", a - 1, "bytes:", b2)  # This will print the length of the array, but since the array starts at 1
    data.append(None)  # We have to subtract it by 1 to start at 0, this will also print the number of bytes