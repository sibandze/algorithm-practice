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

    def _build_component_graph(self, G: Dict[Any, List[Any]], nodes: Set[Any]) -> Dict[Any, List[Any]]:
        """
        Helper to construct the adjacency list for a component given its set of nodes.
        """
        component_graph = {}
        for node in nodes:
            # Check G[node] to get only neighbors that are also in the component (i.e., in 'nodes')
            # Using set intersection is robust, even though for a connected component
            # all neighbors of a node in the component should also be in the component.
            neighbors_in_component = [v for v in G.get(node, []) if v in nodes]
            component_graph[node] = neighbors_in_component
        return component_graph

    def connected_components(self, G: Dict[Any, List[Any]]) -> List[Dict[Any, List[Any]]]:
        """
        Finds the connected components of an undirected graph G using BFS.
        Each component is returned as an adjacency list subgraph.

        Args:
            G (Dict[Any, List[Any]]): The graph represented as an adjacency list.

        Returns:
            List[Dict[Any, List[Any]]]: A list of adjacency list subgraphs,
                                        where each subgraph is a connected component.
        """
        # Ensure all nodes in the graph are considered, including isolated nodes
        all_nodes = set(G.keys())
        for neighbors in G.values():
             all_nodes.update(neighbors)

        # Initialize visited set for the entire graph traversal
        visited = set()
        connected_components = []

        # Iterate over all nodes to find starting points for new components
        for start_node in all_nodes:
            if start_node not in visited:
                # Found a new component, start BFS/DFS
                component_nodes = set()
                q = collections.deque([start_node])
                visited.add(start_node)
                component_nodes.add(start_node)

                while q:
                    u = q.popleft()

                    # Ensure u is a key in G, as it might be an isolated node only in all_nodes
                    for v in G.get(u, []):
                        if v not in visited:
                            visited.add(v)
                            component_nodes.add(v)
                            q.append(v)

                # Build the adjacency list representation for the found component
                component_graph = self._build_component_graph(G, component_nodes)
                connected_components.append(component_graph)

        return connected_components

    def topological_sort(self, G: Dict[Any, List[Any]]):
        sorted_vertex = []

        def dfs(v, visited):



