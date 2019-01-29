import matplotlib.pyplot as plt
x=[1,4,5,3,2,4,3]
y=[10,8,6,9,1,9,4]
plt.scatter(x,y,label='random values',color='c')
plt.legend()
plt.ylabel('y axis')
plt.xlabel('x axis')
plt.title('scatter plot')
plt.show()
