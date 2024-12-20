from mpi4py import MPI
import networkx as nx
import time  # Для замера времени

# Create graph with connected parts
def create_graph(numbers):
    graph = nx.DiGraph()
    graph.add_nodes_from(numbers)

    for num in numbers:
        for other in numbers:
            if num != other and num[-2:] == other[:2]:
                graph.add_edge(num, other)

    return graph

# Find longest sequence
def find_longest_path_exhaustive(graph, start_nodes):
    def dfs(node, visited, path):
        nonlocal longest_path
        visited.add(node)
        path.append(node)

        if len(path) > len(longest_path):
            longest_path = path[:]

        for neighbor in graph.successors(node):
            if neighbor not in visited:
                dfs(neighbor, visited, path)

        visited.remove(node)
        path.pop()

    longest_path = []
    for start_node in start_nodes:
        dfs(start_node, set(), [])
    return longest_path

# Merge numbers
def merge_path(path):
    if not path:
        return ""
    merged_sequence = path[0]
    for i in range(1, len(path)):
        merged_sequence += path[i][2:]
    return merged_sequence


def main():
    # Initialize MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    start_time = time.time()

    if rank == 0:
        with open("source.txt", "r") as f:
            numbers = [line.strip() for line in f.readlines()]
    else:
        numbers = None

    numbers = comm.bcast(numbers, root=0)
    graph = create_graph(numbers)

    nodes = list(graph.nodes)
    chunk_size = len(nodes) // size
    start_nodes = nodes[rank * chunk_size : (rank + 1) * chunk_size] if rank < size - 1 else nodes[rank * chunk_size :]

    local_longest_path = find_longest_path_exhaustive(graph, start_nodes)
    all_longest_paths = comm.gather(local_longest_path, root=0)

    if rank == 0:
        overall_longest_path = max(all_longest_paths, key=len)
        longest_sequence = merge_path(overall_longest_path)

        end_time = time.time()

        print("Longest sequence:", longest_sequence)
        print("Length of sequence:", len(overall_longest_path))
        print(f"Execution time with {size} processes: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
