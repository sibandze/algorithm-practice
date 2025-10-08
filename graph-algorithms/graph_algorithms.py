class Graph_Algorithms:
	def single_source_reachability(self, G, s, t):
		if s not in G or t not in G:
			return False

		level = [s]
		visited = set()
		while level:
			next_level = []
			for u in level:
				if u == t:
					return True
				visited.add(u)
				for v in G[u]:
					if v not in visited:
						next_level.append(v)
			level[:] =  next_level
		return False

	def _build_path(self, p, s, t):
		path = []
		v  = t
		while True:
			path.append(v)
			if v == s:
				break
			v = p[v]

		return path[:]

	def single_pair_shortest_path(self, G, s, t):
		if s not in G or t not in G:
			return float('inf'), []

		distance = 0
		level = [s]
		visited = set()
		p = {}
		while level:
			next_level = []
			for u in level:
				visited.add(u)
				if u == t:
                    return distance, self._build_path(p, s, t))

				for v in G[u]:
					if v not in visited:
						p[v] = u
						next_level.append(v)
			level[:] =  next_level
			distance+=1
		return float('inf'), []

	def single_source_shortest_path(G, s):
		p = {}
		distance = 0
		distances = {v:float('inf') for v in G}
		level = [s]
		visited = {}

		while level:
			next_level = []
			for u in level:
				distances[u] = distance
				visited.add(u)
				for v in G[u]:
					if v not in visited:
						p[v] = u
						next_level.append(v)
			level[:] =  next_level
			distance+=1
		return distances, p

