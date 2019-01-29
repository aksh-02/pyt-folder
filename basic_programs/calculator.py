c='y'
while c=='y' or c=='Y':
 a=float(input('enter first character : '))
 s=input('enter arithmetic operator : ')
 b=float(input('enter second character : '))
 if s=='+':
  print('your result is ',a+b)
 elif s=='-':
  print('your result is ',a-b)
 elif s=='*':
  print('your result is ',a*b)
 elif s=='/':
  print('your result is ',a/b)
 else:
  print('plz enter a correct arithmetic operator')
 c=input('press y or Y to continue : ')

