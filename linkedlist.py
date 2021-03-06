class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.

        Running time: O(1) Why and under what conditions?
        All it does is return a value."""

        # count = 0
        # node = self.head
        # while node is not None:
        #     count += 1
        #     node = node.next
        # return count
        return self.size

    def append(self, item):
        """
        Insert the given item at the tail of this linked list.
        Running time: O(1) Why and under what conditions?
        Changing pointers to different data and nodes takes constant time.
        """
        
        new = Node(item)
     
        if self.tail is not None:
            self.tail.next = new
            self.tail = new
        else:
            self.head = new
            self.tail = new
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) Why and under what conditions?
        Changing pointers to different data and nodes takes constant time."""
        # Create new node to hold given item
        new = Node(item)
        # Prepend node before head, if it exists
        if self.head is not None:
            new.next = self.head
            self.head = new
        else:
            self.head = new
            self.tail = new
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Where n represents the number of nodes in the list.

        Best case running time: O(1) Why and under what conditions?
        Where the item is the first or very early in the list.

        Worst case running time: O(n) Why and under what conditions?
        Where the item is the last in the list or not in the list at all."""
        # Loop through all nodes to find item where quality(item) is True

        current = self.head

        while current is not None:
            if quality(current.data):
                return current.data
            current = current.next
        # Check if node's data satisfies given quality function

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Where n represents the number of nodes in the list.

        Best case running time: O(1) Why and under what conditions?
        Where the item is the first or very early in the list.
        
        Worst case running time: O(n) Why and under what conditions?
        Where the item is the last in the list or not in the list at all.
        """
        current = self.head # O(1)
        previous = None # O(1)
        # O(n) when it reaches the end of the list
        while current is not None: 
            # Check if current node has the item we're looking for
            if current.data == item: 
                self.size -= 1 # O(1)
                # Check if the current node is the last one
                if current.next is None:
                    self.tail = previous # O(1)
                if previous is not None:
                    previous.next = current.next # O(1)
                    return self.head # O(1)
                else:
                    self.head = current.next # O(1)
                    return self.head # O(1)
            previous = current
            current = current.next
        raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()