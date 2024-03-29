# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.key} - {self.value}"

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
        index = self._hash_mod(key)
        new_item = LinkedPair(key, value)
        current_node = self.storage[index]
        last_item = None

        if self.storage[index] == None:
            self.storage[index] = new_item

        else:
            while True:
                if current_node.key == key:
                    current_node.value = value
                    break
                if current_node.next == None:
                    current_node.next = new_item
                    break
                current_node = current_node.next

        #index = self._hash_mod(key)
        #current_node = self.storage[index]
        #new_item = LinkedPair(key, value)
        #last_item = None
        #while current_node is not None and current_node.key != key:
        #    last_item = current_node
        #    current_node = last_item.next
        #if current_node is not None:
        #    current_node.value = value
        #else:
        #    new_item.next = self.storage[index]
#            self.storage[index] = new_item
#


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] == None:
            print("Item not found")
        else:
            current_node = self.storage[index]
            while current_node != None:
                 if current_node.key == key:
                     current_node.value = None 
                     current_node.key = None
                     current_node = None
                     break
                 if current_node.next == None:
                     print("Item not found")
                     return None
                 current_node = current_node.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] != None:
            current_node = self.storage[index]
            while current_node != None:
                if current_node.key == key:
                    return current_node.value
                current_node = current_node.next
        return None


        return self.storage[index].value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity 
        current_node = None

        for i in old_storage:
            current_node  = i
            while current_node != None:
                self.insert(current_node.key, current_node.value )
                current_node = current_node.next

             



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



new_table = HashTable(3) 
new_table.insert("angel", "torres")
new_table.insert("rob", "towe")
new_table.insert("mario", "bros")
#print(new_table.retrieve("angel"))
#print(new_table.retrieve("rob"))
#print(new_table.retrieve("mario"))
#new_table.remove("angel")
#print("-------")
#print(new_table.retrieve("angel" ), "after removal")
#print(new_table.storage, "< -----------------before resize")
#new_table.resize()
#print(new_table.storage, "< -----------------after resize")
#print(new_table.retrieve("rob"))
#print(new_table.retrieve("mario"))
