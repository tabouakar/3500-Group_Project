def run_hamiltonian_algorithm():
    # Sample graph represented as an adjacency list
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2]
    }
    N = len(graph)  # Number of vertices in the graph

    path = []

    def is_valid(vertex, path):
        """Check if the current vertex can be added to the Hamiltonian Path."""
        # Check if this vertex is an adjacent vertex of the previous vertex
        if vertex not in graph[path[-1]]:
            return False
        # Check if the vertex has already been included in the path
        if vertex in path:
            return False
        return True

    def hamiltonian_path(vertex):
        """Recursive utility function to solve the Hamiltonian Path problem."""
        # Base case: If all vertices are included in the path
        if len(path) == N:
            return True

        for next_vertex in graph[vertex]:
            if is_valid(next_vertex, path):
                path.append(next_vertex)
                if hamiltonian_path(next_vertex):
                    return True
                # Remove current vertex if it doesn't lead to a solution
                path.pop()

        return False

    # Try to find a Hamiltonian Path starting from each vertex
    for start_vertex in graph:
        path = [start_vertex]
        if hamiltonian_path(start_vertex):
            print(f"Hamiltonian Path found: {path}")
            return path
        else:
            print(f"No Hamiltonian Path found starting from vertex {start_vertex}")

    print("No Hamiltonian Path exists for the given graph.")
    return None

# Call the function to test the implementation
run_hamiltonian_algorithm()
