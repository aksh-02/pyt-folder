class Graph:
	def __init__(self,n):
		self.graph={i:[] for i in range(1,n+1)}
		self.edges={}
	
	def add_edge(self,x,y,w):
		self.graph[x].append([y,w])
		self.graph[y].append([x,w])
		self.edges[(x,y)]=w
		
	def create_mst(self,parent):
		mst=[]
		for i in range(2,len(parent)+1):
			mst.append([i,parent[i],self.edges.get((i,parent[i]),0)+self.edges.get((parent[i],i),0)])
		return mst
		
	def min_key(self,key_weights,mst_set):
		m=float('inf')
		for i in self.graph.keys():
			if key_weights[i]<m and mst_set[i]==False:
				m=key_weights[i]
				vert=i
		return vert
		
	def prim(self):
		key_weights={i:float('inf') for i in self.graph.keys()}
		key_weights[1]=0
		mst_set={i:False for i in self.graph.keys()}
		parent={i:None for i in self.graph.keys()}
		parent[1]=-1
		
		for _ in range(len(self.graph.keys())):
			vert=self.min_key(key_weights,mst_set)
			mst_set[vert]=True
			for i in self.graph[vert]:
				if mst_set[i[0]]==False and i[1]<key_weights[i[0]]:
					key_weights[i[0]]=i[1]
					parent[i[0]]=vert
		return self.create_mst(parent)
	
if __name__=="__main__":
	n,m=map(int,input().split())
	g=Graph(n)
	for _ in range(m):
		x,y,w=map(int,input().split())
		g.add_edge(x,y,w)
	print(g.prim())
