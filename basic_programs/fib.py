'''
def fibo(n):
   if n<=2:      # this is the naive algorithm
      return 1   # it takes exponential time
   else:
      return fibo(n-1)+fibo(n-2)
'''
# here we will use memoization

memo={1:1,2:1}
def fibo(n):
    if n in memo:
        return memo[n]
    else:
        f=fibo(n-1)+fibo(n-2)
        memo[n]=f
        return f
   
if __name__=='__main__':
 print(fibo(int(input('enter an integer above 0 : '))))

