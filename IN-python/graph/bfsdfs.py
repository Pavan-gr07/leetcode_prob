from collections import deque, defaultdict

# Edges given
edges = [[1, 8], [1, 7], [7, 3], [3, 8]]

# Step 1: Build adjacency list
adj = defaultdict(list)

for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)  # undirected graph

# Step 2: DFS Function
def dfs(node, visited, path):
    visited[node] = True
    path.append(node)

    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, path)

# Step 3: BFS Function
def bfs(start):
    visited = defaultdict(bool)
    q = deque()
    q.append(start)
    visited[start] = True
    path = []

    while q:
        node = q.popleft()
        path.append(node)

        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
    
    return path

# Run DFS
visited_dfs = defaultdict(bool)
dfs_path = []
dfs(1, visited_dfs, dfs_path)

# Run BFS
bfs_path = bfs(1)

# Print results
print("DFS Traversal:", dfs_path)
print("BFS Traversal:", bfs_path)
