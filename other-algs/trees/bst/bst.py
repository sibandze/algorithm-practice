from util import BSTNode

class BST:
	def __init__(self, key_extractor = None, comparator = None):
		'''
			Initializes an empty BST.
			 Args:
				key_extractor:  A function that takes data and returns its key.
						Defaults to identity function (data is the key).
				comparator: 	A function that compares two keys and returns -1, 0, or 1.
						Defaults to standard comparison.
		'''

		self.root = None
		self.key_extractor = key_extractor or (lambda x: x)
		self.comparator = comparator or (lambda a, b: (a>b) - (a<b))

		if not callable(self.key_extractor):
			raise TypeError("key_extractor must be a callable function")
		if not callable(self.comparator):
			raise TypeError("comparator must be a callable function")

	@staticmethod
	def build(iterable, key_extractor = None, comparator = None):
		'''
			Factory method to initialize a BST from an iterable.
			Args:
				iterable: 	An iterable (list, tuple, etc.) of data items.
				key_extractor:  A function that takes data and returns its key.
						Defaults to identity function (data is the key).
				comparator:     A function that compares two keys and returns -1, 0, or 1.
						Defaults to standard comparison.
			Returns:
				A BST populated with data from iterable.
		'''

		if not hasattr(iterable, '__iter__'):
			raise TypeError("iterable must be an iterable")

		# Initialize BST
		new_bst = BST(key_extractor = key_extractor, comparator = comparator)

		# Populate binary tree with data from iterable.
		for item in iterable:
			new_bst.insert(item)

		return new_bst

	def insert(self, data):
		'''
			Insert data into tree
		'''
		if not self.root:
			self.root = BSTNode(data)
		else:
			key = self.key_extractor(data)
			self._insert_recursively(self.root, data, key)

	def _insert_recursively(self, current_node, data, key):
		'''
		'''
		current_key = self.key_extractor(current_node.data)
		comparator_result = self.comparator(key, current_key)

		if comparator_result == 0:
			print(f"The key `{key}`	already exists in tree. Handling duplicates.")
			current_node.data = data
		elif comparator_result > 0:
			if not current_node.right:
				current_node.right = BSTNode(data)
			else:
				self._insert_recursively(current_node.right, data, key)
		else:
			if not current_node.left:
				current_node.left = BSTNode(data)
			else:
				self._insert_recursively(current_node.left, data, key)
