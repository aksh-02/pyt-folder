# Disjoint Sets or Union-Find data structure

class Disjoint_sets:

	def __init__(self,arr):
		self.parent={i:i for i in arr}
		self.rank={i:0 for i in arr}
		

	'''
	def find(self,x):			# without path compression
		if self.parent[x]==x:
			return x
		else:
			return find(self.parent[x])
	'''

	def find(self,x):			# with path compression
		if self.parent[x]!=x:
			self.parent[x]=self.find(self.parent[x])
		return self.parent[x]
	'''	
	def union(self,x,y):
		x_root=self.find(x)
		y_root=self.find(y)
		if x_root==y_root:
		    return
		self.parent[x_root]=y_root
	'''
	def union(self,x,y):       # union by rank
		x_root=self.find(x)
		y_root=self.find(y)
		if x_root==y_root:
		    return
		if self.rank[x_root]<self.rank[y_root]:
		    self.parent[x_root]=y_root
		elif self.rank[x_root]>self.rank[y_root]:
		    self.parent[y_root]=x_root
		else:
		    self.parent[x_root]=y_root
		    self.rank[y_root]+=1
    

if __name__=="__main__":
	
	d_s=Disjoint_sets([i for i in range(10)])
	d_s.union(2,4)
	d_s.union(8,9)
	d_s.union(3,4)
	d_s.union(6,4)
	d_s.union(8,4)
	d_s.union(2,8)
	print(d_s.parent)
