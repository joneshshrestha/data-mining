import numpy as np


def create_transition_matrix(edges, nodes):
    """
    Create transition matrix from edge list.
    edges: list of tuples (from_node, to_node)
    nodes: list of node names
    """
    n = len(nodes)
    node_to_idx = {node: i for i, node in enumerate(nodes)}

    # Initialize matrix with zeros
    M = np.zeros((n, n))

    # Count outgoing links for each node
    out_degree = {node: 0 for node in nodes}
    for src, dst in edges:
        out_degree[src] += 1

    # Fill transition matrix
    for src, dst in edges:
        i = node_to_idx[src]
        j = node_to_idx[dst]
        if out_degree[src] > 0:
            M[j][i] = 1.0 / out_degree[src]

    return M, node_to_idx


def compute_pagerank(M, iterations=100, tolerance=1e-6):
    """
    Compute PageRank using power iteration method.
    M: transition matrix
    iterations: maximum number of iterations
    tolerance: convergence threshold
    """
    n = M.shape[0]
    # Initialize with uniform distribution
    v = np.ones(n) / n

    print(f"Initial distribution: {v}")
    print()

    for i in range(iterations):
        v_new = M @ v

        # Check convergence
        diff = np.linalg.norm(v_new - v, 1)

        print(f"Iteration {i+1}: {v_new}")

        if diff < tolerance:
            print(f"\nConverged after {i+1} iterations")
            break

        v = v_new

    return v
