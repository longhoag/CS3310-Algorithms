#Name: Long Hoang
import sys

def main():
    # Read number of nodes (n) and edges (m)
    line = sys.stdin.readline().strip()
    if not line:
        return
    n, m = map(int, line.split())
    
    # Create adjacency list for the reversed graph: path for Orion
    # We will store edges in reverse: if input says a->b, we store b->a
    edges = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        edges[b-1].append(a-1)  # Reverse the edge direction

    # We use a bitmask DP approach:
    # dp[mask][u] represents the number of ways to reach node u with the visited nodes set represented by mask.
    # "mask" is a bitmask where the i-th bit is 1 if node i is visited.
    
    full_mask = (1 << n) - 1  # When all nodes are visited, mask = 111...111 (binary)
    dp = [[0]*n for _ in range(1 << n)]
    
    start = n - 1  # Orion starts at node n (0-indexed: n-1)
    end = 0         # Xyra is on node 1 (0-indexed: 0)
    
    # Start state: at the start node with only that node visited
    dp[1 << start][start] = 1
    
    # Compute DP
    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == 0:
                continue
            # Check if u is visited in the current mask
            if (mask & (1 << u)) == 0:
                continue
            
            # Try to move from u to v if v is not visited
            for v in edges[u]:
                if (mask & (1 << v)) == 0:
                    dp[mask | (1 << v)][v] += dp[mask][u]
    
    # The answer is the number of ways to end at node 'end' with all nodes visited
    print(dp[full_mask][end])

if __name__ == "__main__":
    main()