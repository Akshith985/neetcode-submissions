from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[int]]) -> list[str]:
        
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
            
        itinerary = []
        
        
        def dfs(airport: str):
            while adj[airport]:
                next_airport = adj[airport].pop()
                dfs(next_airport)
            
            itinerary.append(airport)
            
        dfs("JFK")
        
       
        return itinerary[::-1]