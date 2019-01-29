def binary_search(arr,x,f,l):
  if l >= f:
    mid=(f+l)//2
    if arr[mid] == x:
      return mid
    elif arr[mid] > x:
      return binary_search(arr,x,f,mid-1)
    else:
      return binary_search(arr,x,mid+1,l)
  else:
    return 'not found'

if __name__=='__main__':
  arr=list(map(int,input('enter array : ').split()))
  arr.sort()
  x=int(input('enter number to be searched : '))
  print('given array is : ',arr)
  print(binary_search(arr,x,0,len(arr)-1))
