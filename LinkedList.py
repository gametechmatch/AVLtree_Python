#################################################################
# LinkedList.py
#################################################################
# Source Title: LinkedList.py
# Source Type: Book
# Source Title: Data Structures & Algorithms in Python
# Source Authors: John Canning, Alan Broder, & Robert Lafore
#################################################################
# Course: Data Structures
# Programming Project 10.1
#################################################################
# Implement a singly linked list class
# The link stack file imports from this one
#################################################################
from Link import *

# A class to make a new linked list comprised of nodes created in
# the Link class
#################################################################
class LinkedList(object):

   # This constructor initializes a linked list
   #################################################################
   def __init__(self):
      self.__first = None  # Reference to first Link

   # This method returns the first link in the linked list
   #################################################################
   def getFirst(self):
      return self.__first

   # This method changes the first link in a linked list to a new link
   #################################################################
   def setFirst(self, link):
      if link is None or isinstance(link, Link):
         self.__first = link
      else:
         raise Exception("First link must be Link or None")

   # This method makes the first link next (so it follows the last in
   # first out ordering)
   #################################################################
   def getNext(self):
      return self.getFirst()

   # This method sets the first link as next (so it follows the last in
   # first out ordering)
   #################################################################
   def setNext(self, link):
      self.setFirst(link)

   # This method tests for an empty list and returns true if there
   # is no 1st link (aka if self.getFirst() returns None)
   #################################################################
   def isEmpty(self):
      return self.getFirst() is None

   # This method returns the first data item in the list as long as
   # the node is not empty
   #################################################################
   def first(self):
      if self.isEmpty():
         raise Exception("No first item in empty list")
      return self.getFirst().getData()

   # This method applies a function to all items in list with the
   # default function being to print
   #################################################################
   def traverse(self, func=print):
      link = self.getFirst()
      while link is not None:
         func(link.getData())
         link = link.getNext()

   # This method gets the length (number of nodes/links) of the linked
   # list
   #################################################################
   def __len__(self):
      l = 0
      link = self.getFirst()
      while link is not None:
         l += 1
         link = link.getNext()
      return l

   # This method builds a string representation of the linked list
   #################################################################
   def __str__(self):
      result = "["
      link = self.getFirst()
      while link is not None:
         if len(result) > 1:
            result += " > "
         result += str(link)
         link = link.getNext()
      return result + "]"

   # This method inserts a new node (aka initializes a new link and
   # then sets it as the first node/link in the linked list)
   #################################################################
   def insert(self, datum):
      link = Link(datum, self.getFirst())
      self.setFirst(link)

   # This method fins the 1st link whose reference variable (self.__next())
   # holds the reference we are searching for
   #################################################################
   def find(self, soughtValue, key):
      link = self.getFirst()
      while link is not None:
         if key(link.getData()) == soughtValue:
            return link
         link = link.getNext()

   # This method finds the 1st item whose value matches what we are
   # looking for
   #################################################################
   def search(self, soughtValue, key):
      link = self.find(soughtValue, key)
      if link is not None:
         return link.getData()

   # This method inserts a new node/link after the first node/link
   # with a matching reference variable (self.__next())
   #################################################################
   def insertAfter(self, soughtValue, newDatum, key):
      link = self.find(soughtValue, key)

      # If matching reference variable not found, return False
      if link is None:
         return False

      # Else create a new link node value the new value and insert it
      # after the link with the matching reference variable
      newLink = Link(newDatum, link.getNext())
      link.setNext(newLink)
      return True

   # This method deletes the first link in the linked list or raises
   # an exception if the linked list is empty
   #################################################################
   def deleteFirst(self):

      # Raise an exception if the linked list is empty
      if self.isEmpty():
         raise Exception("Cannot delete first of empty list")

      # Else store (in "first") the value held in the first link,
      # remove the link from the linked list, and return the value
      # stored
      first = self.getFirst()
      self.setFirst(first.getNext())
      return first.getData()

   # Delete the first Link from the list that is holding the value
   # or data we are searching for
   #################################################################
   def delete(self, soughtValue, key):

      # Raise an exception if the linked list is empty
      if self.isEmpty():
         raise Exception("Cannot delete from empty linked list")

      previous = self
      while previous.getNext() is not None:
         link = previous.getNext()

         # If the next link is holding the value sought after,
         # change the previous' next to be Link's next and
         # return the value found
         if soughtValue == key(link.getData()):
            previous.setNext(link.getNext())
            return link.getData()

         # Advance previous to next Link
         previous = link

      # Raise an exception if loop ended without finding a value
      raise Exception("No item with matching key found in list")
