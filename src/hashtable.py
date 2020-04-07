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
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # hash the key
        hashed_key = self._hash_mod(key)
        # pair var
        pair = self.storage[hashed_key]

        # if there's nothing in the bucket at hashed_key, put new LinkedPair there
        if pair is None:
            pair = LinkedPair(key, value)
        # else, we'll traverse the nodes until we either find the key or we hit the end of the chain
        else:
            while pair is not None:
                # if we get to the end of the chain without finding the key, add new LinkedPair on end of chain
                if pair.next == None:
                    pair.next = LinkedPair(key, value)
                    break
                # if we find the key (key already exists in chain), replace the value
                elif pair.key == key:
                    pair.value = value
                    break
                # if current key != key arg and current pair has a next, go to next and continue loop
                else:
                    pair = pair.next
                    continue


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # hash the key
        hashed_key = self._hash_mod(key)
        # pair var
        pair = self.storage[hashed_key]

        # print warning if bucket is empty
        if pair is None:
            print('Warning: key not found')
        # else, traverse nodes until key is found
        else:
            while pair is not None:
            # if pair.key == key and next is None, set bucket to None
            if pair.key == key and pair.next is None:
                pair = None
                break
            # if we hit the end of the chain and key is still not found, print warning
            elif pair.key != key and pair.next is None:
                print('Warning: key not found')
            # when key is found, set next to next.next. this cuts the discarded node out of the chain
            elif pair.next and pair.next.key == key:
                pair.next = pair.next.next
            # if current key != key arg and current pair has a next, go to next and continue loop
            else:
                pair = pair.next
                continue

        # if self.storage[hashed_key] == None:
        #     print('Warning: key not found')
        # else:    
        #     self.storage[hashed_key] = None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # hash key
        hashed_key = self._hash_mod(key)
        # pair var
        pair = self.storage[hashed_key]

        # if bucket is empty, return None
        if pair is None:
            return None
        # else, traverse chain until key is found
        else:
            while pair is not None:
            # if key is found, return value
            if pair.key == key:
                return pair.value
                break
            # if we reach the end of the chain without finding key, return None
            elif pair.key != key and pair.next is None:
                return None
                break
            # if current key != key arg and current pair has a next, go to next and continue loop
            else:
                pair = pair.next
                continue


        # if self.storage[hashed_key]:
        #     return self.storage[hashed_key].value
        # else:    
        #     return self.storage[hashed_key]    


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for bucket in old_storage:
            if bucket is not None:
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