# Name: Long Hoang 
# part 1
import sys
import heapq
from collections import defaultdict

# dijkstra's algorithm
def dijkstra(n, start, graph):
    # initialize distance with infinity / n+1 element
    dist = [float('inf')] * (n + 1)
    # set start node's distance = 0
    dist[start] = 0

    # queue to store (distance, node)
    pq = [(0, start)]

    while pq:
        # get node with the smallest distance/time to travel
        time, node = heapq.heappop(pq)

        # skip node with longer time 
        if time > dist[node]:
            continue

        # explore all neighbors of the current node
        for neighbor, weight in graph[node]:
            # travel time
            new_time = time + weight 
            
            # if time is shorter, add to queue
            if new_time < dist[neighbor]:
                dist[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))
    
    return dist

# find the earliest meeting time: n nodes, m edges, edges(u, v, w) --> w is the weight of node u-v  
def earliest_meeting_time(n, m, edges):
    # construct the graph using adjacency list
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # run dijkstra's algo from node 1 (xyra's start)
    xyra_dist = dijkstra(n, 1, graph)

    # run dijkstra's algo from node n (orion's start)
    orion_dist = dijkstra(n, n, graph)

    # check if they can reach each other: if they cannot reach each other's end --> there's no path
    if xyra_dist[n] == float('inf') or orion_dist[1] == float('inf'):
        return -1
    
    # find the earliest meeting time 
    earliest_time = float('inf')
    for i in range(1, n+1):
        maximum_time_to_meet = max(xyra_dist[i], orion_dist[i]) # max time for 2 robots to meet at node i

        #update smaller possible time
        earliest_time = min(earliest_time, maximum_time_to_meet)

    return earliest_time if earliest_time != float('inf') else -1

if __name__ == "__main__":
    # read input using stdin 
    input = sys.stdin.read().strip().splitlines()

    # parse n nodes and m edges
    n, m = map(int, input[0].split())

    # parse each edge property (u,v,w)
    edges = [tuple(map(int, line.split())) for line in input[1:]]

    # perform methods
    print(earliest_meeting_time(n, m, edges))









