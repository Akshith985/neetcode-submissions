from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree with n nodes MUST have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
            
        # 1. Build the adjacency list for the undirected graph
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            
        visited = set()
        
        # 2. DFS to traverse the connected network
        def dfs(node):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)
                    
        # Kick off DFS from any node (node 0 is a safe start)
        dfs(0)
        
        # 3. If we successfully reached all n nodes, it's a valid tree!
        return len(visited) == n