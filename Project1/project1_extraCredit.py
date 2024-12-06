# Name: Long Hoang 
# extra credit part
import sys
import heapq
from collections import defaultdict

# input: 
# n nodes, m edges, h nodes can turn on hyperdrive
# specify nodes have hyperdrive
# u, v, w

# dijkstra's algorithm with hyperdrive option: hyperdrive_nodes: list of nodes can activate hyperdrive; consider backtracking
def dijkstra(n, start, graph, hyperdrive_nodes=None):
    # initialize distance with infinity / n+1 element
    dist = [[float('inf')] * (n + 1) for _ in range(2)] #[0] for normal weights, [1] for hyperdrive enabled
    # set start node's distance = 0 and inactive hyperdrive
    dist[0][start] = 0

    # queue to store (distance, node, hyperdrive_active status)
    pq = [(0, start, 0)]

    while pq:
        # get node with the smallest distance/time to travel
        time, node, hyperdrive_active = heapq.heappop(pq)

        # skip node with longer time
        if time > dist[hyperdrive_active][node]:
            continue
            
        # explore all neighbors of the current node
        for neighbor, weight in graph[node]:
            # change travel time if hyperdrive is active
            travel_time = weight if not hyperdrive_active else weight // 2 # halve the time
            new_time = time + travel_time

            # Case 1: continue with current hyperdrive state
            if new_time < dist[hyperdrive_active][neighbor]:
                dist[hyperdrive_active][neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor, hyperdrive_active))

            # Case 2: activate hyperdrive if it's not yet activated
            if not hyperdrive_active and node in hyperdrive_nodes:
                # enable hyperdrive and backtrack to all neighbors with halved travel time
                hyperdrive_new_time = time + (weight // 2)
                if hyperdrive_new_time < dist[1][neighbor]:  # hyperdrive active
                    dist[1][neighbor] = hyperdrive_new_time
                    heapq.heappush(pq, (hyperdrive_new_time, neighbor, 1))
                # add back all neighbors with hyperdrive active for further exploration --> backtracking
                for neighbor_back, weight_back in graph[node]:
                    backtrack_time = time + (weight_back // 2)
                    if backtrack_time < dist[1][neighbor_back]:
                        dist[1][neighbor_back] = backtrack_time
                        heapq.heappush(pq, (backtrack_time, neighbor_back, 1))
    return dist # both sets with and without hyperdrive active

# find the earliest meeting time with hyperdrive option
def earliest_meeting_time(n, m, edges, hyperdrive_nodes):
    # construct the graph using adjacency list
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # run dijkstra's algo from node 1 (xyra's start)
    xyra_dist = dijkstra(n, 1, graph, hyperdrive_nodes)

    # run dijkstra's algo from node n (orion's start)
    orion_dist = dijkstra(n, n, graph, hyperdrive_nodes)

    # check if they can reach each other: if they cannot reach each other's end --> there's no path
    if min(xyra_dist[0][n], xyra_dist[1][n]) == float('inf') or min(orion_dist[0][1], orion_dist[1][1]) == float('inf'):
        return -1
    
    # find the earliest meeting time 
    earliest_time = float('inf')
    for i in range(1, n+1):
        # check max times for each possible Hyperdrive state pair
        meet_time_normal = max(xyra_dist[0][i], orion_dist[0][i])
        meet_time_xyra_hyperdrive = max(xyra_dist[1][i], orion_dist[0][i])
        meet_time_orion_hyperdrive = max(xyra_dist[0][i], orion_dist[1][i])
        meet_time_both_hyperdrive = max(xyra_dist[1][i], orion_dist[1][i])

        # take the minimum of max meeting times (max bc of wait times)
        earliest_time = min(earliest_time, meet_time_normal, meet_time_xyra_hyperdrive, meet_time_orion_hyperdrive, meet_time_both_hyperdrive)

    return earliest_time if earliest_time != float('inf') else -1

if __name__ == "__main__":
    # read input using stdin 
    input = sys.stdin.read().strip().splitlines()

    # parse n nodes, m edges, and the number of h nodes
    n, m, h = map(int, input[0].split())

    # parse hyperdrive nodes into a set
    hyperdrive_nodes = set(map(int, input[1].split()))

    # parse each edge --> (u, v, w)
    edges = [tuple(map(int, line.split())) for line in input[2:]]

    # print the earliest time they can meet
    print(earliest_meeting_time(n, m, edges, hyperdrive_nodes))