import matplotlib.pyplot as plt
plt.bar([1,3,5,7,9],[4,6,7,5,3],label='Example one')
plt.bar([2,4,6,8,10],[1,9,12,3,5],label='Example two',color='g')
plt.legend()
plt.ylabel('Heights in m')
plt.xlabel('Building number')
plt.title('Housing Complex')
plt.show()
