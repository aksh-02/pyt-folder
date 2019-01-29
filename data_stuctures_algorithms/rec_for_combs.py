def func(p, k=1, i=0):
	global arr
	if i==n:
		arr.append(p)
		return
	elif k>n:
		return
	func(p, k+1, i)
	func(p+[k], 1, i+1)

	
n = int(input())
arr = []
func([])
print(arr)
print(len(arr))
