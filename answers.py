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
	def print_between(self, node, min, max): 
		def _print_between(node, min, max):
			if node is None:
				return
			else:
				self.print_between(node.left, min, max)
				if node.value >= min and node <= max:
					print(str(node) + ", ")
				self.print_between(node.right, min, max)
		
		_print_between(node, min, max)

	# This function returns the height of the binary tree.
	def height(self):
		return self.height_help(self.root)
	
	def height_help(self, node):
		if node is None:
			return -1
		left_height = self.height_help(node.left)
		right_height = self.height_help(node.right)
		return 1 + max(left_height, right_height)

	'''
	This method returns the inorder successor of value. 
	If there are no nodes with this value in the BST, 
	or the node containing this value does not have an inorder succesor, 
	this method should return None.
	'''
	def inorder_successor(self, value):
		def find_min(node):
			current = node
			while current.left is not None:
				current = current.left
			return current

		def find_successor(node, value):
			if node is None:
				return None

			if value < node.value:
				left = find_successor(node.left, value)
				return left if left is not None else node
			elif value > node.value:
				return find_successor(node.right, value)
			else:
				if node.right is not None:
					return find_min(node.right)
				return None

		return find_successor(self.root, value)