#################################################################
# AVLtreeClient.py
#################################################################
# Author: gametechmatch
# Course: Data Structures
# Programming Project 10.1
#################################################################
# Source Title: BinarySearchTreeClient.py
# Source Type: Book
# Source Title: Data Structures & Algorithms in Python
# Source Authors: John Canning, Alan Broder, & Robert Lafore
#################################################################
# This program uses different methods in the AVLtree class,
# tracks if the AVLtree is balanced at each change, and
# shows the balanced difference of a binary search tree and
# AVL tree of the permutations of the same list of 6 elements
#################################################################

from BinarySearchTree import *
from AVLtree import *
import sys
import itertools

def main():
   print("#########################################################################")
   print("############################### AVL TREE ################################")
   print("#########################################################################")
   # Create an AVL tree and the values that will be inserted
   myAVLtree = AVLtree()
   values = [10000001, 20000002, 30000003, 40000004, 50000005, 60000006, 70000007]

   # check balance
   print("Check balance of empty tree before adding values:")
   checkBalance(myAVLtree)

   # insert values into tree
   insertIntoAVLTree(myAVLtree, values)

   # traverse the tree
   traverseAVLTree(myAVLtree)

   # delete values from the tree
   deleteAllFromAVLTree(myAVLtree, values)

   print("Check balance of empty tree after removing values:")
   checkBalance(myAVLtree)

   # Find all the permutations of a list and turn it into a 2D list
   # The permutationList will be used to test binary search trees
   # and AVL trees
   moreValues = [1, 2, 3, 4, 5, 6]
   permutationsOfMoreValues = permutations(moreValues)
   permutationList = list(permutationsOfMoreValues)

   print("#########################################################################")
   print("################ PERMUTATIONS OF A BINARY SEARCH TREE ###################")
   print("#########################################################################")
   # Check each permutation if it would create a balanced binary search tree based
   # on the difference in levels for each node
   currentTree = BinarySearchTree()
   allBalancedOptions = []
   finalInsertIndex = 0

   # check each permutation
   for item in permutationList:
      treeInsertIndex = 0

      # fill a tree with all the values in the current permutation
      for i in item:
         currentTree.insert(treeInsertIndex, i)
         treeInsertIndex += 1

      # insert the permutation in the list of balanced permutations if it creates
      # a balanced binary search tree
      if currentTree.balanceTrueOrFalse():
         allBalancedOptions.insert(finalInsertIndex, item)
         finalInsertIndex +=1

      # Clear the binary search tree to check the next permutation
      for i in item:
         currentTree.delete(i)

   # print all permutations that would yield a balanced binary search tree
   print("All permutations that would yield a balanced Binary Search Tree:")
   for i in allBalancedOptions:
      print(i)

   # print the number of permutations that would yield a balanced binary
   # search tree
   print(f"Total Balanced Binary Search Tree Permutations: {len(allBalancedOptions)}")
   print(f"Total Permutations in all: {len(permutationList)}")

   print("#########################################################################")
   print("#################### PERMUTATIONS OF AN AVL TREE ########################")
   print("#########################################################################")
   # Check each permutation if it would create an unbalanced AVL tree based
   # on the difference in levels for each node
   testAVLtree = AVLtree()
   allUnbalancedOptions = []
   finalInsertIndex = 0

   # check each permutation
   for item in permutationList:
      treeInsertIndex = 0

      # fill AVL tree with all the values in the current permutation
      for i in item:
         testAVLtree.insert(treeInsertIndex, i)
         treeInsertIndex += 1

      # insert the permutation in the list of unbalanced permutations if it creates
      # an unbalanced AVL tree
      if not testAVLtree.isBalanced():
         allUnbalancedOptions.insert(finalInsertIndex, item)
         finalInsertIndex += 1

      # Clear the AVL tree to check the next permutation
      for i in item:
         testAVLtree.delete(i)

   # print all permutations that would yield an unbalanced AVL tree
   print("All permutations that would not yield a balanced AVL tree:")
   for i in allUnbalancedOptions:
      print(i)

   # print the number of permutations that would yield an unbalanced AVL
   # tree
   print(f"Total Unbalanced AVL Tree Permutations: {len(allUnbalancedOptions)}")
   print(f"Total Permutations in all: {len(permutationList)}")

# This function returns all the permutations of a given list
#########################################################################
def permutations(inputList):
   return itertools.permutations(inputList, len(inputList))

# This function inserts a list of values into an AVL tree
#########################################################################
def insertIntoAVLTree(tree, values):
   print("\n###############################INSERTING###############################")

   # Use command line args if present
   if len(sys.argv) > 1:
      values = [int(a) for a in sys.argv[1:]]

   # insert into the tree
   key = 0
   for value in values:
      print('\nInserting', value, 'returns', tree.insert(key, value))
      key += 1
      print('After inserting', key, ':', value,
            'the tree contains\n')
      tree.print()
      checkBalance(tree)

   return tree

# This function traverses through an AVL tree
#########################################################################
def traverseAVLTree(tree):
   print("\n###############################TRAVERSING###############################")
   print('Traversing the tree in-order:')

   # insert the values
   for key, value in tree.traverse('in'):
      print('key', key, 'has value', value)

      # Check if the tree is balanced at each insertion
      print("Balance Check:")
      checkBalance(tree)

# This function deletes all values from an AVL tree
#########################################################################
def deleteAllFromAVLTree(tree, values):
   print("\n###############################DELETING###############################")
   for value in values:

      # Check the balance of the tree at the start of each deletion
      checkBalance(tree)

      # delete the current value
      delFlag = tree.delete(value)
      print('\nDeleting', value, 'returns', delFlag)

      if delFlag:
         print('After deleting', value, ':',
               'the tree contains\n')
         tree.print()

   return tree

# This function checks if an AVL tree is balanced
#########################################################################
def checkBalance(tree):
   if tree.isBalanced():
      print("The tree is balanced")
   else:
      print("Not balanced")

# execute main function
if __name__ == '__main__':
	main()
