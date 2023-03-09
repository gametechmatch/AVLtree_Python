#################################################################
# LinkStack.py
#################################################################
# Source Title: LinkStack.py
# Source Type: Book
# Source Title: Data Structures & Algorithms in Python
# Source Authors: John Canning, Alan Broder, & Robert Lafore
#################################################################
# Course: Data Structures
# Programming Project 10.1
#################################################################
# Set up a Stack using a linked list data structure.
# The binary search tree file imports this file.
#################################################################
from LinkedList import *

# Link stack class that defines a stack by renaming methods from
# the linked list class
##################################################################
class Stack(LinkedList):
   push = LinkedList.insert
   pop = LinkedList.deleteFirst
   peek = LinkedList.first
