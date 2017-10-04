import unittest
from linkedlist_api import LinkedList
from doublylinkedlist_api import DoublyLinkedList
from circularlist_api import CircularLinkedList
from stack_api import Stack
from queue_api import Queue

import test_linked_list as tll

class LinkedListTest(unittest.TestCase):
    def test_create_linkedlist(self):
        ll = LinkedList()

    def test_add_linkedlist(self):
        ll = LinkedList()
        ll.add('a')
        self.assertEqual(ll.head.value, 'a')

    def test_insert_linkedlist(self):
        ll = LinkedList()
        ll.add('a')
        ll.add('b')
        ll.add('c')
        ll.insert(1, 'h')
        self.assertEqual(ll._get_node(1).value, 'h')

    def test_error_index_linkedlist(self):
        ll = LinkedList()
        ll.add('a')
        ll.add('b')
        ll.insert(7, 'error')

    def test_delete_linkedlist(self):
        ll = LinkedList()
        ll.add('a')
        ll.add('b')

        print(ll.size)
        ll.delete(0)

        self.assertNotEqual(ll._get_node(0).value, 'a')

class DoublyLinkedListTest(unittest.TestCase):
    def test_create_doublyll(self):
        dl = DoublyLinkedList()

    def test_add_doublyll(self):
        dl = DoublyLinkedList()

        dl.add('a')
        dl.add('b')
        dl.add('c')

        self.assertEqual(dl._get_node(0).value, 'a')

    def test_delete_doublyll(self):
        dl = DoublyLinkedList()

        dl.add('a')
        dl.add('b')
        dl.add('c')
        dl.delete(1)

        self.assertNotEqual(dl._get_node(1).value, 'b')

class QueueTest(unittest.TestCase):
    def test_create_queue(self):
        queue = Queue()

    def test_add_queue(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')

        self.assertEqual(q.linked_list._get_node(2).value, 'c')

    def test_error_index_queue(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')

        self.assertEqual(q.linked_list._get_node(7).value, 'c')

    def test_dequeue(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')
        q.dequeue()

        self.assertEqual(q.linked_list._get_node(1).value, 'c')


class StackTest(unittest.TestCase):
    def test_create_stack(self):
        stack = Stack()

    def test_push_stack(self):
        stack = Stack()
        stack.push('a')
        stack.push('c')
        stack.push('b')

        self.assertEqual(stack._get_node(0).value, 'a')


    def test_pop_stack(self):
        stack = Stack()
        stack.push('a')
        stack.push('b')
        stack.push('c')

        stack.pop()
        stack.pop()

        self.assertEqual(stack._get_node(0).value, 'a')



class CircularLinkedListTest(unittest.TestCase):
    def test_create_circularll(self):
        cl = CircularLinkedList()

    def test_debug_cycle_circularll(self):
        cl = CircularLinkedList()
        cl.add('a')
        cl.add('b')
        cl.add('c')
        cl.add('d')

        cl.debug_cycle(5)

    def test_add_circularll(self):
        cl = CircularLinkedList()

        cl.add('a')
        cl.add('b')
        cl.add('c')

        self.assertEqual(cl._get_node(0).value, 'a')

# ================================================================ #
if __name__ == '__main__':
    unittest.main()
    # tll.all()
