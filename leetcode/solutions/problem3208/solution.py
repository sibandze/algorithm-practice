# Solution for problem 3208
class Solution:
	def numberOfAlternatingGroups(self, colors, k):
		i = 0, j = 1
		count = 0
		n = len(colors)
		while j-i < k and j<n:
			if colors[j] == colors[j-1]:
				i = j
			elif j - i + 1 = k:
				count+=1
			j+=1
		while j<n:
			if colors[j] == colors[j-1]:
				i = j
				j+=1
				while j-i < k and j<n:
					if colors[j] == colors[j-1]:
						i=j
					j+=1
			else:
				count += 1
				j+=1
				i+=1
		return count
