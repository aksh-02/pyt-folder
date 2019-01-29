# segment trees
import math


class seg_tree:
	def __init__(self, arr):
		n = len(arr)
		k = int(pow(2, math.ceil(math.log(n, 2))))
		self.seg = [None for i in range(2*k)]     # we need only 2*k-1 nodes but we have made an array of 2*k nodes because the first one has been made a dummy node, so as to have the relation parent_index = child_index//2
		self.build(1, 0, n-1, arr)
		print(self.seg)
		
	def build(self, node, start, end, arr):
		if start == end:
			self.seg[node] = arr[start]
		else:
			mid = (start+end)//2
			self.build(2*node, start, mid, arr)
			self.build(2*node+1, mid+1, end, arr)
			self.seg[node] = self.seg[2*node]+self.seg[2*node+1]
			
	def query(self, l, r, node, start, end):
		if l>end or r<start:  # range l-r is completely out of the range of the node
			return 0
		elif l<=start and r>=end:  # range of the node is completely inside the range l-r
			return self.seg[node]
		else:                      # range of the node is partially inside the given l-r range or the range l-r is completely inside the range of the node
			mid = (start+end)//2   # e.g. l>start and r<end
			p1 = self. query(l, r, 2*node, start, mid)
			p2 = self. query(l, r, 2*node+1, mid+1, end)
			return p1+p2
			
	def update(self, arr, i, val):
		dif = arr[i]-val
		arr[i] = val
		self.upd(1, 0, len(arr)-1, i, dif)
		return arr
		
	def upd(self, node, start, end, i, dif):
		if i==start==end:
			self.seg[node]-=dif
		elif start<=i<=end:
			self.seg[node]-=dif
			mid = (start+end)//2
			self.upd(2*node, start, mid, i, dif)
			self.upd(2*node+1, mid+1, end, i, dif)
			
			
if __name__ == "__main__":
	arr = [1,2,3,4,5,6,7,8]
	st = seg_tree(arr)
	print(st.query(4, 9, 1, 0, len(arr)-1))   # prints the sum of the elements from index 7 to 9
	arr = st.update(arr, 5, 17)
	arr = st.update(arr, 9, 14)
	print(st.seg)
	print(st.query(4, 9, 1, 0, len(arr)-1))
