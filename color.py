def isSafe(v, colour_list, curr_color):
    for i in range(no_vertices):
        if graph[v][i] == 1 and colour_list[i] == curr_color:
            return False
    return True

def graphColourUtil(m, colour_list, v):
    if v == no_vertices: # base case
        return True

    for curr_color in range(1, m+1):
        if isSafe(v, colour_list, curr_color) == True:
            colour_list[v] = curr_color

            if graphColourUtil(m, colour_list, v + 1) == True:
                return True
            colour_list[v] = 0

    return False

def graphColouring(m):
    colour_list = [0] * no_vertices

    if graphColourUtil(m, colour_list, 0) == False:
        print("Solution does not exist")
        return False

    print("Solution exists and the following are the assigned colors:")
    for curr_color in colour_list:
        print(curr_color, end=' ')
    return True

no_vertices = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of colors available: "))
graph = []
print("Enter the adjacency matrix row-wise:")
for i in range(no_vertices):
    row = list(map(int, input().split()))
    graph.append(row)

graphColouring(m)

