import heapq

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
		def _print_between(node, min, max):
			if node is None:
				return
			else:
				_print_between(node.left, min, max)
				if node.value <= max and node.value >= min:
					print(node.value)
				_print_between(node.right, min, max)

	# This function returns the height of the binary tree.
	def height(self):
		def height_help(node):
			if node is None:
				return -1
			else:
				left = 1 + height_help(node.left)
				right = 1 + height_help(node.right)
				return max(left, right)
		
		return height_help(self.root)
			
	'''
	This method returns the inorder successor of value. 
	If there are no nodes with this value in the BST, 
	or the node containing this value does not have an inorder succesor, 
	this method should return None.
	'''
	def inorder_successor(self, value):
		pass