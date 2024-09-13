class Graph:
    def __init__(self,inp):
        self.nodes=inp
        self.adj=[ [] for i in range(inp)]

                 
    def Edge(self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)

    def DFS_util(self,source,visited,result):
        result.append(source)
        visited[source]=True
        for node in self.adj[source]:
            if not visited[node]:
                self.DFS_util(node,visited,result)

    def DFS(self,source):
        visited=[False]*self.nodes
        result=[]
        self.DFS_util(source,visited,result)
        return result



    
graph1=Graph(5)

graph1.Edge(1,2)
graph1.Edge(1,4)
graph1.Edge(1,3)
graph1.Edge(4,3)
graph1.Edge(2,5)


print(graph1.DFS(0))