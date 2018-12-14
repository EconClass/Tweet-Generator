#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(p) Why and under what conditions?
        Where p represents the number of key:value pairs in the hashtable.
        p can also be found by b*i where:
        b = number of buckets
        i = number of items in the bucket"""
        # Collect all keys in each bucket
        all_keys = []
        # O(b) where b = number of buckets
        for bucket in self.buckets: # O(b)
            for key, _ in bucket.items(): # O(i)
                all_keys.append(key) # O(1)
        return all_keys # O(1)

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(p) Why and under what conditions?
        Where p represents the number of key:value pairs in the hashtable.
        p can also be found by b*i where:
        b = number of buckets
        i = number of items in the bucket"""
        all_values = []
        
        for bucket in self.buckets:# O(b)
            for _, value in bucket.items():# O(i)
                all_values.append(value) # O(1)
        return all_values # O(1)

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(p) Why and under what conditions?
        Where p represents the number of key:value pairs in the hashtable.
        p can also be found by b*i where:
        b = number of buckets
        i = number of items in the bucket"""
        
        all_items = [] # O(1)
        for bucket in self.buckets: # O(b)
            all_items.extend(bucket.items()) # O(i)
        return all_items# O(1)

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(b) Why and under what conditions?
        """
        # Loop through all buckets
        count = 0 # O(1)
        for bucket in self.buckets: # O(b)
            ## size is a property of the linked list that tracks the number of nodes in the list ##
            count += bucket.size # O(1) 
        return count # O(1)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(l) if key is not in list or last in the list.
        O(1) if key is first on list.
        """
        
        index = self._bucket_index(key) # O(1)
        bucket = self.buckets[index] # O(1)

        # O(1) or O(l) where l = number of nodes in the list
        compare = bucket.find(lambda data: data[0] == key) 

        if compare: # O(1)
            return True # O(1)
        return False # O(1)

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(l) or O(1) Why and under what conditions?"""
        
        index = self._bucket_index(key) # O(1)
        bucket = self.buckets[index] # O(1)

        # O(1) or O(l) where l = number of nodes in the list
        compare = bucket.find(lambda data: data[0] == key) 

        if compare: # O(1)
            return compare[1] # O(1)
        else: raise KeyError('Key not found: {}'.format(key)) # O(1)

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(???) Why and under what conditions?"""
        
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        # O(1) or O(l) where l = number of nodes in the list
        compare = bucket.find(lambda data: data[0] == key)

        if compare:
            self.delete(key)
        bucket.prepend((key,value))


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(l) Why and under what conditions?
        If the item containing the key is not in the list or is the last in the list."""
        
        index = self._bucket_index(key) # O(1)
        bucket = self.buckets[index] # O(1)

        # O(1) or O(l) where l = number of items in the list
        compare = bucket.find(lambda data: data[0] == key)

        # O(1) or O(l) where l = number of items in the list
        value = self.get(key)

        if compare:
            # O(1) or O(l) where l = number of items in the list
            bucket.delete((key,value))
        else: raise KeyError('Key not found: {}'.format(key))

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
