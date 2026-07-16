from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Every node starts out as its own standalone component
        parent = list(range(n))
        component_count = n
        
        # Helper function to find the ultimate root boss of a node
        def find(node):
            # Path Compression: points nodes directly to the root boss 
            # to keep future lookups super fast
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
            
        # Helper function to link two nodes together
        def union(node1, node2):
            nonlocal component_count
            root1 = find(node1)
            root2 = find(node2)
            
            # If they belong to different groups, merge them!
            if root1 != root2:
                parent[root1] = root2
                component_count -= 1 # Two groups became one
                return True
            return False # Already in the same group
            
        # Process every edge to merge connected pieces
        for u, v in edges:
            union(u, v)
            
        return component_count