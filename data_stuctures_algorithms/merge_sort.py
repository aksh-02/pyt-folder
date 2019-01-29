def merge(s1,s2):
  c=[]
  i=j=0
  while i<len(s1) and j<len(s2):
    if s1[i]<s2[j]:
      c.append(s1[i])
      i+=1
    else:
      c.append(s2[j])
      j+=1
  if i==len(s1):
    c.extend(s2[j:])
  else:
    c.extend(s1[i:])
  return c

def merge_sort(arr):
  if len(arr)<2:
    return arr
  else:
    x,y=merge_sort(arr[0:len(arr)//2]),merge_sort(arr[len(arr)//2:])
    return merge(x,y)


if __name__=='__main__':
  a=list(map(int,input().split()))
  print(merge_sort(a))
  
