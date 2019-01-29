# sieve of eratosthenes
# finding the number of primes between 1 to n

def sieve(n):
	prime={i:True for i in range(2,n+1)}
	p=2
	while p<=pow(n,0.5):
		if prime[p]==True:
			for i in range(p*2,n+1,p):
				prime[i]=False
		p+=1
	return [i for i in prime.keys() if prime[i]]
	
if __name__=='__main__':
	print(sieve(int(input())))
