from matplotlib import pyplot as plt
from matplotlib import style
x1=[4,5,8,11]
y1=[3,6,22,10]
x2=[3,5,9]
y2=[5,9,14]
plt.plot(x1,y1,'g',label='Lineone',linewidth=10)
plt.plot(x2,y2,'c',label='Linetwo',linewidth=10)
plt.title('finance')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend() # prints label
plt.grid(True,color='K') #enables grid of color black
plt.show()
