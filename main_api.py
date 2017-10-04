#!/usr/bin/env python3
from linkedlist_api import LinkedList
from circularlist_api import CircularLinkedList, CircularLinkedListIterator
from doublylinkedlist_api import DoublyLinkedList
from stack_api import Stack
from queue_api import Queue
import sys


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
        self.songs_iter.next()
        pass

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
                # self.prev probs not being added
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

orig_stdout = sys.stdout
f = open('output.txt', 'w')
sys.stdout = f

with open('data.csv', newline='') as f:
    processor = Processor()
    processor.run(f)

sys.stdout = orig_stdout
f.close()
