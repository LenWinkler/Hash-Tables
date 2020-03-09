class DynamicArray:
    # my_array = [4] # make an empty array of size 4, not a 1 size array with 4 in it
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        # make sure we have open space
        if self.count >= self.capacity:
            # make array resize dynamically
            print('Error: array is full')
            return

        # make sure index is in range
        if index > self.count:
            print('Error: index out of range')

        # shift everything right
        # start with last one, move it to the right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]

        # insert our value
        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)

    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]

        self.storage = new_storage

my_array = DynamicArray(4)
my_array.insert(0, 1)
my_array.insert(0, 2)
my_array.insert(1, 3)
my_array.insert(3, 4)
my_array.insert(0, 5)