def sq(n):
 return n**2

# assigning a variable a function
f=sq(2)  # here the value is returned
print(f)

g=sq     # here the function is assigned to the variable 'g' (property of first class function)
print(g(3))

# passing a function as an argument
def mappo(func,array):
 k=[]
 for i in array:
  k.append(func(i))
 return k

li=mappo(sq,[3,5,7])  # 'sq' function is passed as an arguent
print(li)

# returning a function as a result from another function

def outfunc(msg):
 def infunc():
  print('boss here is the message : ',msg)
 return infunc

a=outfunc('we are the best') # a becomes equal to infunc
a() # this will execute the inner function


