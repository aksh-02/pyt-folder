def fact(a):
 if a<0:
  return 'invalid input'
 elif a==0:
  return 1
 else:
  return a*fact(a-1) 
i=int(input('say a number for finding factorial: '))
print(fact(i))
