from collections import deque
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
			self.root = BSTNode(data, self.key_extractor)
		else:
			key = self.key_extractor(data)
			self._insert_recursively(self.root, data, key)

	def _insert_recursively(self, current_node, data, key):
		'''
		'''
		current_key = self.key_extractor(current_node.key)
		comparator_result = self.comparator(key, current_key)

		if comparator_result == 0:
			#print(f"The key `{key}`	already exists in tree. Handling duplicates.")
			current_node.insert(data, self.key_extractor, self.comparator)
		elif comparator_result > 0:
			if not current_node.right:
				current_node.right = BSTNode(data, self.key_extractor)
			else:
				self._insert_recursively(current_node.right, data, key)
		else:
			if not current_node.left:
				current_node.left = BSTNode(data, self.key_extractor)
			else:
				self._insert_recursively(current_node.left, data, key)

	def find(self, key):
		if not self.root:
			return None
		return self._find(self.root, key)

	def find_min(self, node = None):
		return self._find_min(node or self.root)

	def find_max(self, node = None):
		return self._find_max(node or self.root)

	def find_min_data(self, node = None):
		min_node = self.find_min(node)
		if not min_node:
			return None
		return min_node.data_store[0][0]

	def find_max_data(self, node = None):
                max_node = self.find_max(node)
                if not max_node:
                        return None
                return max_node.data_store[-1][0]

	def _find_max(self, node = None):
		if not node:
			return None
		while node.right:
			node = node.right
		return  node

	def _find_min(self, node):
		if not node:
			return None
		while node.left:
			node = node.left
		return node

	def _find(self, node, key):
		if not node:
			return None

		comparator_result = self.comparator(key, node.key)
		if comparator_result == 0:
			return node
		elif comparator_result > 0:
			return self._find(node.right, key)
		return self._find(node.left, key)

	def contains_key(self, key):
		return self.find(key) != None

	def  get_data(self, key):
		node = self.find(key)
		if not node:
			return None
		data_list = []
		for data, count in node.data_store:
			for _ in range(count):
				data_list.append(data)
		return data_list

	def find_next(self, key):
		if self.root:
			return self._find_next(self.root, key)
		return None

	def find_prev(self, key):
		if self.root:
                        return self._find_prev(self.root, key)
		return None

	def find_nth(self, n):
		if self.root:
                        return self._find_nth(self.root, n)
		return None
	'''
	def delete(self, key = None, data = None):
		if not (key or data):
			raise Exception("One between `key` or `data` should be assigned a value.")
		if (key and data) and  self.comparator(key_extractor(data), key) != 0:
			raise Exception("`key: {key} and data_key: {key_extractor(data)} should match;")
		if self.root:
                        return self._delete(self.root, key, data)
		return None

	def _delete(self, node, key, data):
		pass

	def _find_nth(self, node, n):
		pass

	def delete_first(self):
		return self.delete_nth(0)

	def delete_last(self):
		return self.delete_nth(-1)

	def delete_nth(self, n):
		pass
	'''
	# --- TRAVERSALS ---
	def __iter__(self):
		return self.inorder()

	def inorder(self):
		return self._inorder_traversal(self.root)

	def preorder(self):
		return self._preorder_traversal(self.root)

	def postorder(self):
		return self._postorder_traversal(self.root)

	def levelorder(self):
		if self.root is None:
			return

		queue = deque([self.root])
		while queue:
			node = queue.popleft()
			for data, count in node.data_store:
                                for _ in range(count):
                                        yield data
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)

	def _inorder_traversal(self, node):
		if node is not None:
			yield from self._inorder_traversal(node.left)
			for data, count in node.data_store:
				for _ in range(count):
					yield data
			yield from self._inorder_traversal(node.right)

	def _preorder_traversal(self, node):
		if node is not None:
			for data, count in node.data_store:
                                for _ in range(count):
                                        yield data
			yield from self._preorder_traversal(node.left)
			yield from self._preorder_traversal(node.right)

	def _postorder_traversal(self, node):
		if node is not None:
			yield from self._postorder_traversal(node.left)
			yield from self._postorder_traversal(node.right)
			for data, count in node.data_store:
                                for _ in range(count):
                                        yield data

