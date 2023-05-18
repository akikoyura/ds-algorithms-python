class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0

    """
    Separate chaining:
    In case of collision, the `put()` function uses the same bucket to store a linked list of key-value pairs
    Every bucket will have it's own separate chain of linked list nodes.
    """

    def put(self, key, value):  # The key is a string, a value is numeric
        bucket_index = self.get_bucket_index(key)
        new_node = LinkedListNode(key, value)  # create a node
        head = self.bucket_array[
            bucket_index]  # create a reference that points to the existing bucket at position bucket_index

        # check if key is already present in the map, and UPDATE it's value
        # Remember, a key should always be unique
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        """
        If the key is a new one, hence not found in the chain ( LinkedList ), then following two cases arise:
        1. The key has generated a new bucket_index
        2. The key has generated and existing bucket_index.
           The event is a Collision, i.e., two different keys have same bucket_index
        
        In both the cases, we will prepend the new node (key, value) at the beginning (head) of the chain (LinkedList).
        Remember that each `bucket` at position `bucket_index` is actually a chain (LinkedList) with 1 or more nodes.
        """

        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node  # Prepend the new node in the beginning of the Linked list
        self.num_entries += 1

    def get(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)  # The returned hash code will be the bucket_index
        return bucket_index

    def get_hash_code(self, key):
        key = str(key)

        num_buckets = len(self.bucket_array)  # Length of array to be used in Mod operation
        current_coefficient = 1  # represents (self.p^0) which is 1
        hash_code = 0

        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets  # compress hash_code ( Mod Operation )
            current_coefficient *= self.p  # compress coefficient as well
            current_coefficient = current_coefficient % num_buckets

        return hash_code % num_buckets  # one last compression before returning

    def size(self):
        return self.num_entries

    # Helper function to see the hashmap
    def __repr__(self):
        output = "\nLet's veiew the hash map: "
        node = self.bucket_array

        for bucket_index, node in enumerate(self.bucket_array):
            if node is None:
                output += '\n[{}]'.format(bucket_index)
            else:
                output += '\n[{}]'.format(bucket_index)
                while node is not None:
                    output += ' ({}, {}) '.format(node.key, node.value)
                    if node.next is not None:
                        output += ' --> '
                    node = node.next
        return output


if __name__ == '__main__':
    # check the bucket_index for two different strings made with same set of characters
    hash_map = HashMap()

    hash_map.put("one", 1)
    hash_map.put("two", 2)
    hash_map.put("three", 3)
    hash_map.put("neo", 11)

    print("size: {}".format(hash_map.size()))

    print("one: {}".format(hash_map.get("one")))
    print("neo: {}".format(hash_map.get("neo")))
    print("three: {}".format(hash_map.get("three")))

    hash_map

    # bucket_index = hash_map.get_bucket_index("one")
    # print(bucket_index)
    #
    # hash_map_1 = HashMap()
    # bucket_index_1 = hash_map_1.get_bucket_index("neo")
    # print(bucket_index_1)
