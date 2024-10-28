from collections import defaultdict
from queue import Queue, PriorityQueue

def read_txt(file):
    size=int(file.readline())
    start,goal=(int(num) for num in file.readline().split(' '))
    matrix=[[int(num) for num in line.split(' ')] for line in file]
    return size,start,goal,matrix

def  convert_graph(a):
    adjList=defaultdict(list)
    for i in range (len(a)):
        for j in range (len(a[i])):
            if a[i][j]==1:
                adjList[i].append(j)
    return adjList

def convert_graph_weight(a):
    adjList = defaultdict(list)
    for i in range (len(a)):
        for j in range (len(a[i])):
            if a[i][j]!=0:
                adjList[i].append((j,a[i][j]))
    return adjList

def BFS(graph, start, end):
    visited = set()
    frontier = Queue()
    frontier.put(start)
    visited.add(start)
    parent = {start: None}
    path_found = False

    while not frontier.empty():
        current_node = frontier.get()
        if current_node == end:
            path_found = True
            break
        for node in graph[current_node]:
            if node not in visited:
                frontier.put(node)
                parent[node] = current_node
                visited.add(node)
    path = []
    if path_found:
        
        while current_node is not None:
            path.append(current_node)
            current_node = parent[current_node]
        path.reverse()
        return path
   
def DFS(graph,start,end):
    visited = []
    frontier = []
    frontier.append(start)
    visited.append(start)
    parent=dict()
    parent[start]=None
    path_found=False
    while True:
        if frontier==[]: 
            raise Exception("No way Exception")
        current_node = frontier.pop()
        visited.append(current_node)
        if current_node == end:
            path_found = True
            break
        for node in graph[current_node]:
            if node not in visited:
                frontier.append(node)
                parent[node]=current_node
                visited.append(node)
    path = []
    if path_found:
        path.append(end)
        while parent[end] is not None:
            path.append(parent[end])
            end=parent[end]
        path.reverse()
    return path

def UCS(graph,start,end):
    visited = []
    frontier = PriorityQueue()
    frontier.put((0,start))
    visited.append(start)
    parent=dict()
    parent[start]=None
    path_found=False
    while True:
        if frontier.empty():
            print("No way Exception")
            current_w = 0
            break
        current_w, current_node = frontier.get()
        visited.append(current_node)
        if current_node==end:
            path_found=True
            break
        for node_i in graph[current_node]:
            node, weight = node_i
            if node not in visited:
                frontier.put((current_w + weight, node))
                parent[node] = current_node
                visited.append(node)
    path = []
    if path_found:
        path.append(end)
        while parent[end] is not None:
            path.append(parent[end])
            end=parent[end]
        path.reverse()
    return current_w, path
if __name__ == "__main__":
    # Read Input.txt and InputUCS.txt files
    file_1 = open("Input.txt", "r")
    file_2 = open("InputUCS.txt", "r")

    size_1, start_1, goal_1, matrix_1 = read_txt(file_1)
    size_2, start_2, goal_2, matrix_2 = read_txt(file_2)

    file_1.close()
    file_2.close()

    graph_1 = convert_graph(matrix_1)
    graph_2 = convert_graph_weight(matrix_2)

    # Execute BFS algorithm
    result_bfs = BFS(graph_1, start_1, goal_1)
    print("Result using BFS algorithm: \n", result_bfs)

    # Execute DFS algorithm
    result_dfs = DFS(graph_1, start_1, goal_1)
    print("Result using DFS algorithm: \n", result_dfs)

    # Execute UCS algorithm
    cost, result_ucs = UCS(graph_2, start_2, goal_2)
    print("Result using UCS algorithm: \n", result_ucs, "with total cost of", cost)
