import numpy as n

a=n.array([(1,2,3,4),(4,5,6,7)])
b=n.array([(9,2,3,4),(4,5,6,7)])
print(a)
print(a[0:])
print(a[0:,1]) #shows 2nd element of all rows i.e [0:]  
print(a.sum())
print(a.ndim) #gives the dimensions of an array 
print(a.itemsize) #gives the size of the elements
print(a.dtype) #gives the datatype of the elements
print(a.reshape(8,1))
print(n.vstack((a,b))) #stacks a over b
print(n.hstack((a,b))) #stacks b's rows with a's rows 
print(a.max())
print(a.min())
print(n.sqrt(a))
print(round(n.std(a),2)) #prints standard deviation
print(a.size)
print(a.shape)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print('sum',a.sum(axis=1))
print(n.log(a))
print(n.log10(a)) #prints log with base 10
print(n.exp(a))
c=n.arange(5)
d=n.arange(3)
print(c) #would print from 0 to 4

print(n.__version__)
print(n.zeros(10,dtype='int'))
print(n.ones((3,5)))      # creates a 3x5 array of ones
print(n.full((3,3),245,dtype='float'))  # creates a 3x3 arry filled with 245
print(n.arange(5,12,2))   # creates an array of integers between 5 and 12 with difference 2 among them
print(n.linspace(1,2,5))  # creates an array of five equally separated numbers between 1 and 2
print(n.random.normal(0,1,(3,3)))  # create a 3x3 array with mean 0 and standard deviation 1
print(n.eye(3))  # create an identity matrix
print(n.random.seed(0))      # set a random seed
print(n.random.randint(5,10,size=6)) # creates a 1d array of size 6 with numbers between 5 and 10
print(n.random.randint(3,16,size=(3,4,5))) # creates a 3d array of size 60 with numbers between 3 and 16

x=n.array([4, 3, 4, 4, 8, 4])
print(x)
y=n.arange(5)
print(y)
z=n.concatenate([x,y])
print(n.concatenate([x,y]))
i=n.array([[1,2,3],[4,5,6]])
j=n.array([[7,8,9],[10,11,12]])
print(i)
print(n.concatenate([i,j],axis=0))
print(n.concatenate([i,j],axis=1))
k=n.arange(15)
a1,a2,a3=n.split(k,[7,10]) # splits k after 7 and 10 elements
print(a1)
print(a2)
print(a3)
grid=n.arange(16).reshape((4,4))
u,l=n.vsplit(grid,[3]) # splits the grid array after 3 rows
print(u)
print(l)

print(n.random.randint(2, size=10)) # 10 labels
t1=[[3,4,5],[3,2,1]]
t2=[[6,8,9],[1,2,3],[4,5,6]]
print(n.dot(t1,t2))
