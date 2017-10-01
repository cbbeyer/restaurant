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
cl = CircularLinkedList()

cl.add('a')
cl.add('b')
cl.add('c')

test = cl._get_node(2).next

print(test)







# class Processor(object):
#
#     def __init__(self):
#         '''Creates the lists'''
#         self.callahead = DoublyLinkedList()
#         self.waiting = DoublyLinkedList()
#         self.appetizers = Queue()
#         self.buzzers = Stack()
#         self.buzzers.push('Buzzer')
#         self.buzzers.push('Buzzer')
#         self.buzzers.push('Buzzer')
#         self.buzzers.push('Buzzer')
#         self.buzzers.push('Buzzer')
#         self.buzzers.push('Buzzer')
#         self.buzzers.push('Buzzer')
#         self.buzzers.push('Buzzer')
#         self.songs = CircularLinkedList()
#         self.songs.add('Song 1')
#         self.songs.add('Song 2')
#         self.songs.add('Song 3')
#         self.songs_iter = CircularLinkedListIterator(self.songs)
#
#     def run(self, f):
#         '''Processes the given file stream.'''
#         for line_i, line in enumerate(f):
#             line = line.rstrip()
#             print('{}:{}'.format(line_i, line))
#             parts = line.split(',')
#             # call this command's function
#             try:
#                 func = getattr(self, 'cmd_{}'.format(parts[0].lower()))
#                 func(*parts[1:])
#             except Exception as e:
#                 print('Error: {}'.format(e))
#
#     def cmd_debug(self, *args):
#         # write logic here
#
#     def cmd_song(self, *args):
#         # write logic here
#
#     def cmd_appetizer(self, *args):
#         # write logic here
#
#     def cmd_appetizer_ready(self, *args):
#         # write logic here
#         # self.ar.set(int(args[0]), args[1])
#
#     def cmd_call(self, *args):
#         # write logic here
#         # print(self.ar.get(int(args[0])))
#
#     def cmd_arrive(self, *args):
#         # write logic here
#
#     def cmd_seat(self, *args):
#         # write logic here
#
# #######################
# ###   Main loop
#
# with open('data.csv', newline='') as f:
#     processor = Processor()
#     processor.run(f)
#
#
#     def debug(self):
#         self.callahead.debug_print()
#         self.waiting.debug_print()
#         self.appetizers.debug_print()
#         self.buzzers.debug_print()
#         self.songs.debug_print()
#
#
#
# #######################
# ###   Main loop
#
# with open('data.csv', newline='') as f:
#     processor = Processor()
#     processor.run(f)
