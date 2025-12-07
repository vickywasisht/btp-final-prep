# Binary Search Tree (BST) class with methods to implement
class BST:
	class Node:
		def __init__(self, value=None, left=None, right=None):
			self.value = value
			self.left = left
			self.right = right

	# BST's init function
	def __init__(self):
		self.root = None
		
	'''
	This function prints every value in the tree that is between min and max inclusive. 
	Function only visits a subtree where the values may be valid.
	'''
	def print_between(self, min, max): 
		pass
	
	# This function returns the height of the binary tree.
	def height(self):
		pass
	
	'''
	This method returns the inorder successor of value. 
	If there are no nodes with this value in the BST, 
	or the node containing this value does not have an inorder succesor, 
	this method should return None.
	'''
	def inorder_successor(self, value):
		pass
