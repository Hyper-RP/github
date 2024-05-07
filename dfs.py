def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def main():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))
    
    for i in range(num_vertices):
        vertex = input("Enter vertex name: ")
        neighbors = input("Enter neighbors of vertex {} separated by space: ".format(vertex)).split()
        graph[vertex] = neighbors
    
    start_vertex = input("Enter the start vertex for DFS: ")
    
    print("Depth First Search starting from vertex {}:".format(start_vertex))
    dfs(graph, start_vertex)

if __name__ == "__main__":
    main()
