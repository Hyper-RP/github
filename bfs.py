from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Taking input from the user to represent the graph as an adjacency list
def input_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        u, v = input("Enter an edge (u v): ").split()
        u, v = int(u), int(v)

        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append(v)
        graph[v].append(u)

    return graph

if __name__ == "__main__":
    graph = input_graph()
    start_node = int(input("Enter the start node: "))

    print("BFS Traversal:")
    bfs(graph, start_node)
