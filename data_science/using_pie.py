import matplotlib.pyplot as plt
shares=[8,6,4,7]
owners=['ram','mohan','ashfaq','sukhi']
cols=['c','m','r','b']
plt.pie(shares,labels=owners,colors=cols,startangle=90,shadow=True,explode=(0,0.2,0,0),autopct='%1.2f%%')
plt.title('ownership distribution of a company')
plt.show()
