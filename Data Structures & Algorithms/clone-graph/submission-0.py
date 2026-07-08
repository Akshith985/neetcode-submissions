class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Edge case: If the input graph is empty, return None
        if not node:
            return None
            
        # The master mapping vault: Maps original_node -> cloned_node
        old_to_new = {}
        
        def clone_dfs(curr_node):
            # BASE CASE: If we have already cloned this node, 
            # don't recreate it! Return the existing clone instantly.
            if curr_node in old_to_new:
                return old_to_new[curr_node]
                
            # 1. Create a shallow clone copy of the node (value only, empty neighbors for now)
            copy = Node(curr_node.val)
            # Register it in our vault immediately BEFORE recursing on neighbors
            old_to_new[curr_node] = copy
            
            # 2. Replicate the connections
            for neighbor in curr_node.neighbors:
                # Recursively clone the neighbor node, and append it to our clone's neighbors list
                copy.neighbors.append(clone_dfs(neighbor))
                
            return copy

        # Kick off the cloning engine starting from the master entry node
        return clone_dfs(node)
        