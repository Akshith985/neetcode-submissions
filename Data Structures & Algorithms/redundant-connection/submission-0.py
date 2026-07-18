from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # The nodes are 1-indexed, from 1 to n. 
        # len(edges) is equal to n, so we make our list size n + 1.
        n = len(edges)
        parent = list(range(n + 1))
        
        # Helper function to find the ultimate root boss of a node (with Path Compression)
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
            
        # Helper function to link two nodes together
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            
            # TRAP SPRUNG: If they already share the same root boss, 
            # this edge is redundant and creates a cycle!
            if root1 == root2:
                return False
                
            # Otherwise, merge the groups cleanly
            parent[root1] = root2
            return True

        # Process the edges in order. The first one to return False is our culprit.
        for u, v in edges:
            if not union(u, v):
                return [u, v]