import heapq

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
		def min(node):
			curr = node
			while curr.left is not None:
				curr = curr.left
			return curr
		
		def find_successor(node, value):
			if node is None:
				return None
			else:
				if node.value > value:
					left = find_successor(node.left, value)
					return left if left is not None else node
				elif node.value < value:
					return find_successor(node.right, value)
				else:
					if node.right is not None:
						return min(node.right)
					return None
		return find_successor(self.root, value)

	def preorder_sucessor(self, value):
		curr = self.root
		#find node
		while curr is not None and curr.value != value:
			if value < curr.value:
				curr = curr.left
			else:
				curr = curr.right
		#if node was found return preorder sucessor
		if curr is None:
			return None
		if curr.left is not None:
			return curr.left.value
		elif curr.right is not None:
			return curr.right.value
	
	def postorder_sucessor(self, value):
		def min(node):
			curr = node
			while curr.left is not None:
				curr = curr.left
			return curr
		
		parent = None
		curr = self.root
		#find node
		while curr is not None and curr.value != value:
			if value < curr.value:
				parent = curr
				curr = curr.left
			else:
				parent = curr
				curr = curr.right
		#if node was found return postorder sucessor
		if curr is None:
			return None
		if parent is None:
			return min(self.root.right).value
		else:
			if parent.right == curr or parent.right is None:
				return parent.value
			else:
				return min(parent.right).value
		
	
	def breadthwidth_successor(self, value):
		if self.root is None:
			return None

		queue = [self.root]
		found = False

		while queue:
			node = queue.pop(0)

			if found:
				return node.value
			if node.value == value:
				found = True

			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

		return None