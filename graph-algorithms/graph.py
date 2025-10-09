import collections
# heapq is not used in the Graph class itself, but often with it for algorithms
from typing import List, Dict, Tuple, Set, Any, Union, Type # Type for classmethod

# Define type aliases for clarity
Node = Any
Weight = Union[int, float] # Weights can be integers or floats

# Adjacency list format: Dict[Node, Set[Tuple[Node, Weight]]]
# Even for unweighted graphs, we store (neighbor, 1) internally for consistency.
AdjList = Dict[Node, Set[Tuple[Node, Weight]]]

class Graph:
    """
    A class to represent a graph, supporting both directed/undirected and
    weighted/unweighted variations. Provides standard graph operations and
    Pythonic access via magic methods.
    """
    def __init__(self, directed: bool = False, weighted: bool = False):
        """
        Initializes an empty graph.

        Args:
            directed (bool): True if the graph is directed (edges are one-way),
                             False for undirected (edges are two-way). Defaults to False.
            weighted (bool): True if edges have weights, False for unweighted (all weights are 1).
                             Defaults to False.
        """
        self.adj: AdjList = collections.defaultdict(set)
        self._directed = directed
        self._weighted = weighted
        self.num_vertices = 0
        self.num_edges = 0 # Represents conceptual edges, not duplicated for undirected
        self._vertices_set = set() # Explicit set to track all vertices, including isolated ones

    def is_directed(self) -> bool:
        """Returns True if the graph is directed, False otherwise."""
        return self._directed

    def is_weighted(self) -> bool:
        """Returns True if the graph is weighted, False otherwise."""
        return self._weighted

    def add_vertex(self, v: Node):
        """Adds a vertex 'v' to the graph. If 'v' already exists, does nothing."""
        if v not in self._vertices_set:
            self.adj[v] # Ensure 'v' is a key in the adjacency dict even if it has no edges
            self._vertices_set.add(v)
            self.num_vertices += 1

    def remove_vertex(self, v: Node):
        """
        Removes a vertex 'v' and all its incident edges (edges connected to 'v').
        If 'v' does not exist, does nothing.
        """
        if v not in self._vertices_set:
            return

        # 1. Remove edges where 'v' is the source
        if v in self.adj:
            self.num_edges -= len(self.adj[v]) # Decrement by count of edges (v, neighbor)
            del self.adj[v]

        # 2. Remove edges where 'v' is the destination for other nodes
        # Iterate over a copy of keys to avoid modification issues during iteration
        for u in list(self._vertices_set): # Iterate over all vertices that might have edges to v
            if u == v: # Skip if u is the vertex being removed
                continue

            edges_to_remove_from_u = set()
            for neighbor, weight in self.adj.get(u, set()):
                if neighbor == v:
                    edges_to_remove_from_u.add((neighbor, weight))

            if edges_to_remove_from_u:
                self.adj[u].difference_update(edges_to_remove_from_u)
                # For directed graphs, these are 'incoming' edges to 'v'.
                # They represent distinct conceptual edges that need num_edges decrement.
                # For undirected graphs, these are the symmetric representations of edges (v,u)
                # which were already handled in step 1, so no further decrement needed for num_edges.
                if self._directed:
                    self.num_edges -= len(edges_to_remove_from_u)

        # 3. Finally, remove 'v' from the set of all vertices
        self._vertices_set.remove(v)
        self.num_vertices -= 1

    def add_edge(self, u: Node, v: Node, weight: Weight = 1):
        """
        Adds an edge between vertices 'u' and 'v' with an optional weight.
        If 'u' or 'v' do not exist, they are added to the graph.
        If the edge already exists:
            - For unweighted graphs, no change occurs.
            - For weighted graphs, the edge's weight is updated if different.
        """
        self.add_vertex(u)
        self.add_vertex(v)

        # Ensure weight is always 1 internally for unweighted graphs if no weight is provided,
        # or if the graph itself is unweighted.
        if not self._weighted: # If graph is explicitly unweighted, force weight to 1
            weight = 1

        # Check for existing edge (u, v) (could be with a different weight)
        existing_uv_edge = None
        for neighbor, w in self.adj[u]:
            if neighbor == v:
                existing_uv_edge = (neighbor, w)
                break

        # If no edge (u,v) exists, or if it exists but its weight needs updating (for weighted graph)
        if not existing_uv_edge:
            self.adj[u].add((v, weight))
            self.num_edges += 1 # Increment for a new conceptual edge
        elif self._weighted and existing_uv_edge[1] != weight:
            # If weighted graph and weight is being updated
            self.adj[u].remove(existing_uv_edge)
            self.adj[u].add((v, weight))
            # num_edges does not change, as it's an update, not a new edge

        # Handle undirected graph symmetry: add/update the reverse edge (v, u)
        if not self._directed:
            existing_vu_edge = None
            for neighbor, w in self.adj[v]:
                if neighbor == u:
                    existing_vu_edge = (neighbor, w)
                    break

            if not existing_vu_edge:
                self.adj[v].add((u, weight))
                # num_edges was already incremented for the conceptual edge (u,v),
                # so no further increment here.
            elif self._weighted and existing_vu_edge[1] != weight:
                # If weighted graph and weight needs updating for the symmetric edge
                self.adj[v].remove(existing_vu_edge)
                self.adj[v].add((u, weight))
            # If unweighted and edge (v,u) exists (or was just added), no action needed.

    def remove_edge(self, u: Node, v: Node):
        """
        Removes an edge between vertices 'u' and 'v'.
        If the edge does not exist, does nothing.
        """
        if u not in self._vertices_set or v not in self._vertices_set:
            return

        edge_to_remove_from_u = None
        for neighbor, weight in self.adj.get(u, set()):
            if neighbor == v:
                edge_to_remove_from_u = (neighbor, weight)
                break

        if edge_to_remove_from_u:
            self.adj[u].remove(edge_to_remove_from_u)
            self.num_edges -= 1 # Decrement for a conceptual edge being removed

        # If undirected, also remove the symmetric edge (v, u)
        if not self._directed:
            edge_to_remove_from_v = None
            for neighbor, weight in self.adj.get(v, set()):
                if neighbor == u:
                    edge_to_remove_from_v = (neighbor, weight)
                    break

            if edge_to_remove_from_v:
                self.adj[v].remove(edge_to_remove_from_v)
                # num_edges was already decremented for the conceptual edge (u,v),
                # so no further decrement here.

    def has_vertex(self, v: Node) -> bool:
        """Checks if vertex 'v' exists in the graph."""
        return v in self._vertices_set

    def has_edge(self, u: Node, v: Node) -> bool:
        """Checks if an edge exists between vertices 'u' and 'v'."""
        if u not in self.adj:
            return False
        return any(neighbor == v for neighbor, _ in self.adj[u])

    def get_edge_weight(self, u: Node, v: Node) -> Union[Weight, None]:
        """
        Returns the weight of the edge (u,v).
        Returns None if no such edge exists.
        """
        if u not in self.adj:
            return None
        for neighbor, weight in self.adj[u]:
            if neighbor == v:
                return weight
        return None

    def get_vertices(self) -> List[Node]:
        """Returns a list of all vertices in the graph."""
        return list(self._vertices_set)

    def get_edges(self) -> List[Tuple[Node, Node, Weight]]:
        """
        Returns a list of all edges in the graph as (u, v, weight) tuples.
        For undirected graphs, each conceptual edge is listed only once.
        """
        edge_list = []
        # Iterate over sorted vertices and neighbors for consistent output
        for u in sorted(list(self._vertices_set), key=str):
            if u in self.adj:
                for v, weight in sorted(list(self.adj[u]), key=lambda x: str(x[0])):
                    # For undirected, only add each conceptual edge (u,v) once (e.g., A-B, not B-A)
                    if self._directed or str(u) < str(v): # Use string comparison for general types
                        edge_list.append((u, v, weight))
        return edge_list

    # --- Static Constructor ---
    @classmethod
    def from_edges(
        cls: Type['Graph'],
        edges: List[Union[Tuple[Node, Node], Tuple[Node, Node, Weight]]],
        directed: bool = False
    ) -> 'Graph':
        """
        Static constructor to create a Graph instance from a list of edges.

        Args:
            cls (Type['Graph']): The Graph class itself.
            edges (List[Union[Tuple[Node, Node], Tuple[Node, Node, Weight]]]):
                A list of edges. Each edge can be a 2-tuple (u, v) for unweighted
                edges or a 3-tuple (u, v, weight) for weighted edges.
                If any edge is a 3-tuple, the graph will be initialized as weighted.
                2-tuple edges in a weighted graph will have a default weight of 1.
            directed (bool): True if the graph should be directed, False for undirected.

        Returns:
            Graph: An instance of the Graph class.

        Raises:
            ValueError: If an edge has an invalid format (not 2 or 3 elements).
        """
        # Determine if the graph should be weighted based on the edge format
        is_weighted_input = any(len(edge) == 3 for edge in edges)

        # Create a new Graph instance
        graph = cls(directed=directed, weighted=is_weighted_input)

        # Add all edges to the graph
        for edge in edges:
            if len(edge) == 2:
                u, v = edge
                graph.add_edge(u, v) # Default weight 1 is used if graph is weighted=True, else forced to 1
            elif len(edge) == 3:
                u, v, weight = edge
                graph.add_edge(u, v, weight)
            else:
                raise ValueError(f"Invalid edge format: {edge}. Edges must be (u, v) or (u, v, w).")

        return graph


    # --- Magic Methods for Pythonic Behavior ---

    def __getitem__(self, v: Node) -> Union[List[Node], List[Tuple[Node, Weight]]]:
        """
        Allows accessing neighbors of a vertex using `graph_instance[v]` syntax.
        Returns:
            - A list of (neighbor, weight) tuples if the graph is weighted.
            - A list of neighbor nodes if the graph is unweighted.
        Returns an empty list if vertex 'v' does not exist or has no outgoing neighbors.
        """
        if v not in self._vertices_set: # Check if vertex exists
            return []

        neighbors_with_weights = list(self.adj.get(v, set()))

        if self._weighted:
            # For weighted graphs, return (neighbor, weight) tuples, sorted by neighbor
            return sorted(neighbors_with_weights, key=lambda x: str(x[0]))
        else:
            # For unweighted graphs, return just neighbor nodes, sorted
            return sorted([neighbor for neighbor, _ in neighbors_with_weights], key=str)

    def __len__(self) -> int:
        """Returns the number of vertices in the graph when `len(graph_instance)` is called."""
        return self.num_vertices

    def __contains__(self, v: Node) -> bool:
        """Allows checking if a vertex exists using `v in graph_instance` syntax."""
        return self.has_vertex(v)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the graph.
        Shows graph type, vertex/edge counts, and adjacency list.
        """
        graph_type_str = "Directed" if self._directed else "Undirected"
        weight_info_str = "Weighted" if self._weighted else "Unweighted"
        s = f"{graph_type_str} {weight_info_str} Graph ({self.num_vertices} vertices, {self.num_edges} edges):\n"

        # Collect and sort vertices for consistent output
        vertices_sorted = sorted(list(self._vertices_set), key=str)

        for v in vertices_sorted:
            neighbors_repr = []
            if v in self.adj:
                # Sort neighbors for consistent output
                sorted_neighbors_info = sorted(list(self.adj[v]), key=lambda x: str(x[0]))
                if self._weighted:
                    neighbors_repr = [f"({n}, {w})" for n, w in sorted_neighbors_info]
                else:
                    neighbors_repr = [str(n) for n, _ in sorted_neighbors_info]
            s += f" {v}: {{{', '.join(neighbors_repr)}}}\n"
        return s

    def __repr__(self) -> str:
        """Returns a developer-friendly string representation of the graph."""
        graph_type_str = "directed" if self._directed else "undirected"
        weight_info_str = "weighted" if self._weighted else "unweighted"
        return f"Graph(num_vertices={self.num_vertices}, num_edges={self.num_edges}, {graph_type_str}={self._directed}, {weight_info_str}={self._weighted})"

