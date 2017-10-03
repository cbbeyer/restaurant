#!/usr/bin/env python3
from linkedlist_api import LinkedList

class Queue(object):
    '''
    A linked list implementation of a queue.

    This contains a LinkedList internally.  It does not extend LinkedList.
    In other words, this class uses "Composition" rather than "Inheritance".
    '''

    def __init__(self):
        '''Constructor'''
        self.linked_list = LinkedList()

    def debug_print(self):
        '''Prints a representation of the entire queue.'''
        self.linked_list.debug_print()

    def enqueue(self, item):
        '''Adds an item to the end of the queue'''
        self.linked_list.add(item)

    def dequeue(self):
        '''
        Dequeues the first item from the list.  This involves the following:
            1. Get the first node in the list.
            2. Delete the node from the list.
            3. Return the value of the node.
        '''
        if self.linked_list.head is not None:
            first_node = self.linked_list.head
            self.linked_list.head = self.linked_list.head.next
            self.linked_list.size -= 1
            return first_node
        else:
            raise IndexError('The given index is not within the bounds of the current list.')

    def size(self):
        '''Returns the number of items in the queue'''
        print(self.linked_list.size)
