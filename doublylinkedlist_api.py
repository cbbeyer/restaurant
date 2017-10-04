#!/usr/bin/env python3


class DoublyLinkedList(object):
    '''
    A doubly-linked list implementation that holds arbitrary objects.
    '''

    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0


    def debug_print(self):
        '''Prints a representation of the entire list.'''
        values = []
        n = self.head
        while n != None:
            values.append(str(n.value))
            n = n.next

        backwards = self.backwards_print()

        print('{} >>> {} >>> {}'.format(self.size, ', '.join(values), ', '.join(backwards)))

    def backwards_print(self):
        '''Prints list backwards'''
        backwards = []
        if self.size >= 1:
            last_node = self._get_node(self.size-1)
        else:
            last_node = None

        while last_node != None:
            backwards.append(str(last_node.value))
            last_node = last_node.prev

        return backwards

    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if 0 <= index < self.size:
            n = self.head
            for i in range(index):
                n = n.next
            return n
        else:
            # RAISE ERROR
            # raise IndexError('{} is not within the bounds of the current linked list.'.format(index))
            raise IndexError('The given index is not within the bounds of the current list.')


    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        if self.head is not None:
            last_node = self._get_node(self.size-1)
            last_node.next = Node(item)
            last_node.next.prev = last_node
            self.size += 1
        else:
            self.head = Node(item)
            self.size += 1


    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        if self._get_node(index):
            if index == 0:
                temp_val = self.head
                self.head = Node(item)
                self.head.next = temp_val
                temp_val.prev = self.head
                self.size += 1

            else:
                prev_val = self._get_node(index-1)
                follow_val = self._get_node(index)
                prev_val.next = Node(item)
                prev_val.next.prev = prev_val
                prev_val.next.next = follow_val
                prev_val.next.next.prev = prev_val.next
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
                if (self.size - 1) != index:
                    prev_val.next = self._get_node(index+1)
                    prev_val.next.prev = prev_val
                else:
                    prev_val.next = None


            else:
                self.head = self._get_node(index+1)
                self.head.prev = None

            self.size -= 1


    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        # find each item
        node1 = self._get_node(index1)
        node2 = self._get_node(index2)
        # swap the items
        node1.value, node2.value = node2.value, node1.value

    def check_value(self, value):
        '''Checks to see if a value is in a given list'''
        # something wrong with self.head??
        n = self.head
        while n != None:
            if n.value == value:
                return True
            n = n.next

    def get_index(self, value):
        '''Returns the index for a value'''
        n = self.head
        counter = 0
        while n != None:
            if n.value == value:
                return counter
            n = n.next
            counter += 1


######################################################
###   A node in the linked list

class Node(object):
    '''A node on the linked list'''

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return '<Node: {}>'.format(self.value)
