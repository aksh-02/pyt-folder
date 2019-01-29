class Graph:
	def __init__(self):
		self.graph={}

	def add_vertices(self,vertice):
		if vertice not in self.graph:
			self.graph[vertice]=[]

	def add_edges(self, tup):	# tup is a tuple of a pair of vertices
		self.add_vertices(tup[0])
		self.add_vertices(tup[1])
		if tup[1] not in self.graph[tup[0]]:
			self.graph[tup[0]].append(tup[1])
		if tup[0] not in self.graph[tup[1]]:
			self.graph[tup[1]].append(tup[0])

	def generate_edges(self):
		edges=[]
		for i in self.graph.keys():
		    for j in self.graph[i]:
		    	if (j,i) not in edges:
		    		edges.append((i,j))
		    		
		print(edges)
		
	def find_path(self,start_vert,end_vert,path=None):
		if path==None:
			path=[]
		path=path+[start_vert]
		if start_vert not in self.graph.keys():
			return None
		if start_vert==end_vert:
			return path
		for i in graph[start_vert]:
			if i not in path:
				ext_path=self.find_path(i,end_vert)
				if ext_part!=None:
					return ext_part
					
		return 
		
if __name__=="__main__":
	pass
