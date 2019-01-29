import matplotlib.pyplot as plt
prices=[3,5,56,43,55,546,4,32,45,75,24,13]
priceband=[0,20,40,60,80,100]
plt.hist(prices,priceband,histtype='bar',rwidth=0.5,label='year 2010',color='g')
plt.title('market prices')
plt.ylabel('no. of goods in the range')
plt.xlabel('bands')
plt.legend()
plt.show()
