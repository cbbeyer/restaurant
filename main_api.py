#!/usr/bin/env python3
from linkedlist_api import LinkedList
from circularlist_api import CircularLinkedList, CircularLinkedListIterator
from doublylinkedlist_api import DoublyLinkedList
from stack_api import Stack
from queue_api import Queue


# ll = LinkedList()
# ll.add('a')
# ll.add('b')
# ll.add('c')
# try:
#     ll.get(5)
# except Exception as e:
#     print('Error: {}'.format(e))
#
# cl = CircularLinkedList()
#
# cl.add('a')

# cl.add('b')
# cl.add('c')
#
# test = cl._get_node(2).next
#
# print(test)
# try:
#     cl.insert(5, 'd')
# except Exception as e:
#     print('Error: {}'.format(e))

# cl.get(3)
# test = cl._get_node(3).next

# cl.swap(1,2)
#
# cl.debug_print()

# dl = DoublyLinkedList()
#
# dl.add('a')
# dl.add('b')
# dl.add('c')
#
# dl.insert(2, 'h')
#
# print(dl._get_node(3).prev)
# dl.debug_print()
#
# dl.delete(1)
#
# print(dl._get_node(2).prev)
# dl.debug_print()

# st = Stack()
#
# st.push('a')
# st.debug_print()
# st.push('b')
# st.debug_print()
# st.push('c')
# st.debug_print()
#
# st.pop()
# st.debug_print()

# q = Queue()
#
# q.enqueue('a')
# q.enqueue('b')
# q.enqueue('c')
# q.dequeue()
# q.debug_print()
# q.dequeue()
# q.debug_print()
# q.dequeue()
#
# q.debug_print()


#
#
# def call(val):
#     dl_callahead.add(val)
#
#
# call('Heyward')
# dl_waiting.debug_print()
# call('Baggins')
# dl_waiting.debug_print()
# call('Goldworthy')
# dl_waiting.debug_print()
#
#
# arrive('Bugler')
# dl_callahead.debug_print()
# arrive('Gamgee')
# dl_callahead.debug_print()
# arrive('Hlothran')
# dl_callahead.debug_print()
# arrive('Heyward')
# dl_callahead.debug_print()
# arrive('Proudfoot')
# dl_callahead.debug_print()
# arrive('Took')
# dl_callahead.debug_print()
# arrive('Smallburrow')
# dl_callahead.debug_print()
# arrive('Sackville')
# dl_callahead.debug_print()
# arrive('Mugwort')
# dl_callahead.debug_print()
# arrive('Goldworthy')
# dl_callahead.debug_print()


















class Processor(object):

    def __init__(self):
        '''Creates the lists'''
        self.callahead = DoublyLinkedList()
        self.waiting = DoublyLinkedList()
        self.appetizers = Queue()
        self.buzzers = Stack()
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.songs = CircularLinkedList()
        self.songs.add('Song 1')
        self.songs.add('Song 2')
        self.songs.add('Song 3')
        self.songs_iter = CircularLinkedListIterator(self.songs)

    def run(self, f):
        '''Processes the given file stream.'''
        for line_i, line in enumerate(f):
            line = line.rstrip()
            print('{}:{}'.format(line_i, line))
            parts = line.split(',')
            # call this command's function
            try:
                func = getattr(self, 'cmd_{}'.format(parts[0].lower()))
                func(*parts[1:])
            except Exception as e:
                print('Error: {}'.format(e))

    def cmd_debug(self, *args):
        self.callahead.debug_print()
        self.waiting.debug_print()
        self.appetizers.debug_print()
        self.buzzers.debug_print()
        self.songs.debug_print()

    def cmd_song(self, *args):
        # write logic here
        pass

# NEED TO FIX
    def cmd_appetizer(self, *args):
        if self.appetizers.linked_list.size is not 0:
            app = self.appetizers.linked_list._get_node(0)
            backwards = self.waiting.backwards_print()
            last_three = []
            if len(backwards) >= 3:
                for i in range(3):
                    last_three.append(backwards[i])
            else:
                last_three = backwards
            print('{} >>> {}'.format(app.value, ', '.join(last_three)))
        self.appetizers.dequeue()


    def cmd_appetizer_ready(self, *args):
        self.appetizers.enqueue(args[0])

    def cmd_call(self, *args):
        self.callahead.add(args[0])

    def cmd_arrive(self, *args):
        if self.callahead.check_value(args[0]):
            if self.waiting.size > 4:
                self.waiting.insert((self.waiting.size-4), args[0])
                self.callahead.delete(self.callahead.get_index(args[0]))
            else:
                self.waiting.insert(0, args[0])
                self.callahead.delete(self.callahead.get_index(args[0]))
        else:
            self.waiting.add(args[0])

        self.buzzers.pop()

    def cmd_seat(self, *args):
        self.waiting.get(0)
        self.waiting.delete(0)
        self.buzzers.push('Buzzer')

    def cmd_leave(self, *args):
        temp = self.waiting.get_index(args[0])
        if temp is not False:
            self.waiting.delete(temp)
        self.buzzers.push('Buzzer')

#######################
###   Main loop

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
with open('example_data.csv', newline='') as f:
    processor = Processor()
    processor.run(f)
