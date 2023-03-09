#################################################################
# AVLtree.py
#################################################################
# Source Title: BinarySearchTreeClient.py
# Source Type: Book
# Source Title: Data Structures & Algorithms in Python
# Source Authors: John Canning, Alan Broder, & Robert Lafore
#################################################################
# Additional Methods: .isBalanced(), .__isBalanced()
#################################################################
# Author of additional methods: gametechmatch
# Course: Data Structures
# Programming Project 10.1
#################################################################
# This file implements an AVL tree using tree and node classes.
# These are balanced binary trees.
##################################################################

from LinkStack import *
    
class AVLtree(object):

# To preserve node integrity, node values and children links should
# not be accessible from the caller, so we make the entire
# Node class hidden, but leave its attributes public for ease
# of manipulating them in the Tree class
#########################################################################

   # Class to create a node in an AVL tree
   #####################################################################
   class __Node(object):

      # This constructor initializes a node by taking  a key-value pair
      ##################################################################
      def __init__(self, key, value):
         self.key = key
         self.value = value
         self.left = self.right = None # Empty child links
         self.updateHeight() # Set initial height of node

      # This method updates the height of a node from children
      ##################################################################
      def updateHeight(self):
         # Get maximum child height using 0 for empty child links
         self.height = max(child.height if child else 0
            # Add 1 for this node
            for child in (self.left, self.right)) + 1

      # This method returns the difference in child heights
      ##################################################################
      def heightDiff(self):
         left  = self.left.height  if self.left  else 0
         right = self.right.height if self.right else 0
         return left - right

      # This method creates a string representation of a node using a
      # prefix and its value
      ##################################################################
      def __str__(self):
         return 'AVL>' + str(self.value)
     
   # This constructor initializes an empty AVL tree
   #####################################################################
   def __init__(self):
      self.__root = None # No root node in empty tree

   # This method checks if a tree is empty
   #####################################################################
   def isEmpty(self):
      return self.__root is None

   # This method finds a node that matches a soughtValue value
   #####################################################################
   def __find(self, soughtValue, node):
      while node is not None:
         # If current node's value matches soughtValue, return the node
         if node.value == soughtValue:
            return node
         # Else if soughtValue is below current node, then search left subtree
         elif soughtValue < node.value:
            node = node.left
         # Else search the right subtree
         else:
            node = node.right
      # If the loop ends, soughtValue wasn't found
      return None

   # This method searches for an item whose value matches a soughtValue starting
   # at root.
   #####################################################################
   def search(self, soughtValue):
      node = self.__find(soughtValue, self.__root)
      # Return the node's key, if found
      if node is not None:
         return node.key

   # This method inserts an item into the AVL tree
   #####################################################################
   def insert(self, key, value):
      # Reset the root to be the modified tree
      self.__root, flag = self.__insert(self.__root, key, value)
      # Return the insert vs. update flag
      return flag

   # This method inserts an item into the AVL subtree
   #####################################################################
   def __insert(self, node, key, value):
      # If the subtree is empty, return a new node in the tree
      if node is None:
         return self.__Node(key, value), True

      # If node already has the insert value, then update it with the new
      # key
      if value == node.value:
         node.key = key
         # Return the node and False for flag
         return node, False

      # If the value belongs in the left subtree, insert on the left and
      # update the left link
      elif value < node.value:
         node.left, flag = self.__insert(node.left, key, value)

         # If insert made node left heavy
         if node.heightDiff() > 1:

            # If inside grandchild inserted, then raise grandchild
            if node.left.value < value:
               node.left = self.rotateLeft(node.left)

            # Correct left heavy tree by rotating right around node
            node = self.rotateRight(node)
          
      # Else, value belongs in the right subtree
      else:
         # Insert it on the right and update the right link
         node.right, flag = self.__insert(node.right, key, value)

         # If insert made node right heavy
         if node.heightDiff() < -1:

            # If inside grandchild inserted, then raise grandchild
            if value < node.right.value:
               node.right = self.rotateRight(node.right)

            # Correct right heavy tree by rotating left around this
            # node
            node = self.rotateLeft(node)

      # Update this node's height and return the updated node &
      # insert flag
      node.updateHeight()
      return node, flag

   # This method rotates a subtree to the right
   #####################################################################
   def rotateRight(self, top):
      # The node to raise is top's left child
      toRaise = top.left

      # The raised node's right crosses over to be the left subtree
      # under the old top
      top.left = toRaise.right
      toRaise.right = top

      # Then the heights must be updated
      top.updateHeight()
      toRaise.updateHeight()

      # Return raised node to update parent
      return toRaise

   # This method rotates a subtree to the left
   #####################################################################
   def rotateLeft(self, top):

      # The node to raise is top's right child
      toRaise = top.right

      # The raised node's left crosses over to be the right subtree
      # under the old top
      top.right = toRaise.left
      toRaise.left = top
      top.updateHeight()

      # The heights must be updated
      toRaise.updateHeight()

      # Return raised node to update parent
      return toRaise

   # This method traverses a tree in pre, in, or post order.It is a
   # non-recursive generator
   #####################################################################
   def traverse(self, traverseType='in'):
      # Verify traversal type is an accepted value & raise exception if
      # not
      if traverseType not in ['pre', 'in', 'post']:
         raise ValueError("Unknown traversal type: " + str(traverseType))

      # Create a stack and put root node in stack
      stack = Stack()
      stack.push(self.__root)

      # While there is work in the stack
      while not stack.isEmpty():

         # Get the next item
         item = stack.pop()

         # If it's a tree node
         if isinstance(item, self.__Node):

            # For post-order, put it last
            if traverseType == 'post':
               stack.push((item.key, item.value))

            # Traverse right child
            stack.push(item.right)

            # For in-order, put item 2nd
            if traverseType == 'in':
               stack.push((item.key, item.value))

            # Traverse left child
            stack.push(item.left)

            # For pre-order, put item 1st
            if traverseType == 'pre':
               stack.push((item.key, item.value))

         # Every other non-None item is a (key, value) pair to be
         # yielded
         elif item:
            yield item

   # This method prints a tree sideways with 1 node on each line,
   # indents each level by some blanks, and starts at the root node
   # with no indent
   #####################################################################
   def print(self, indentBy=7):
      self.__pTree(self.__root, "", indentBy)

   # This method recursively prints a subtree, sideways with the root
   # node left justified using indent as prefix for its level.
   # Increase the indent level for subtrees
   #####################################################################
   def __pTree(self, node, indent, indentBy=7):

      # Only print if there is a node
      if node:

         # Print the right subtree
         self.__pTree(node.right, indent + " " * indentBy, indentBy)
         # Print this node, its height, & balance
         print(indent, node, '(',node.height, node.heightDiff(), ')')
         # Print the left subtree
         self.__pTree(node.left, indent + " " * indentBy, indentBy)

   # This method shows the tree in string form as key-value pairs
   # surrounded in curly braces
   #####################################################################
   def __str__(self):
      return '{{{}}}'.format(', '.join('{}: {}'.format(repr(key), repr(value))
                   for key, value in self.traverse('pre')))

   # This method deletes a node whose value matches a given soughtValue
   #####################################################################
   def delete(self, soughtValue):
      # Delete starting at root and update root link
      self.__root, flag = self.__delete(self.__root, soughtValue)
      # Return flag indicating soughtValue node found
      return flag

   # This method deletes a soughtValue value from a subtree rooted at a node &
   # return the modified node.
   #####################################################################
   def __delete(self, node, soughtValue):
      # If subtree is empty, then return None and false
      if node is None:
         return None, False

      # If node to delete is in left subtree, delete from left,
      # update the left link, and store the flag
      if soughtValue < node.value:
         node.left, flag = self.__delete(node.left, soughtValue)

         # Correct any imbalance
         node = self.__balanceLeft(node)

      # If the node to delete is in the right subtree, then delete
      # from the right, update the right link, and store the flag
      elif soughtValue > node.value:   # Is node to delete in right subtree?
         node.right, flag = self.__delete(node.right, soughtValue)

         # Correct any imbalance
         node = self.__balanceRight(node)
            
      # Else node's value matches soughtValue, so determine deletion case
      # If no left child, return right child as remainder, flag
      # deletion
      elif node.left is None:
         return node.right, True
      # If no right child, return left child as remainder,
      # flagging deletion
      elif node.right is None:
         return node.left, True
      # Deleted node has two children so find successor in right
      # subtree and replace this item
      else:
         node.key, node.value, node.right= self.__deleteMin(node.right)

         # Correct any imbalance
         node = self.__balanceRight(node)

         # The soughtValue was found and deleted
         flag = True

      # Update height of node after deletion
      node.updateHeight()
      # Return modified node and delete flag
      return node, flag

   # This method finds the min node of a subtree, deletes it, returns
   # the min value, returns the key value pair and updated link to parent
   #####################################################################
   def __deleteMin(self, node):

      # If left child link is empty, then
      if node.left is None:
         # this node is minimum and its right subtree, if any,
         # replaces it
         return (node.key, node.value, node.right)

      # Else, delete minimum from left subtree
      key, value, node.left = self.__deleteMin(node.left)

      # Correct any imbalance
      node = self.__balanceLeft(node)

      # Update height of node
      node.updateHeight()
      return (key, value, node)

   # This method rebalances after left deletion
   #####################################################################
   def __balanceLeft(self, node):

      # If node is right heavy, then rebalance
      if node.heightDiff() < -1:

         # If the right child is left heavy, then rotate it to the
         # right first
         if node.right.heightDiff() > 0:
            node.right = self.rotateRight(node.right)

         # Correct right heavy tree by rotating left around this node
         node = self.rotateLeft(node)

      # Return top node
      return node

   # This method rebalances after a right deletion
   #####################################################################
   def __balanceRight(self, node):

      # If node is left heavy, then rebalance
      if node.heightDiff() > 1:

         # If the left child is right heavy, then rotate it to the left
         # first
         if node.left.heightDiff() < 0:
            node.left = self.rotateLeft(node.left)

         # Correct left heavy tree by rotating right around this node
         node = self.rotateRight(node)

      # Return top node
      return node

   # This method uses the private __isBalanced() method to check
   # verify that an entire AVL tree is balanced based on height
   #####################################################################
   def isBalanced(self):
      if self.isEmpty():
         return True

      return self.__isBalanced(self.__root)

   # This method recursively goes through an AVL tree and checks that
   # each node is balanced based on height
   #####################################################################
   def __isBalanced(self, node):
      print(f"node: {node}")
      if node:
         print(f"node height difference: {node.heightDiff}")
         if abs(node.heightDiff()) > 1:
            return False

         # Recursively traverse the left subtree
         for childKey, childValue in self.__isBalanced(node.leftChild):
            yield (childKey, childValue)  # yielding its nodes

         # Yield the current node's (subtree's root node) key and value
         yield (node.key, node.value)

         # Recursively traverse right subtree
         for childKey, childValue in self.__isBalanced(node.rightChild):
            yield (childKey, childValue)  # yielding its nodes

      return True
