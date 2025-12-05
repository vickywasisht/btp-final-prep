class BST:
	class Node:
		def __init__(self, value=None, left=None, right=None):
			self.value = value
			self.left = left
			self.right = right

	# BST's init function
	def __init__(self):
		self.root = None
		
	def insert(self, value):
		"""Helper method to insert values into BST for testing"""
		if self.root is None:
			self.root = self.Node(value)
		else:
			self._insert_helper(self.root, value)
	
	def _insert_helper(self, node, value):
		if value < node.value:
			if node.left is None:
				node.left = self.Node(value)
			else:
				self._insert_helper(node.left, value)
		elif value > node.value:  # Only insert if value is greater, ignore duplicates
			if node.right is None:
				node.right = self.Node(value)
			else:
				self._insert_helper(node.right, value)
		# If value == node.value, do nothing (ignore duplicates)
		
	'''
	This function prints every value in the tree that is between min and max inclusive. 
	Function only visits a subtree where the values may be valid.
	'''
	def print_between(self, min, max): 
		result = []
		self._print_between_helper(self.root, min, max, result)
		return result  # Return list for testing purposes
	
	def _print_between_helper(self, node, min_val, max_val, result):
		if node is None:
			return
		
		# Only explore left subtree if current value is greater than min
		if node.value > min_val:
			self._print_between_helper(node.left, min_val, max_val, result)
		
		# Add current node if it's in range
		if min_val <= node.value <= max_val:
			result.append(node.value)
		
		# Only explore right subtree if current value is less than max
		if node.value < max_val:
			self._print_between_helper(node.right, min_val, max_val, result)
	
	# This function returns the height of the binary tree.
	def height(self):
		return self._height_helper(self.root)
	
	def _height_helper(self, node):
		if node is None:
			return 0
		return 1 + max(self._height_helper(node.left), self._height_helper(node.right))
	
	'''
	This method returns the inorder successor of value. 
	If there are no nodes with this value in the BST, 
	or the node containing this value does not have an inorder succesor, 
	this method should return None.
	'''
	def inorder_successor(self, value):
		# First find the node with the given value
		node = self._find_node(self.root, value)
		if node is None:
			return None
		
		# Case 1: Node has right subtree
		if node.right is not None:
			return self._find_min(node.right).value
		
		# Case 2: Node has no right subtree
		# Find the deepest ancestor for which given node is in left subtree
		successor = None
		current = self.root
		
		while current is not None:
			if value < current.value:
				successor = current
				current = current.left
			elif value > current.value:
				current = current.right
			else:
				break
		
		return successor.value if successor else None
	
	def _find_node(self, node, value):
		if node is None or node.value == value:
			return node
		if value < node.value:
			return self._find_node(node.left, value)
		return self._find_node(node.right, value)
	
	def _find_min(self, node):
		while node.left is not None:
			node = node.left
		return node