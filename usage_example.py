import random
from trees import BST

max_len = 10**6
min_num = -10**9
max_num = 10**9

number_of_data_list = random.randint(2, 10)
data_lists = []
print(f"\r\033[KGenerating {number_of_data_list} data lists of lengths...", end = "")

for i in range(number_of_data_list):
	length = random.randint(0, max_len)
	if i == 0:
		s = f"Generating {number_of_data_list} data lists of lengths {length}..."
	else:
		s = f"{s[0:-3]}, {length}..."
	print(f"\r\033[K{s}", end = "")
	data_lists.append([random.randint(random.randint(min_num, 0), random.randint(1,max_num)) for _  in range(length)])
print(f"\r\033[K{s}")
print()


for idx, data_list in enumerate(data_lists):
	print(f"List {idx+1}: {len(data_list)} items, {len(set(data_list))} unique items.")
	bst = BST()
	min_max = [float("inf"), float("-inf")]
	for data in data_list:
		min_max = min(min_max[0], data), max(min_max[1], data)
		bst.insert(data)
	start = True
	'''for data in bst:
		print(f", {data}" if not start else data, end = "")
		if start:
			start = False
	'''
	min_key = bst.find_min_data()
	max_key = bst.find_max_data()
	print(f"Min: {min_key == min_max[0]}, Max: {max_key==min_max[1]}")
	print()
