from simple_uweighted_graph_algorithms import Graph_Algorithms

# --- 1. Define a Sample Graph (Adjacency List) ---
# The graph is undirected and unweighted.
# G[u] contains a list of nodes reachable directly from u.
# The graph: A-B, B-C, B-D, C-E, D-F, F-G, H (isolated)
GRAPH = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'E'],
    'D': ['B', 'F'],
    'E': ['C'],
    'F': ['D', 'G'],
    'G': ['F'],
    'H': [], # Isolated node
    'I': ['J'], # Start of a second component
    'J': ['I']
}

# --- 2. Initialize the Class ---
graph_solver = Graph_Algorithms()

print("--- Graph Analysis using Graph_Algorithms ---")
print(f"Sample Graph: {GRAPH}")
print("-" * 40)

# --- 3. Method: single_source_reachability ---
# Checks if node 'G' is reachable from node 'A'.
start_node_reach = 'A'
target_node_reach = 'G'
is_reachable = graph_solver.single_source_reachability(GRAPH, start_node_reach, target_node_reach)
print(f"1. Is '{target_node_reach}' reachable from '{start_node_reach}'? **{is_reachable}**")

# Check for a non-reachable node
target_node_unreach = 'H'
is_unreachable = graph_solver.single_source_reachability(GRAPH, start_node_reach, target_node_unreach)
print(f"   Is '{target_node_unreach}' reachable from '{start_node_reach}'? **{is_unreachable}**")
print("-" * 40)

# --- 4. Method: single_pair_shortest_path ---
# Finds the shortest path and distance between 'A' and 'G'.
start_node_path = 'A'
target_node_path = 'G'
distance, path = graph_solver.single_pair_shortest_path(GRAPH, start_node_path, target_node_path)
print(f"2. Shortest Path from '{start_node_path}' to '{target_node_path}':")
print(f"   Distance: **{distance}**")
print(f"   Path: **{path}**")

# Check for a path that doesn't exist
start_node_no_path = 'A'
target_node_no_path = 'H'
no_dist, no_path = graph_solver.single_pair_shortest_path(GRAPH, start_node_no_path, target_node_no_path)
print(f"\n   Shortest Path from '{start_node_no_path}' to '{target_node_no_path}':")
print(f"   Distance: **{no_dist}**")
print(f"   Path: **{no_path}**")
print("-" * 40)

# --- 5. Method: single_source_shortest_path ---
# Finds all shortest distances and predecessors from 'B'.
start_node_all_paths = 'B'
distances, predecessors = graph_solver.single_source_shortest_path(GRAPH, start_node_all_paths)
print(f"3. Shortest Distances and Predecessors from '{start_node_all_paths}':")
print(f"   Distances: **{distances}**")
print(f"   Predecessors: **{predecessors}**")
print("-" * 40)

# --- 6. Method: connected_components ---
# Identifies the connected subgraphs.
components = graph_solver.connected_components(GRAPH)
print(f"4. Connected Components Found: **{len(components)}**")

for i, component in enumerate(components):
    # Print the nodes in the component for easy viewing
    component_nodes = sorted(component.keys())
    print(f"   Component {i+1} (Nodes: {component_nodes}):")
    print(f"     {component}")

print()

# --- 1. Define Directed Graphs ---

# Acyclic Graph (DAG): A -> C, A -> D, B -> D, B -> E, C -> F, D -> F, D -> G, F -> H, G -> H
G_ACYCLIC = {
    'A': ['C', 'D'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['F', 'G'],
    'E': [],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

# Cyclic Graph: Cycle 1 -> 2 -> 3 -> 1
G_CYCLIC = {
    1: [2],
    2: [3],
    3: [1, 4], 
    4: [5],
    5: [6],
    6: []
}

# --- 2. Initialize the Class ---
graph_solver = Graph_Algorithms()

print("--- Directed Graph Analysis (Topological Sort) ---")

# --- 3. Test on Acyclic Graph (DAG) ---
print("\n## 🌳 Test on G_ACYCLIC (DAG)")
print(f"Graph Nodes: {list(G_ACYCLIC.keys())}")
top_sort_acyclic = graph_solver.topological_sort(G_ACYCLIC)
print(f"Result: **{top_sort_acyclic}**")
if top_sort_acyclic:
    print("Status: Success - A valid topological order was found.")
else:
    print("Status: Failure - Cycle Detected.")

# --- 4. Test on Cyclic Graph ---
print("\n## ➡️ Test on G_CYCLIC (Cyclic)")
print(f"Graph Nodes: {list(G_CYCLIC.keys())}")
top_sort_cyclic = graph_solver.topological_sort(G_CYCLIC)
print(f"Result: **{top_sort_cyclic}**")
if not top_sort_cyclic:
    print("Status: **Success - Cycle Detected** (returns empty list as designed).")
else:
    print("Status: Failure - Incorrectly returned a sort for a cyclic graph.")
