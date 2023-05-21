"""
    Instructions
    * Create a HashTable class, with the following functions:
        store() - a function that takes a string as input, and stores it into the hash table.
        lookup() - a function that checks if a string is already available in the hash table.
        If yes, return the hash value, else return -1
        calculate_hash_value() - a helper function to calculate a hash value of a given string
"""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        hash_value = self.calculate_hash_value(string)  # generate the hash value
        if hash_value != -1:  # if the string is a new one
            if self.table[hash_value] is not None:  # if the bucket is non-empty
                self.table[hash_value].append(string)  # append the string in the líst at that bucket
            else:
                self.table[hash_value] = [string]  # store the string in a new list at that bucket

    def lookup(self, string):
        """
        TODO: Return the hash value if the
        string is already in the table.
        Return -1 otherwise.
        """
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value] is not None:
            if string in self.table[hash_value]:
                return hash_value

        return -1

    def calculate_hash_value(self, string):
        """
        TODO: Helper function to calculate a
        hash value from a string.
        """
        value = ord(string[0]) * 100 + ord(string[1])
        return value


if __name__ == '__main__':
    # Setup
    hash_table = HashTable()

    # Test calculate_hash_value
    print(hash_table.calculate_hash_value('UDACITY'))  # Should be 8568

    # Test Lookup edge case
    print(hash_table.lookup('UDACITY'))  # Should be -1

    # Test store
    hash_table.store('UDACITY')
    print(hash_table.lookup('UDACITY'))  # Should be 8568

    # Test store edge case
    hash_table.store('UDACIOUS')
    print(hash_table.lookup('UDACIOUS'))  # Should be 8568
