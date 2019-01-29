import matplotlib.pyplot as plt
days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]
#the code below is just lines just to add labels 
plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=5)
plt.plot([],[],color='r',label='working',linewidth=5)
plt.plot([],[],color='k',label='playing',linewidth=5)
#the code below for the area or stack plot
plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])
plt.xlabel('days')
plt.ylabel('hours')
plt.title('how hours were spent')
plt.legend()
plt.show()
