#################################################################
# BinarySearchTree.py
#################################################################
# Source Title: BinarySearchTree.py
# Source Type: Book
# Source Title: Data Structures & Algorithms in Python
# Source Authors: John Canning, Alan Broder, & Robert Lafore
#################################################################
# Additional Methods: .levelBalance(), .__allUnbalancedNodesByLevels(),
# .nodeBalance(), .__allUnbalancedNodesByNodes(),
# .__balanceCheckTraverse(), .unbalancedNodes()
#################################################################
# Author of Additional Methods: gametechmatch
# Course: Data Structures
# Programming Project 10.1
#################################################################
# Implement binary search trees using Tree and Node classes.
# Nodes contain a key and a value.
#################################################################
from LinkStack import *
class BinarySearchTree(object):

   # Node class
   #################################################################
   class __Node(object):

      # Constructor that initializes a binary search tree node
      #################################################################
      def __init__(self, key, value, left=None, right=None):
         self.key = key
         self.value = value
         self.leftChild = left
         self.rightChild = right

      # This method returns a string representation of a binary search
      # tree node
      #################################################################
      def __str__(self):
         return "{" + str(self.key) + ", " + str(self.value) + "}"

   # This method initializes a binary search tree
   #################################################################
   def __init__(self):
      self.__root = None # Starts as empty

   # This method checks if the binary search tree is empty
   #################################################################
   def isEmpty(self):
      return self.__root is None

   # This method returns a root's key and value if the tree is not
   # empty
   #################################################################
   def root(self):

      # Raise an exception if the tree is empty
      if self.isEmpty():
         raise Exception("No root node in empty tree")

      # Otherwise return the value and key
      return (self.__root.key, self.__root.value)

##################################################################################################
   # This method finds an internal node whose value matches the
   # value sought
   #################################################################
   def __findNodeByValue(self, soughtValue):
      current = self.__root
      parent = self

      # While there is a tree left to explore and current value
      # isn't the goal
      while (current and soughtValue != current.value):
         #print(f"self: {self}")
         #print(f"self.__root: {self.__root}")
         #print(f"current: {current}")
         #print(f"current.value: {current.value}")
         #print(f"soughtValue: {soughtValue}")

         # Prepare to move one level down
         parent = current

         # Advance current to left subtree when goal is less than
         # current value, else right
         current = (current.leftChild if soughtValue < current.value else
            current.rightChild)
               
      # If the loop ended on a node, it must have the goal value
      # Return the node or None and parent
      return (current, parent)

   # This method searches for a given value
   #################################################################
   def search(self, soughtValue):
      node, parent = self.__findNodeByValue(soughtValue)
      return node.key if node else None

##################################################################################################
   # Insert a new node in a binary search tree
   #################################################################
   def insert(self, key, value):

      # Find the parent node
      node, parent = self.__findNodeByValue(value)

      # If we find a node the same value, then return False to
      # show that nothing was inserted
      if node:
         node.key = key
         return False

      # If the tree is empty, insert a new node at the root of the
      # tree
      if parent is self:
         self.__root = self.__Node(key, value)

      # Else if the new value is less than the parent node's value,
      # insert the new value (now new node) as a left child of the
      # parent
      elif value < parent.value:
         parent.leftChild = self.__Node(key, value, right=node)

      # Else, insert the new value (now new node) as right child
      # of parent node
      else:
         parent.rightChild = self.__Node(key, value, right=node)

      # Return true to confirm that value was inserted
      return True

   # This method visit all nodes of the tree in-order and prints each
   #################################################################
   def inOrderTraverse(self, function=print):

      # Call recursive version starting at root node
      self.__inOrderTraverse(self.__root, function=function)

   # Visit a subtree in-order, recursively The subtree's root is node
   #################################################################
   def __inOrderTraverse(self, node, function):
      if node:

         # Traverse the left subtree
         self.__inOrderTraverse(node.leftChild, function)
         function(node)

         # Traverse the right subtree
         self.__inOrderTraverse(node.rightChild, function)

   # Traverse the tree recursively in pre, in, or post order
   #################################################################
   def traverse_rec(self,traverseType="in"):

      # Use a generator to walk the tree yielding values and indicies
      # starting at the root
      if traverseType in ['pre', 'in', 'post']:
         return self.__traverse(self.__root, traverseType)
      
      raise ValueError("Unknown traversal type: " + str(traverseType))

   # This method is a recursive generator that traverses a subtree
   # rooted at node in pre, in, or post order
   #################################################################
   def __traverse(self, node, traverseType):

      # If subtree is empty, traversal is done
      if node is None:
         return

      # If pre-order, yield the current node before all the others
      if traverseType == "pre":
         yield (node.key, node.value)

      # Recursively traverse the left subtree
      for childKey, childValue in self.__traverse(node.leftChild, traverseType):
         yield (childKey, childValue)       # yielding its nodes

      # If in-order, yield the current node
      if traverseType == "in":
         yield (node.key, node.value)

      # Recursively traverse right subtree
      for childKey, childValue in self.__traverse(node.rightChild, traverseType):
         yield (childKey, childValue)        # yielding its nodes

      # If post-order, yield the current node after all the others
      if traverseType == "post":
         yield (node.key, node.value)

   # This method is a non-recursive generator that traverses the tree
   # in pre, in, or post order (default is in-order)
   #################################################################
   def traverse(self, traverseType='in'):

      # Verify traversal type is an accepted value
      if traverseType not in ['pre', 'in', 'post']:
         raise ValueError("Unknown traversal type: " + str(traverseType))

      # Create a stack and put the root node in the stack
      stack = Stack()
      stack.push(self.__root)

      # While the stack isn't empty, get the next item.
      while not stack.isEmpty():
         item = stack.pop()

         # If it is a tree node, put it in its proper location based
         # on the traversal type
         if isinstance(item, self.__Node): # If it's a tree node

            # For post-order, put it last
            if traverseType == 'post':
               stack.push((item.key, item.value))

            # Traverse right child
            stack.push(item.rightChild)

            # For pre-order, put item 2nd
            if traverseType == 'in':
               stack.push((item.key, item.value))

            # Traverse left child
            stack.push(item.leftChild)

            # For pre-order, put item 1st
            if traverseType == 'pre':
               stack.push((item.key, item.value))

         # Every other non-None item has its value and key
         # yielded
         elif item:
            yield item

   # This method finds the leftmost node and returns its value and key
   #################################################################
   def minNode(self):

      # If the tree is empty, raise exception
      if self.isEmpty():
         raise Exception("No minimum node in empty tree")

      # Else, start at root, and keep following the left child node
      # until it reaches the end
      node = self.__root
      while node.leftChild:
         node = node.leftChild

      # return the value and key
      return (node.key, node.value)

   # This method finds the rightmost node, and returns its value
   # and key
   #################################################################
   def maxNode(self):         # Find and return node with maximum value

      # If the tree is empty, raise exception
      if self.isEmpty():
         raise Exception("No maximum node in empty tree")

      # Else, start at the root, and keep following the right child
      # node until it reaches the end
      node = self.__root
      while node.rightChild:
         node = node.rightChild

      # return the value and key
      return (node.key, node.value)

   # This method counts the number of levels in the tree starting
   # at the root
   #################################################################
   def levels(self):
      return self.__levels(self.__root)

   # This method recursively counts the levels in a subtree
   #################################################################
   def __levels(self, node):
      if node:
         return 1 + max(self.__levels(node.leftChild),self.__levels(node.rightChild))

      # Empty subtree has no levels
      else: return 0

   # This method counts the tree nodes recursively starting at the
   # root
   #################################################################
   def nodes_rec(self):
      return self.__nodes(self.__root)

   # This method recursively counts nodes in a subtree
   #################################################################
   def __nodes(self, node):
      if node:
         return (1 + self.__nodes(node.leftChild) + self.__nodes(node.rightChild))

      # Empty subtree has no nodes
      else: return 0

   # This method returns the number of tree nodes in a binary search
   # tree using an iterator
   #################################################################
   def totalNodes(self):
      count = 0
      for key, value in self.traverse():
         count += 1
      return count

   # This method prints the binary search tree sideways with 1 node
   # on each line and indenting each level
   #################################################################
   def print(self,indentBy=4):

      # by some blanks.  Start at root node with no indent
      self.__pTree(self.__root,"ROOT:   ", "", indentBy)

   # This method recursively prints a subtree sideways with the root
   # node left justified. The nodeType shows the relation to its parent
   # and the indent shows its level
   #################################################################
   def __pTree(self,node,nodeType,indent,indentBy=4):

      # Only print if there is a node
      if node:

         # Print the right subtree
         self.__pTree(node.rightChild, "RIGHT:  ",indent + " " * indentBy, indentBy)
         print(indent + nodeType, node) # Print this node

         # Print the left subtree
         self.__pTree(node.leftChild,  "LEFT:   ",indent + " " * indentBy, indentBy)

##################################################################################################
   # This method deletes a node containing the value sought
   #################################################################
   def delete(self, goal):

      # Find the node, and its parent
      node, parent = self.__findNodeByValue(goal)

      # If node was found then perform deletion at node under the parent
      if node is not None:
         return self.__delete(parent, node)

      # Else return None for no deletion
      return

   # This method deletes the specified node in the tree modifying
   # the parent node/tree
   #################################################################
   def __delete(self, parent, node):
      deleted = node.key

      # Determine number of subtrees
      if node.leftChild:

         # If both subtrees exist, then promote successor to replace
         # deleted node
         if node.rightChild:
            self.__promote_successor(node)

         # If no right child, move left child up
         else:
            # If parent is the whole tree, update root
            if parent is self:
               self.__root = node.leftChild

            # If node is parent's left child, update left
            elif parent.leftChild is node:
               parent.leftChild = node.leftChild

            # If node is parent's right child, update right
            else:
               parent.rightChild = node.leftChild

      # No left child; so promote right child
      else:

         # If parent is the whole tree, update root
         if parent is self:
            self.__root = node.rightChild

         # If node is parent's left child, update left
         elif parent.leftChild is node:
            parent.leftChild = node.rightChild

         # If node is parent's right child, update right
         else:
            parent.rightChild = node.rightChild

      # Return the deleted node's key
      return deleted

   # When deleting a node with both subtrees, this method finds
   # the  successor on the right subtree, puts its value in this
   # node, and deletes the successor from the right subtree
   #################################################################
   def __promote_successor(self, node):

      # Start search for successor in right subtree and track its parent
      successor = node.rightChild
      parent = node

      # Descend left child links until no more left links, tracking parent
      while successor.leftChild:
         parent = successor
         successor = successor.leftChild

      # Replace node to delete with successor's value and key
      node.value = successor.value
      node.key = successor.key

      # Remove successor node
      self.__delete(parent, successor)

   # This method computes the number of levels in the right subtree minus
   # the number of levels in the left subtree
   #################################################################
   def levelBalance(self):
      # check if binary tree is empty
      if self.isEmpty():
         return 0

      # set up variables to keep track of each child node of the root
      leftChildNode = self.__root.leftChild
      rightChildNode = self.__root.rightChild

      # count the number of levels on each side of the root, calculate
      # the difference, and return the result
      totalLeftLevels = self.__levels(leftChildNode)
      totalRightLevels = self.__levels(rightChildNode)
      differenceInRightAndLeftLevels = totalRightLevels - totalLeftLevels
      return differenceInRightAndLeftLevels

   # This method computes all nodes with an unbalanced number of levels
   # on the right and left side that exceeds the threshold given (default 1)
   #################################################################
   def __allUnbalancedNodesByLevels(self, by):
      # check if binary tree is empty
      if self.isEmpty():
         return 0

      # Create Stack to hold nodes with unbalanced levels
      stackOfNodesWithUnbalancedLevels = Stack()

      # Traverse through all nodes checking if their levels are balanced
      for key, value in self.__balanceCheckTraverse(self.__root):
         currentNode, parentNode = self.__findNodeByValue(value)

         # set up variables to keep track of each child node of the root
         leftChildNode = currentNode.leftChild
         rightChildNode = currentNode.rightChild

         # count the number of levels on each side of the node and
         # calculate the absolute value of the difference
         totalLeftLevels = self.__levels(leftChildNode)
         totalRightLevels = self.__levels(rightChildNode)
         differenceInLevels = abs(totalRightLevels - totalLeftLevels)

         # If the difference of left and right levels exceeds our
         # given limit (by), add node to stack tracking all nodes with
         # unbalanced left and right levels
         if differenceInLevels > by:
            stackOfNodesWithUnbalancedLevels.push(currentNode)

      # Return the stack nodes with unbalanced nodes after checking all nodes
      return stackOfNodesWithUnbalancedLevels

   # This method computes the number of nodes in the right subtree minus
   # the number of nodes in the left subtree
   #################################################################
   def nodeBalance(self):

      # check if binary tree is empty
      if self.isEmpty():
         return 0

      # set up variables to keep track of each child node of the root
      leftChildNode = self.__root.leftChild
      rightChildNode = self.__root.rightChild

      # count the number of nodes on each side of the root, calculate
      # the difference, and return the result
      totalLeftNodes = self.__nodes(leftChildNode)
      totalRightNodes = self.__nodes(rightChildNode)
      differenceInRightAndLeftNodes = totalRightNodes - totalLeftNodes
      return differenceInRightAndLeftNodes

   # This method computes all nodes with an unbalanced number of nodes
   # on the right and left side that exceeds the threshold given (default 1)
   #################################################################
   def __allUnbalancedNodesByNodes(self, by):

      # check if binary tree is empty
      if self.isEmpty():
         return 0

      # Create Stack to hold nodes with unbalanced nodes
      stackOfNodesWithUnbalancedNodes = Stack()

      # Find any unbalanced nodes and use the .__balanceCheckTraverse()
      # method to recursively traverse through the tree
      for key, value in self.__balanceCheckTraverse(self.__root):
         currentNode, parentNode = self.__findNodeByValue(value)

         # set up variables to keep track of each child node of the root
         leftChildNode = currentNode.leftChild
         rightChildNode = currentNode.rightChild

         #count the number of nodes on each side of the root and
         # calculate the absolute value of the difference
         totalLeftNodes = self.__nodes(leftChildNode)
         totalRightNodes = self.__nodes(rightChildNode)
         nodesNodeBalance = abs(totalRightNodes - totalLeftNodes)

         # If the difference of left and right nodes exceeds our
         # given limit (by), add root node to stack tracking all nodes with
         # unbalanced left and right nodes
         if nodesNodeBalance > by:
            stackOfNodesWithUnbalancedNodes.push(currentNode)

      # Return the stack of unbalanced nodes after checking all nodes
      return stackOfNodesWithUnbalancedNodes

   # This method recursively traverses a binary search tree with in-order
   # traversal
   #################################################################
   def __balanceCheckTraverse(self, node):
      # If subtree is empty, traversal is done
      if node is None:
         return

      if node:
         # Recursively traverse the left subtree
         for childKey, childValue in self.__balanceCheckTraverse(node.leftChild):
            yield (childKey, childValue)  # yielding its nodes

         # Yield the current node's (subtree's root node) key and value
         yield (node.key, node.value)

         # Recursively traverse right subtree
         for childKey, childValue in self.__balanceCheckTraverse(node.rightChild):
            yield (childKey, childValue)  # yielding its nodes

   # This method returns a list of nodes that are unbalanced based
   # off of their nodes and nodes that are unbalanced based off of their
   # levels
   #################################################################
   def unbalancedNodes(self, by=1):

      # Check which nodes have unbalanced levels and print their key/value
      # pairs
      stackOfNodesWithUnbalancedLevels = self.__allUnbalancedNodesByLevels(by)
      print("Nodes with unbalanced levels: ")
      stackOfNodesWithUnbalancedLevels.traverse()

      # Check which nodes have unbalanced nodes and print their key/value
      # pairs
      stackOfNodesWithUnbalancedNodes = self.__allUnbalancedNodesByNodes(by)
      print("Nodes with unbalanced nodes: ")
      stackOfNodesWithUnbalancedNodes.traverse()


   def balanceTrueOrFalse(self, by=1):
      # Check which nodes have unbalanced levels and print their key/value
      # pairs
      stackOfNodesWithUnbalancedLevels = self.__allUnbalancedNodesByLevels(by)
      if stackOfNodesWithUnbalancedLevels.isEmpty():
         return True

      return False
