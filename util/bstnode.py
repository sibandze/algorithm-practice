from util import TreeNode
class BSTNode(TreeNode):
	"""
	Represents a node specifically for a Binary Search Tree.
	Inherits from TreeNode, which already has left/right pointers.
	This base BST node doesn't add tree-specific properties directly,
	but serves as a clear indicator for BST structures.
	"""
	def __init__(self, key, data):
		super().__init__(None) # Initialize data, left, right from TreeNode
		# Additional properties like height or parent are often added by
		# more specific subclasses (like AVLNode) or managed by the BST class itself.
		# To handle duplicates and keep track of duplicates
		self.key = key
		self.data_store = [[data, 1]]
		self.size = 1

	def insert(self, data, key_extractor, comparator):
		data_key = key_extractor(data)
		if comparator(data_key, self.key) != 0:
			raise Exception("Key mismatch: Node key {} does not match data key {}".format(self.key, data_key))
		for i, (stored_data, count) in enumerate(self.data_store):
			if stored_data == data:
				self.data_store[i][1] += 1
				self.size += 1
				return
		self.data_store.append([data, 1])
		self.size += 1

	def delete(self, data, key_extractor, comparator):
		data_key = key_extractor(data)
		if comparator(data_key, self.key) != 0:
			raise Exception("Key mismatch: Node key {} does not match data key {}".format(self.key, data_key))

		for i, (stored_data, count) in enumerate(self.data_store):
			if stored_data == data:
				if count > 1:
					self.data_store[i][1] -= 1
					self.size -= 1
				else:
					self.data_store.pop(i)
					self.size -= 1
				return True
		return False

	def delete_key(self, key, key_extractor, comparator):
		data_key = key_extractor(data)
		if comparator(data_key, self.key) != 0:
			raise Exception("Key mismatch: Node key {} does not match data key {}".format(self.key, data_key))

		if len(self.data_store) > 0:
			size = self.size
			self.data_store.clear()
			self.size = 0
			return size
		return 0

	def __repr__(self):
		# Leverage TreeNode's repr, but indicate it's a BSTNode
		return f"BSTNode(key={self.key}, size={self.size}, left={repr(self.left)}, right={repr(self.right)})"

