import numpy as np
import random

def generate_random_graph(n, density):
    graph = [[] for _ in range(n)]
    max_edges = n * (n - 1) // 2
    num_edges = int(max_edges * density)

    while num_edges > 0:
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        if i != j and j not in graph[i]:
            graph[i].append(j)
            graph[j].append(i)
            num_edges -= 1

    return graph

def warshall(graph):
    num_nodes = len(graph)
    shortest_paths = np.zeros((num_nodes, num_nodes))

    adjacency_matrix = np.zeros((num_nodes, num_nodes))
    for i in range(num_nodes):
        for j in graph[i]:
            adjacency_matrix[i][j] = 1

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                shortest_paths[i][j] = 0
            elif adjacency_matrix[i][j] == 1:
                shortest_paths[i][j] = 1
            else:
                shortest_paths[i][j] = float('inf')

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                shortest_paths[i][j] = min(shortest_paths[i][j], shortest_paths[i][k] + shortest_paths[k][j])

    return shortest_paths, adjacency_matrix

def main():
    n = int(input("Enter the number of users in the social network (from 20 to 200): "))
    density = float(input("Enter the density of the graph (from 0.0 to 1.0): "))

    graph = generate_random_graph(n, density)

    shortest_paths, adjacency_matrix = warshall(graph)

    print("\nAdjacency matrix of the graph:")
    for row in adjacency_matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
