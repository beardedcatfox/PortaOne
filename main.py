import networkx as nx
import time

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
def find_longest_path_exhaustive(graph):
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
    for start_node in graph.nodes:
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
    start_time = time.perf_counter()

    with open("source.txt", "r") as f:
        numbers = [line.strip() for line in f.readlines()]

    graph = create_graph(numbers)
    longest_path = find_longest_path_exhaustive(graph)
    longest_sequence = merge_path(longest_path)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print("Longest sequence:", longest_sequence)
    print("Length of sequence:", len(longest_path))
    print(f"Execution time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
