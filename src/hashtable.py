# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        my_hash = 5381

        for char in key:
            my_hash = (my_hash * 33) + ord(char)

        return my_hash


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index]:
            # create current var
            current = self.storage[index]

            # start while loop
            while True:
                # check if current.key == key, if it does replace current with what was passed in
                if current.key == key:
                    current.value = value
                    break
                # check if current.next is None
                elif current.next is None:
                    # if it is, set current.next to new LinkedPair
                    current.next = LinkedPair(key, value)
                    break
                else:
                    # else, set current var to current.next
                    current = current.next
        else:
            self.storage[index] = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        # get index by running hashmod on key
        index = self._hash_mod(key)
        # make sure bucket isn't empty
        if self.storage[index] is None:
            print('Error: key not found')
        else:
            # create current var
            current = self.storage[index]
            # loop through bucket looking for the matching key
            while True:
                # if first item in bucket matches key
                if current.key == key:
                    #set that index to current.next
                    self.storage[index] = current.next
                    break
                # if not, set current to current.next and repeat
                else:
                    current = current.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            return None
        else:
            # in case of multiple objects in same bucket, look for matching key and return that object's value
            # var for while loop
            current = self.storage[index]
            # while loop
            while True:
                if current.key == key:
                    return current.value
                else:
                    current = current.next

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # copy old storage
        old_storage = self.storage
        # double capacity
        self.capacity *= 2
        # expand storage to new capacity
        self.storage = [None] * self.capacity
        # loop over each bucket in old storage
        for bucket in old_storage:
            # if current bucket is none, skip to next bucket
            if bucket is None:
                continue
            else:
                # if not, insert current item into storage
                self.insert(bucket.key, bucket.value)
                # repeat until end of current bucket
                while bucket.next:
                    bucket = bucket.next
                    self.insert(bucket.key, bucket.value)





if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
