from pprint import pprint

from collections import deque
#insert, pop, popleft, remove, index, append


from math import inf

def adjacency_list(graph_str):
    """
    converts a graph_str to a list of edges for each vertex
        (e.g. adj_list[0] == list of all edges from vertex 0)
    """
    rows = (graph_str.rstrip()).split("\n")
    top_row_data = rows[0].split()
    directed, n = top_row_data[0] == 'D', int(top_row_data[1])
    weighted = True if len(top_row_data) > 2 and top_row_data[2] == 'W' else False

    output = [[] for i in range(n)]
    for row in rows[1:]:
        row_data = row.split()
        src, dst = int(row_data[0]), int(row_data[1])
        cost = int(row_data[2]) if weighted else None
        output[src].append((dst, cost))
        if not directed:
            output[dst].append((src, cost))
    
    return output



def dijkstra(adj_list, start):
    """
    Given a graph with non-negative edge weights and a starting vertex, the al-
    gorithm finds the shortest path from the starting vertex to any other vertex
    reachable from it.
    
    The algorithm gradually grows a shortest path tree rooted at the starting
    vertex. In each iteration, a new edge is added to the tree by selecting an edge
    that connects a vertex in the tree to a vertex outside that is closest to the
    starting vertex.
    """
    n = len(adj_list)
    in_tree = [False for x in range(n)]
    distance = [float('inf') for x in range(n)]
    parent = [None for x in range(n)]
    distance[s] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if not in_tree[v] and (distance[u] + weight) < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance


def next_vertex(in_tree, distance):
    """
    Function used by the prim mst and dijkstra algorithms.
    Given a distance array, finds the next un-discovered vertex with the lowest cost.
    """
    n = None
    for i, vertex in enumerate(in_tree):
        # vertex not reached yet, and (init or lower cost vertex found)
        if not vertex and (n == None or distance[i] < distance[n]):
            n = i
    return n


def next_hop(parent, start):
    if parent[start] == None:
        return start
    elif parent[parent[start]] == None:
        return start
    return next_hop(parent, parent[start])

# 2nd number in top line is number vertices + 1
graph_string = """\
U 8 W
1 2 1
1 7 8
1 6 5
2 1 1
2 3 3
3 2 3
3 4 4
4 3 4
4 7 6
4 5 2
5 4 2
5 6 1
6 5 1
6 1 5
7 1 8
7 4 6
"""
import sys
ARGUEMENTS = sys.argv[1:]
source = int(ARGUEMENTS[0])
print(source)

parent, cost = (dijkstra(adjacency_list(graph_string), source))#forwarding table for x
print(parent[1:],cost[1:])#extra 0 vertex is included so must be removed
print("parent (p) is the last hop to the target router addr (a)")
print('a','p',"c (addr, parent(not next_hop), cost)")
for i in range(1,len(cost)):
    p = parent[i]
    if p == None:
        p = ' '
    print(i,next_hop(parent,i),cost[i])
