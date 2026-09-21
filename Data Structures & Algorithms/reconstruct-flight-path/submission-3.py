class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for src, des in tickets:
            adj[src].append(des)
        
        res = []
        def dfs(src):
            while adj[src]:
                des = adj[src].pop(0)
                dfs(des)
            res.append(src)
        
        dfs("JFK")
        return res[::-1]