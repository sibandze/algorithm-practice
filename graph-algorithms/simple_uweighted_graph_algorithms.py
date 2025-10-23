import collections import deque
from typing import List, Dict, Tuple, Set, Any

class Graph_Algorithms:
    def single_source_reachability(self, G: Dict[Any, List[Any]], s: Any, t: Any) -> bool:
        """
        Determines if node t is reachable from node s in an unweighted graph G
        using Breadth-First Search (BFS).

        Args:
            G (Dict[Any, List[Any]]): The graph represented as an adjacency list.
            s (Any): The starting node.
            t (Any): The target node.

        Returns:
            bool: True if t is reachable from s, False otherwise.
        """
        if s not in G or t not in G:
            return False

        q = deque([s])
        visited = {s}

        while q:
            u = q.popleft()

            if u == t:
                return True

            for v in G[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return False

    def _build_path(self, p: Dict[Any, Any], s: Any, t: Any) -> List[Any]:
        """
        Helper function to reconstruct the path from s to t using a predecessor map.

        Args:
            p (Dict[Any, Any]): Predecessor map (node -> its parent in BFS tree).
            s (Any): The starting node.
            t (Any): The target node.

        Returns:
            List[Any]: The path from s to t.
        """
        path = []
        curr = t
        while curr != s: # Trace back until the start node is reached
            path.append(curr)
            curr = p[curr]
        path.append(s) # Add the start node
        return path[::-1] # Reverse to get path from s to t

    def single_pair_shortest_path(self, G: Dict[Any, List[Any]], s: Any, t: Any) -> Tuple[int, List[Any]]:
        """
        Finds the shortest path distance and the path itself between s and t
        in an unweighted graph G using BFS.

        Args:
            G (Dict[Any, List[Any]]): The graph represented as an adjacency list.
            s (Any): The starting node.
            t (Any): The target node.

        Returns:
            Tuple[int, List[Any]]: A tuple containing the shortest distance
                                   and the path. Returns (float('inf'), []) if not reachable.
        """
        if s not in G or t not in G:
            return float('inf'), []

        q = collections.deque([(s, 0)]) # Queue stores (node, distance)
        visited = {s}
        p = {} # Predecessor map

        while q:
            u, dist = q.popleft()

            if u == t:
                return dist, self._build_path(p, s, t)

            for v in G[u]:
                if v not in visited:
                    visited.add(v)
                    p[v] = u # Record predecessor
                    q.append((v, dist + 1))

        return float('inf'), [] # Not reachable

    def single_source_shortest_path(self, G: Dict[Any, List[Any]], s: Any) -> Tuple[Dict[Any, int], Dict[Any, Any]]:
        """
        Finds the shortest path distances and predecessors from s to all reachable
        nodes in an unweighted graph G using BFS.

        Args:
            G (Dict[Any, List[Any]]): The graph represented as an adjacency list.
            s (Any): The starting node.

        Returns:
            Tuple[Dict[Any, int], Dict[Any, Any]]: A tuple containing:
                - A dictionary of shortest distances from s to all nodes.
                - A dictionary of predecessors for path reconstruction.
        """
        if s not in G:
            # If start node is not in graph, return all distances as infinity and empty predecessors.
            return {v: float('inf') for v in G}, {} 

        distances = {node: float('inf') for node in G}
        p = {} # Predecessor map

        q = collections.deque([(s, 0)]) # Queue stores (node, distance)
        visited = {s}
        distances[s] = 0 # Distance from s to s is 0

        while q:
            u, dist = q.popleft()

            for v in G[u]:
                if v not in visited:
                    visited.add(v)
                    p[v] = u # Record predecessor
                    distances[v] = dist + 1 # Update shortest distance
                    q.append((v, dist + 1))

        return distances, p

    def connected_components(self, G: Dict[Any, List[Any]]) -> List[Dict[any, List[Any]]]:
        #for undirected G
        connected_components = []

		unvisited_vertexes = set(G) # Create a set of all unvisited vertexes
		for neighbors in G.values():
             unvisited_vertexes.update(neighbors)

        def dfs(v, components):
            if v in G:
                 for u in G[v]:
				    if u in unvisited_vertexes:
                        components[u] = G.get(u, [])
                        unvisited_vertexes.remove(u)
					    dfs(u, components)
            return components

        while unvisited_vertexes:
			v = unvisited_vertexes.pop()
            components = dfs(v, {v: G.get(v,[])})
            connected_components.append(components)
        return connected_components
