#################################################################
# Link.py
#################################################################
# Source Title: LinkedList.py
# Source Type: Book
# Source Title: Data Structures & Algorithms in Python
# Source Authors: John Canning, Alan Broder, & Robert Lafore
#################################################################
# Course: Data Structures
# Programming Project 10.1
#################################################################
# A class for each link
#################################################################
class Link(object):

   # Constructor that initializes a single link along with the data
   # and reference portions of each link
   #################################################################
   def __init__(self, linkValue, referenceNext=None):
      self.__linkValue = linkValue
      self.__referenceNext = referenceNext

   # This method returns the data stored in a link
   #################################################################
   def getData(self):
      return self.__linkValue

   # This method sets or updates the data in a link
   #################################################################
   def setData(self, linkValue):
      self.__linkValue = linkValue

   # This method returns the next link
   #################################################################
   def getNext(self): return self.__referenceNext

   # This method changes the next link to a new link
   #################################################################
   def setNext(self, link):

      # Set next link if 'link' or 'None'
      if link is None or isinstance(link, Link):
         self.__referenceNext = link

      # Else raise exception
      else:
         raise Exception("Next link must be Link or None")

   # This method tests if the link currently selected is the last
   # by returning true if there is no next link (aka its self.__next
   # attribute (its reference attribute) in the chain equals "None")
   #################################################################
   def isLast(self):
      return self.getNext() is None

   # This method makes a string representation of a link
   #################################################################
   def __str__(self):
      return str(self.getData())
