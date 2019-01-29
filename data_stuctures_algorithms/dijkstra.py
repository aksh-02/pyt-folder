# dijkstra's algorithm

class Graph:
	def __init__(self,n,start,edges):  # n is the number of vertices
		self.graph={i:[] for i in range(1,n+1)}
		self.src=start                 # source vertex
		self.edges=edges
		for k in self.edges:
			self.graph[k[0]].append((k[1],k[2]))
			self.graph[k[1]].append((k[0],k[2]))
	
	def min_dist(self,dist,spt_set):
		m=float('inf')
		for i in dist.keys():
			if dist[i]<m and spt_set[i]==None:
				m=dist[i]
				vert=i
		return (vert,m)
	
	def dijk(self):
		dist={i:float('inf') for i in self.graph.keys()}
		dist[self.src]=0
		spt_set={i:None for i in self.graph.keys()}
		for _ in range(len(dist.keys())):
			vert,m=self.min_dist(dist,spt_set)
			spt_set[vert]=m
			for k in self.graph[vert]:
				if m+k[1]<dist[k[0]]:
					dist[k[0]]=m+k[1]
					
		return spt_set
		
if __name__=="__main__":
	n,m=map(int,input().split())
	edges=[]
	for _ in range(m):
		edges.append(list(map(int,input().split())))
	start=int(input())
	g=Graph(n,start,edges)
	print(g.dijk())
