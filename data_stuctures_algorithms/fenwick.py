# Binary Indexed Tree or Fenwick Tree
# Fenwick tree is implemented using an array
# next nodes and parent nodes are different, parent node is used to find the sum from the parent node excluding(parent node) to the child node, while the next node is used to update the value in the next node
# all nodes keep the sum of x(x = pow(2,k) where k is an integer) numbers at different indexes

def construct(arr):
	global bitree
	bitree=[0]*(n+1) # initialized bitree with node 0 as a dumb node
	
	# storing the actual values of bitree using update
	for i in range(n):
		update(i, arr[i])
	
	return bitree
	
def update(i, val):
	i = i+1 # since the input array is 0 indexed but the bitree is 1 indexed

	# travesing all next nodes of i less than n
	while i <= n:
		bitree[i] += val  # add value to the current node
		# update index to the next node
		i += (i&-i) # basically adding the decimal value of the last set bit of i to i
		
def getsum(i): # finding the sum upto kth index
	s = 0
	i =i+1 # since the input array is 0 indexed but the bitree is 1 indexed
	while i > 0:
		s += bitree[i]
		# update index to parent node
		i -= (i&-i)  # basically unsetting the last set bit, also could have done i = i&(i-1)
	return s
	
if __name__ == "__main__":
	arr = [3, 5, 6, -4, 8, 12, 0, 13, 7, 23, 15, 12, 9, 6]
	n = len(arr)
	construct(arr)
	print(getsum(int(input())))  # get sum of all the numbers upto the index mentioned
