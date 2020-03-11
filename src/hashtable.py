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
        self.count = 0

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
                    self.count += 1
                    break
                else:
                    # else, set current var to current.next
                    current = current.next
        else:
            self.storage[index] = LinkedPair(key, value)
            self.count += 1


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            print('Error: key not found in hashtable')
        else:
            current = self.storage[index]

            while True:
                if current.key == key and current.next:
                    self.storage[index] = current.next
                    break
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
        # double capacity
        old_capacity = self.capacity
        self.capacity *= 2
        # create new storage
        new_storage = [None] * self.capacity
        # loop over old storage, bucket by bucket (i in range(self.capacity)
        for i in range(old_capacity):
        # if current bucket is none, skip to next bucket
            if self.storage[i] is None:
                continue
        # if not, copy current item to new storage. this will require running hashmod on the key with the new capacity
            else:
                # vars for current objects
                current_old = self.storage[i]
                current_new = None
                # index for new storage
                new_index = self._hash_mod(self.storage[i].key)
                # create new LinkedPair instance at new_storage[new_index]
                new_storage[new_index] = LinkedPair(self.storage[i].key, self.storage[i].value)
                current_new = new_storage[new_index]
                # if current.next is not None, move to next node and repeat
                while current_old.next:
                    current_old = current_old.next
                    current_new.next = LinkedPair(current_old.key, current_old.value)
                # once current.next is none, skip to next bucket
                # finally, set self.storage = new storage
        self.storage = new_storage





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
