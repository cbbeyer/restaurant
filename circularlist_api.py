#!/usr/bin/env python3

class CircularLinkedList(object):
    '''
    A circularly-linked list implementation that holds arbitrary objects.
    '''

    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0

    def debug_print(self):
        '''Prints a representation of the entire list.'''
        values = []
        n = self.head
        i = 0

        while i < self.size:
            values.append(str(n.value))
            n = n.next
            i += 1
        print('{} >>> {}'.format(self.size, ', '.join(values)))

    def reverse_list(self):
        '''Reverses and returns a given circular list'''
        reverse_list = CircularLinkedList()
        i = 0
        n = self.head

        while i < self.size:
            if i == 0:
                reverse_list.add(n.value)
            else:
                reverse_list.insert(0, n.value)
            n = n.next
            i += 1

        return reverse_list

    def debug_cycle(self, count):
        '''Prints a representation of the entire cycled list up to count items'''
        # front to back count times, or back to front count times
        abs_count = abs(count)
        values = []
        i = 0

        if count > 0:
            n = self.head
            for t in range(abs_count):
                while i < self.size:
                    values.append(str(n.value))
                    n = n.next
                    i += 1
                print('{} >>> {}'.format(self.size, ', '.join(values)))
        else:
            rev_list = self.reverse_list()
            n = rev_list.head
            for t in range(abs_count):
                while i < self.size:
                    values.append(str(n.value))
                    n = n.next
                    i += 1
                print('{} >>> {}'.format(self.size, ', '.join(values)))


    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if 0 <= index < self.size:
            n = self.head
            for i in range(index):
                n = n.next
            return n
        else:
            raise IndexError('The given index is not within the bounds of the current list.')

    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        # if statement for first added node to linked list
        if self.head is not None:
            last_node= self._get_node(self.size-1)
            last_node.next = Node(item)
            last_node.next.next = self.head
            self.size += 1
        else:
            self.head = Node(item)
            self.head.next = self.head
            self.size += 1

    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        if self._get_node(index):
            if index == 0:
                temp_val = self.head
                self.head = Node(item)
                if self.size > 0:
                    self.head.next = temp_val
                    # self.head.next.next = self.head
                else:
                    self.head = temp_val
                self.size += 1

            else:
                prev_val = self._get_node(index-1)
                follow_val = self._get_node(index)
                prev_val.next = Node(item)
                prev_val.next.next = follow_val
                self.size += 1


    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if self._get_node(index):
            val = self._get_node(index)
            val.value = item


    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if self._get_node(index):
            n = self._get_node(index)
            print(n.value)

    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        if self._get_node(index):
            if index is not 0:
                prev_val = self._get_node(index-1)
                if index == (self.size-1):
                    prev_val.next = self.head
                else:
                    prev_val.next = self._get_node(index+1)
            else:
                if self.size == 1:
                    self.head = None
                else:
                    self.head = self._get_node(index+1)
            self.size -= 1

    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        # find each item
        node1 = self._get_node(index1)
        node2 = self._get_node(index2)
        # swap the items
        node1.value, node2.value = node2.value, node1.value



######################################################
###   A node in the linked list

class Node(object):
    '''A node on the linked list'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '<Node: {}>'.format(self.value)



######################################################
###   An iterator for the circular list

class CircularLinkedListIterator(object):
    def __init__(self, circular_list):
        '''Starts the iterator on the given circular list.'''
        self.cl = circular_list
        self.index = 0

    def has_next(self):
        '''Returns whether there is another value in the list.'''
        if self.cl._get_node(self.index) is not None:
            return True
        else:
            return False

    def next(self):
        '''Returns the next value, and increments the iterator by one value.'''
        if self.has_next:
            if self.index < self.cl.size:
                val = self.cl._get_node(self.index).value
                self.index += 1
                print(val)
                return val
            else:
                val = self.cl._get_node(0).value
                print(val)
                self.index = 1
                return val
